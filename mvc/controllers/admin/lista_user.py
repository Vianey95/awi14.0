import web  #se importa la libreria web.py
import pyrebase #Se importa la libreria para conectarse a la firebase pip install pyrebase4
import firebase_config as token 
import json # se importa la libreria (JSON)


lista_user = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/admin/') # se menciona la carpeta en donde se encontraran nuestros archivos html 

class Lista_user:
    def GET(self): #se invoca al entrar ala ruta /bienvenida
        cookies = web.cookies().get('localIdd')
        all_users = db.child("usuarios").get()
        for user in all_users.each():
            usuario=user.keys()
            if usuario ==  cookies:
                usuario = user.val()
                nombre = usuario['name']
                return render.lista_user(name)
            else:
                return web.seeother('/bienvenida')    
       

if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    lista_user.run() # ejecuta al web app     