import web #se importa la libreria web.py
import pyrebase #se importa la libreria pyrebase
import firebase_config as token
import json #se importa json para permitir el uso del formato json

urls = (
    '/registrar', 'Registrar',
    '/login', 'Login', #raiz de las paginas web
)
app1 = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('views') # se configura la carpeta en donde se encontraran nuestros archivos html 

class Login:
    def GET(self): # se menciona al ingresar a la ruta de login
        try: # prueba el siguiente bloque de codigo
            print("Login.GET Email: ",web.cookies().get('Email')) # se imprime el valor de email para verificarlos
            if web.cookies().get('Email') == None: # Si email es None se redirecciona a registrar.html
                return web.seeother("registrar") # se redirecciona al registrar.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.login() # renderiza login.html
        except Exception as error: # se atrapa algun error
            print("Error Login.GET: {}".format(error)) # se imprime el error atrapado

class Registrar:
    def GET(self):
        try: # prueba el siguiente bloque de codigo
            message = None # se crear una variable para el mensaje de error
            return render.registrar(message) # renderiza la pagina tegistrar.html con el mensaje
        except Exception as error: # atra algun error
            message = "Error en el sistema" # se alamacena un mensaje de eror
            print("Error Registrar.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.registrar(message) # se renderiza nuevamente registrar con el mensaje de error   
            
    def POST(self):
        try:
            message = None
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() #se crea una variable formulario para almacenar los datos de registrar
            email = formulario.email #se almacema el valor email en el formulario
            password= formulario.password # se almacena el valor en el formulario
            auth.create_user_with_email_and_password(email, password) #codigo para crear usuarios
            print("Su cuenta ha sido registrada :)") #Un mensaje que ayudara a verificar la creacion
            print(email) #se imprime email
            web.setcookie('Email', email, 3600) # se almacena en una cookie el email
            print("Email: ",web.cookies().get(email)) # se imprime la cookie para verificar que se almaceno correctamente
            return web.seeother("login") # Redirecciona a login que es otra pagina web  
        except Exception as error: # atrapa algun error
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Registrar.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('Email', None, 3600) # se resetea el email en la cookie
            return render.registrar(message)   

if __name__ == "__main__":
    web.config.debug = False # se desactiva el modo de repuracion de firebase
    app1.run()

