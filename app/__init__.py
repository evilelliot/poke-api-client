# ./app/__init__.py
from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

def create_app():
    app = Flask(__name__)

    app.jinja_loader = ChoiceLoader([
        FileSystemLoader('app/views'),
        FileSystemLoader('app/templates')
    ])
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
