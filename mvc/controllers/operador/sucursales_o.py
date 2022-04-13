import web
import app
import pyrebase
import mvc.firebase_config as token

render = web.template.render("mvc/views/operador/")


class Sucursales_o:
   def GET (self):
        firebase= pyrebase.initialize_app(token.firebaseConfig)
        
        ba =firebase.database()
        sensores = ba.child("sensores").get()
        return render.sucursales_o()