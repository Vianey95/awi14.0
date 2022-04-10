import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import json
import app
import mvc.firebase_config as token

render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html 

class Bienvenida:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localId')) # se imprime el valor de localIdd
            if web.cookies().get('localId') == None: # Validar si el usuario esta logueado
                return web.seeother("bienvenida") # si no esta logueado renderiza a login
            else: #si no 
                #TODO UN IF
                return render.bienvenida() #se renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida.GET: {}".format(error))  