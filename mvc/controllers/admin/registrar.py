import web
import app
import pyrebase
import mvc.controllers.public.firebase_config as token
import json

render = web.template.render("mvc/views/admin/")
registrar = web.application(urls, globals()) # configura las urls en la aplicacion web

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
            return web.seeother('/lista_user') 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error registrar.POST: {}".format(message)) 
            return render.registrar(message) 