from flask import Flask
from .auth import auth_bp
from .detect import detect_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(detect_bp)
    return app
