import web  #se importa la libreria web.py
import app


index = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/public/') # se menciona la carpeta en donde se encontraran nuestros archivos html 



class Logout: #clase loguot
    def GET(self):
        web.setcookie('localIdd' == None) # Cambiar el valor de localidd a vacio 
        return render.seeother("/") #renderizar a loguot

class Logout: #clase index
    def GET(self):
        return render.index()
    def POST(self): 
            return render.index()