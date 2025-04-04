from flask import Flask
from config import Config
from flask_mail import Mail

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)
    with app.app_context():
        from app import routes

    return app