import web
import pyrebase
import firebase_config as token

urls = (
    '/login', 'Login'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth()
        formulario = web.input()
        email = formulario.email
        password= formulario.password
        print(email,password)
        return render.login()    

if __name__ == "__main__":
    app.run()