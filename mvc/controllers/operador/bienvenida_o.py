import web  #se importa la libreria web.py
import app
import mvc.firebase_config as token


render = web.template.render('mvc/views/operador/') # se menciona la carpeta en donde se encontraran nuestros archivos html 


class Bienvenida_o: #clase index
    def GET(self):
        return render.bienvenida_o()
    def POST(self): 
            return render.bienvenida_o()
  

