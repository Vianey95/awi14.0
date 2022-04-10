import web  #se importa la libreria web.py
import app
import mvc.firebase_config as token


render = web.template.render('mvc/views/operador/') # se menciona la carpeta en donde se encontraran nuestros archivos html 


class Bienvenida_o:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localIdd')) # se imprime el valor de localIdd
            if web.cookies().get('localIdd') == None: # Validar si el usuario esta logueado
                return web.seeother("bienvenida_o") # si no esta logueado renderiza a login
            else: #si no 
                #TODO UN IF
                return render.bienvenida_o() #se renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida.GET: {}".format(error)) 

