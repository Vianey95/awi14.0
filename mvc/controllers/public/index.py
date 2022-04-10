import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria (JSON)



index = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html 
render_plain = web.template.render('mvc/views/operador/') # se menciona la carpeta en donde se encontraran nuestros archivos html


class Index: #clase index
    def GET(self):
        return render.index()
    def POST(self): 
            return render.index()

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
            all_users = db.child("usuarios").get() #obtiene todos los usuarios
            for user in all_users.each():
                if user.key() == localIdd and user.val()['level'] == "admin": #compara el localId y el email
                    if user.val()['status'] == 'true':
                        return web.seeother('/bienvenida') #redirecciona a la pagina de admin
                    else:
                        admin = user.val()['level'] == "admin"
                        return web.seeother('/login')
                elif user.key() == localIdd and user.val()['level'] == "operador":
                    if user.val()['status'] == 'true':
                        return web.seeother('/bienvenida2') #redirecciona a la pagina de operador
                    else:
                        admin = user.val()['level'] == "admin"
                        return web.seeother('/login')
        except Exception as error: # atrapa algun error
            formato = json.loads(error.args[1]) # Error en formato JSON 1 puede variar segun el numero que indiques (son parte del codigo de error json)
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('localIdd', None, 3600)
            return render.login(message) # se muestra nuevamente login mostrando el mensaje de error

class Bienvenida:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localIdd')) # se imprime el valor de localIdd
            if web.cookies().get('localIdd') == None: # Validar si el usuario esta logueado
                return web.seeother("bienvenida") # si no esta logueado renderiza a login
            else: 
                return render.bienvenida() #se renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida.GET: {}".format(error)) 
class Bienvenida2:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida2.GET localID: ",web.cookies().get('localIdd')) # se imprime el valor de localIdd
            if web.cookies().get('localIdd') == None: # Validar si el usuario esta logueado
                return web.seeother("bienvenida2") # si no esta logueado renderiza a login
            else: 
                return render_plain.bienvenida2() #se renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida2.GET: {}".format(error)) 


class Recuperar: #clase recuperar password
    def GET(self): 
        message = None
        return render.recuperar(message)

    def POST(self):
        try: 
            message= None
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            recuperacion =auth.send_password_reset_email(email) #codigo para recuperar contraseña almacenado en una variable
            print(recuperacion)
            return web.seeother("/login") 
        except Exception as error:
            formato = json.loads(error.args[1]) 
            error = formato['error'] 
            message = error['message']
            print("Error recuperar.POST: {}".format(message))
            return render.recuperar(message)         
class Registrar: 
    def GET(self):
        message = None
        return render.registrar(message)

    def POST(self):
        try:
            message = None
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input()
            nombre = formulario.nombre
            telefono = formulario.telefono
            email = formulario.email
            password= formulario.password
            nivel = formulario.nivel
            estado = formulario.estado
            user = auth.create_user_with_email_and_password(email, password) 
            datos_user = {'nombre': nombre, 'telefono': telefono, 'email':email, 'nivel':nivel, 'estado':estado} 
            results = db.child("usuarios").child(user['localId']).set(datos) 
            print(datos_user)
            print(results)
            return web.seeother('/lista_user') 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error registrar.POST: {}".format(message)) 
            return render.registrar(message)  
if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    index.run() # ejecuta al web app   