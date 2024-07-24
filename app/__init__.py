from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # Set a secret key for the session
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #Configure Flask-Login 
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))
    
    #Route for testing
    @app.route('/')
    def index():
        return 'Hello, World!'

    # Import and register the routes from routes.py
    from app.routes import app as app_blueprint
    app.register_blueprint(app_blueprint) 

    #Import and register the auth routes from auth_routes.py
    from app.auth_routes import auth_bp 
    app.register_blueprint(auth_bp, url_prefix = '/auth')


    return app
