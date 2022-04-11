import web
import app
import pyrebase
import mvc.firebase_config as token

render = web.template.render("mvc/views/admin/")


class Sucursales:
    def GET(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth() 
        db = firebase.database()
        sucu_1 = db.child("sensores").child("sucursal_1").child("enfriamiento").get()
        sucu_2 = db.child("sensores").child("sucursal_2").child("enfriamiento").get()
        return render.sucursales(sucu_1,sucu_2)
    def POST(self):
        form = web.input()
        sucur_1 = form.enfriamiento_1
        sucur_2 = form.enfriamiento_2
        db.child("sensores").child("sucursal_1").update({"enfriamiento": sucur_1})
        db.child("sensores").child("sucursal_2").update({"enfriamiento": sucur_2})
        localId = web.cookies().get('localId')
        sucu_1 = db.child("sensores").child("sucursal_1").child("enfriamiento").get()
        sucu_2 = db.child("sensores").child("sucursal_2").child("enfriamiento").get()
        return render.sucursales(sucu_1, sucu_2)


