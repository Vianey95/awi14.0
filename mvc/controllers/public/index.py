import web  #se importa la libreria web.py
import app
import firebase_config as token

render = web.template.render('mvc/views/public/') # se menciona la carpeta en donde se encontraran nuestros archivos html 


class Index: #clase index
    def GET(self):
        return render.index()
    def POST(self): 
            return render.index()
  