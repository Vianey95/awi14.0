import web #se importa la libreria web.py
import pyrebase #se importa la libreria pyrebase
import firebase_config as token
import json #se importa json para permitir el uso del formato json

urls = (
    '/registrar', 'Registrar',
    '/login', 'Login' #raiz de las paginas web
)
app1 = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('views') # se configura la carpeta en donde se encontraran nuestros archivos html 

class Login:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Login.GET email: ",web.cookies().get('email')) # se imprime el valor de localIdd
            if web.cookies().get('email') == None: # Validar si el usuario esta logueado
                return web.seeother("/") # si no esta logueado renderiza a login
            else: 
                return render.login() #se renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Login.GET: {}".format(error)) 

class Registrar:
    def GET(self):
        try: # prueba el siguiente bloque de codigo
            message = None
            return render.registrar(message) # renderiza la pagina registrar.html con el mensaje
        except Exception as error: # atra algun error
            message = "Error en el sistema" # se alamacena un mensaje de eror
            print("Error Registrar.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.registrar(message) # se renderiza nuevamente login con el mensaje de error  
            
    def POST(self):
        try:
            message = None
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se realiza la autenticacion con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            db = firebase.database() # creo la base de datos en firebase 
            formulario = web.input() #Indico el formulario html
            name = formulario.name #Se almacena en campo name del formulario
            phone= formulario.phone #Se almacena en campo phone del formulario
            email = formulario.email #Se almacena en campo email del formulario
            password= formulario.password  #Se almacena en campo password del formulario
            print("Nombre: ",name) #Imprimo nombre por terminal para comprobar datos
            print("Telefono: ",phone) #Imprimo telefono por terminal para comprobar datos
            print("Email: ",email) #Imprimo email por terminal para comprobar datos
            user =auth.create_user_with_email_and_password(email, password) #Codigo para crear usuarios
            print("localId: ",user['localId']) #obtengo el localId del usuario registrado y lo imprimo
            #Agrego los datos del usuario
            data ={
                "name": name,
                "phone": phone,
                "email": email
            }
            results = db.child("users").child(user['localId']).set(data)  
            print(results)
            web.setcookie('email',email, 3600) # se almacena en una cookie el localIdd
            print("email:",web.cookies().get('email')) # se imprime la cookie 
            return web.seeother("/") # Redirecciona a login que es otra pagina web  
        except Exception as error: # atrapa algun error
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error registrar.POST: {}".format(message)) # se imprime el message enviado por firebase
            return render.registrar(message)   
if __name__ == "__main__":
    web.config.debug = False # se desactiva el modo de repuracion de firebase
    app1.run()

