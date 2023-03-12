import cherrypy

from catalog import Catalog
from config import config


def create_app():
    app = cherrypy.tree.mount(Catalog(**config), "/", {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()
        }
    })
    cherrypy.config.update({'engine.autoreload.on': False})
    cherrypy.server.unsubscribe()
    cherrypy.engine.start()
    return app
