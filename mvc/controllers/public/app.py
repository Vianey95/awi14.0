import web  #se importa la libreria web.py
import app


app = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/public/') # se menciona la carpeta en donde se encontraran nuestros archivos html 
 

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
                elif user.key() == localId and user.val()['level'] == "operador":
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

 