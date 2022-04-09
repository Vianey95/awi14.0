import web

urls = (
    '/', 'mvc.controllers.public.index.Index' ,
    "/", "mvc.controllers.admin.app.login",
    "/", "mvc.controllers.admin.app.bienvenida"
    
    
)
app = web.application(urls, globals()) 

if __name__ == "__main__":
    app.run()