import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria (JSON)


bienvenida = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html 

class Logout: #clase loguot
    def GET(self):
        web.setcookie('localIdd' == None) # Cambiar el valor de localidd a vacio 
        return render.seeother("/index") #renderizar a loguot

class Bienvenida2:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localIdd')) # se imprime el valor de localIdd
            if web.cookies().get('localIdd') == None: # Validar si el usuario esta logueado
                return web.seeother("bienvenida") # si no esta logueado renderiza a login
            else: #si no 
                #TODO UN IF
                return render.bienvenida() #se renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida2.GET: {}".format(error)) 

if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    bienvenida.run() # ejecuta al web app 