import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import json
import app
import mvc.firebase_config as token
render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html

class Lista_user:
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            datos_user = db.child("usuarios").get()
            print(datos_user)
            return render.lista_user(datos_user) 
        except Exception as error:
            return render.lista_user(error)   