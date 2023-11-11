from flask import Flask
from . import views



def create_app():

    app = Flask(__name__)
    app.register_blueprint(views.bp)
    app.config.from_object('app.config')
    return app

