import web
import pyrebase
import app
import mvc.firebase_config as token
import json

render = web.template.render('mvc/views/admin') # se menciona la carpeta en donde se encontraran nuestros archivos html 
class Actualizar: 
    def GET(self, localId):
        return render.actualizar()
    def POST(self,localId):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            users= db.child("usuarios").child(user['localId']).get() 
            formulario = web.input()
            nombre = formulario.nombre
            telefono = formulario.telefono
            email = formulario.email
            password= formulario.password
            nivel = formulario.nivel
            estado = formulario.estado
            user = auth.update_user
            datos_user = {'nombre': nombre,
                          'telefono': telefono,
                          'email':email, 
                          'nivel':nivel, 
                          'estado':estado} 
            result=db.child("up").child(nombre).update(datos_user)         
            return web.seeother('/lista_user') 
        except Exception as error:
            print("Error actualizar.POST: {}".format(error)) 
            return web.seeother('/lista_user')
