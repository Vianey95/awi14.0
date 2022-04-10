import web  #se importa la libreria web.py
import app

recuperar = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/public')
class Recuperar: #clase recuperar password
    def GET(self): 
        message = None
        return render.recuperar(message)

    def POST(self):
        try: 
            message= None
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            recuperacion =auth.send_password_reset_email(email) #codigo para recuperar contraseña almacenado en una variable
            print(recuperacion)
            return web.seeother("/login") 
        except Exception as error:
            formato = json.loads(error.args[1]) 
            error = formato['error'] 
            message = error['message']
            print("Error recuperar.POST: {}".format(message))
            return render.recuperar(message)   
if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    recuperar.run() # ejecuta al web app    

