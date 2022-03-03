import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria (JSON)

urls = (
    '/login', 'Login',
    '/recuperar' , 'Recuperar'
)

recuperar = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('views')

class Recuperar: #clase recuperar password
    def GET(self):
        return render.recuperar()
    def POST(self): 
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            print("Email:",email)
            recuperacion =auth.send_password_reset_email(email) #codigo para recuperar contraseña almacenado en una variable
            print(recuperacion)
            return render.recuperar()
            
if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    recuperar.run() # ejecuta al web app    

