import web  #Se importa la libreria we.py pip install web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria para permitir el uso del formato JSON

urls = (
    '/login', 'Login',
    '/bienvenida', 'Bienvenida',
) #Se ingresa una pagina raiz

app = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('views') # se configura la carpeta en donde se encontraran nuestros archivos html 


class Bienvenida:
    def GET(self): # se menciona al ingresar a la ruta de bienvenida 
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return web.seeother("login") # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                #Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.bienvenida() # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida.GET: {}".format(error)) # se imprime el error atrapado


class Login: 
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
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se crea un objeto para conectarse con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            password= formulario.password # se alamcena el valor de password del formulario
            print(email,password) # se imprimen para verificar los valores recibidos
            user = auth.sign_in_with_email_and_password(email, password) # se hace la autenticacion con firebase
            print(user['localId']) # si los datos son correctos se recibe informacion del usuario y se imprime el localID
            web.setcookie('localID', user['localId'], 3600) # se almacena en una cookie el localID
            print("localId: ",web.cookies().get('localID')) # se imprime la cookie para verificar que se almaceno correctamente
            return web.seeother("bienvenida") # Redirecciona a otra pagina web 
        except Exception as error: # atrapa algun error
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('localID', None, 3600) # se resetea el localID en la cookie
            return render.login(message) # se muestra nuevamente login mostrando el mensaje de error

if __name__ == "__main__":
    web.config.debug = False # Activa o desactiva el modo de repuracion de firebase
    app.run() # ejecuta al web app    