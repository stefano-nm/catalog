import json
import logging
from typing import Any

import cherrypy
import requests

from catalog import Catalog
from config import config

if __name__ == "__main__":
    cherrypy.tree.mount(Catalog(**config, debug=True), "/", {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()
        }
    })
    cherrypy.engine.start()
    _, port = cherrypy.server.bound_addr
    endpoint = f"http://localhost:{port}"
    logging.basicConfig(level=logging.INFO)

    def get(method: str, **params: Any):
        query = f"{endpoint}/{method}"
        if len(params) > 0:
            query += "?" + "&".join([f"{name}={value}" for name, value in params.items()])
        response = requests.get(query)
        if response.status_code == 200:
            logging.info(method.upper() + ":" + json.dumps(response.json()))
        else:
            logging.info(method.upper() + ":" + str(response.status_code))

    get("service", name="test")
    get("register", name="test", endpoint="test")
    get("service", name="test")
    get("register", name="test", endpoint="test_modified", token="test")
    get("service", name="test")
    get("unregister", name="test", token="wrong")
    get("service", name="test")
    get("unregister", name="test", token="test")
    get("service", name="test")
    get("catalog")

    cherrypy.engine.block()
