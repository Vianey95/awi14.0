import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import json
import app
import firebase_config as token

render = web.template.render('mvc/views/public/') # se menciona la carpeta en donde se encontraran nuestros archivos html
render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html
render = web.template.render('mvc/views/operador/') # se menciona la carpeta en donde se encontraran nuestros archivos html

class Login: #clase login
    def GET(self): # se invoca al entrar a la ruta /login
        try: # prueba el siguiente bloque de codigo
            message = None # se crear una variable para el mensaje de error
            return render.login(message) # renderiza la pagina login.html con el mensaje
        except Exception as error: # atra algun error
            message = "Error en el sistema" # se alamacena un mensaje de eror
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.login(message) # se renderiza nuevamente login con el mensaje de error
    def POST(self): # se invoca al recibir el formulario
        try: # prueba el siguiente bloque de codigo
            message = None # se crea una variable para el mensaje de error que se mostrara si la autenticacion es incorrecta
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            password= formulario.password # se alamcena el valor de password del formulario
            print(email,password) # se imprimen para verificar los valores recibidos
            user = auth.sign_in_with_email_and_password(email, password) #codigo para inisiar sesion de usuarios
            web.setcookie('localIdd', user['localId'], 3600) # se almacena en una cookie el localIdd
            print("localId:",web.cookies().get('localIdd')) # se imprime la cookie 
            all_users = db.child("usuarios").get() 
            for user in all_users.each():
                if user.key() == localIdd and user.val()['nivel'] == "admin":
                    if user.val()['estado'] == 'true':
                        return web.seeother('/bienvenida') 
                    else:
                        admin = user.val()['nivel'] == "admin"
                        return web.seeother('/logout')
                elif user.key() == localId and user.val()['nivel'] == "operador":
                    if user.val()['estado'] == 'true':
                        return web.seeother('/bienvenida2') 
                    else:
                        admin = user.val()['nivel'] == "admin"
                        return web.seeother('/logout')
        except Exception as error: 
            formato = json.loads(error.args[1])
            error = formato['error'] 
            message = error['message'] 
            print("Error Login.POST: {}".format(message)) 
            web.setcookie('localIdd', None, 3600)
            return render.login(message) 

 