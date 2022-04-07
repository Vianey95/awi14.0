import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria (JSON)

urls = (
    '/index', 'Index', 
    '/login', 'Login'#raiz/ clase
    
) #url de las paginas a acceder

index = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/public') # se menciona la carpeta en donde se encontraran nuestros archivos html 

class Index: #clase recuperar password
    def GET(self):
        return render.index()
    def POST(self): 
            return render.index()
if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    index.run() # ejecuta al web app   