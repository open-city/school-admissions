from flask import Flask
from api.endpoints import endpoints
from api.views import views

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.app_config')
    app.register_blueprint(endpoints)
    app.register_blueprint(views)
    return app
