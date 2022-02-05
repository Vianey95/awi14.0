import web
import pyrebase
import firebase_config as token
urls = (
    '/registrar', 'Registrar'
)
app1 = web.application(urls, globals())
render = web.template.render('views')

class Registrar:
    def GET(self):
        return render.registrar()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth()
        formulario = web.input()
        email = formulario.email
        password= formulario.password
        auth.create_user_with_email_and_password(email, password)
        print("Su cuenta ha sido registrada :)")
        print(email,password)
        return render.registrar()    

if __name__ == "__main__":
    app1.run()