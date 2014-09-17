from flask import Flask
from api.endpoints import endpoints

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.app_config')
    app.register_blueprint(endpoints)
    return app
