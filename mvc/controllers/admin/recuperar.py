import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria (JSON)

urls = (
    '/login', 'Login',
    '/recuperar' , 'Recuperar'
)

recuperar = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/admin')

class Recuperar: #clase recuperar password
    def GET(self):
        try: # prueba el siguiente bloque de codigo
            message = None # se crear una variable para el mensaje de error
            return render.recuperar(message) # renderiza la pagina login.html con el mensaje
        except Exception as error: # atra algun error
            message = "Error en el sistema" # se alamacena un mensaje de eror
            print("Error Recuperar.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.recuperar(message) # se renderiza nuevamente login con el mensaje de error
    def POST(self): 
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            print("Email:",email)
            recuperacion =auth.send_password_reset_email(email) #codigo para recuperar contraseña almacenado en una variable
            print(recuperacion)
            return render.recuperar()
         except Exception as error: # atrapa algun error
            formato = json.loads(error.args[1]) # Error en formato JSON 1 puede variar segun el numero que indiques (son parte del codigo de error json)
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Recuperar.POST: {}".format(message)) # se imprime el message enviado por firebase
            return render.recuperar(message) # se muestra nuevamente login mostrando el mensaje de error    
            
if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    recuperar.run() # ejecuta al web app    

