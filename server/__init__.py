from flask import Flask
from flask_restx import Api

from .routes import user, users_api, auth_api, rename_api


def init_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    api.add_namespace(user)
    api.add_namespace(users_api)
    api.add_namespace(auth_api)
    api.add_namespace(rename_api)
    return app
