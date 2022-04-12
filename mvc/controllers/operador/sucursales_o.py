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
        sucu_1_p1 = db.child("UsersData").child("Sucursal_1_Temperatura").get()
        sucu_1_p2 = db.child("UsersData").child("sucursal_1_Humedad").get()
        sucu_1_p11 = db.child("UsersData").child("sucursal_1__2_Temperatura").get()
        sucu_2_p22 = db.child("UsersData").child("sucursal_1_2_Humedad").get()
        return render.sucursales(sucu_1_p1, sucu_1_p2, sucu_1_p11, sucu_2_p22)

