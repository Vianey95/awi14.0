import web
import pyrebase
import app
import firebase_config as token
import json

urls = (
    '/registrar', 'Registrar', #raiz/ clase
    '/bienvenida', 'Bienvenida',
    '/logout' , 'Logout'
    '/recuperar' , 'Recuperar'
) #url de las paginas a acceder

app = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/admin') # se menciona la carpeta en donde se encontraran nuestros archivos html 
class Registrar: 
    def GET(self):
        message = None
        return render.registrar(message)

    def POST(self):
        try:
            message = None
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input()
            nombre = formulario.nombre
            telefono = formulario.telefono
            email = formulario.email
            password= formulario.password
            nivel = formulario.nivel
            estado = formulario.estado
            user = auth.create_user_with_email_and_password(email, password) 
            datos_user = {'nombre': nombre, 'telefono': telefono, 'email':email, 'nivel':nivel, 'estado':estado} 
            results = db.child("usuarios").child(user['localId']).set(datos_user) 
            print(datos_user)
            print(results)
            return web.seeother('/index') 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error registrar.POST: {}".format(message)) 
            return render.registrar(message) 

if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    app.run() # ejecuta al web app 