import web  #se importa la libreria web.pyimport pyrebase
import pyrebase
import json
import mvc.firebase_config as token
urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/login', 'mvc.controllers.public.login.Login',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',
    '/logout', 'mvc.controllers.public.logout.Logout',
    '/bienvenida', 'mvc.controllers.admin.bienvenida.Bienvenida',
    '/bienvenida_o', 'mvc.controllers.operador.bienvenida_o.Bienvenida_o',
    '/lista_user', 'mvc.controllers.admin.lista_user.Lista_user',
    '/registrar', 'mvc.controllers.admin.registrar.Registrar',
    '/actualizar', 'mvc.controllers.admin.actualizar.Actualizar',

    
) #url de las paginas a acceder

    
app = web.application(urls, globals()) 

if __name__ == "__main__":
    web.config.debug = False 
    app.run()