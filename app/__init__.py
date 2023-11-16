from flask import Flask
from . import views


application = Flask(__name__)
application.register_blueprint(views.bp)
application.config.from_object('app.config')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
