import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import json
import app
import firebase_config as token
render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html


class Lista_user:
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            users = db.child("usuarios").get() 
            return render.usuarios(users) 
        except Exception as error:
            return render.usuarios(error)   