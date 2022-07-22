from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "app.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfsdfsdfdsf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)
    login.login_view = 'login'
    
    from .models import User
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    from .views import views
    from .auth import auth
    from . import models
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    
    
    return app
