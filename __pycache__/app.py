import web  #se importa la libreria web.pyimport pyrebase
import pyrebase
import json
urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/login', 'mvc.controllers.public.index.Index',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',
    '/logout', 'mvc.controllers.public.logout.Logout',
    '/bienvenida', 'mvc.controllers.admin.bienvenida.Bienvenida',
    '/bienvenida', 'mvc.controllers.operador.bienvenida.Bienvenida2',
    '/lista_user', 'mvc.controllers.admin.lista_user.Lista_user',
    '/registrar', 'mvc.controllers.admin.registrar.Registrar',

    
) #url de las paginas a acceder



app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    registrar.run() # ejecuta al web app     