from flask import Flask
from dotenv import load_dotenv
import os 
from app.extensions import db, migrate
from app.routes import main_bp


load_dotenv()


def create_app():
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(main_bp)



    return app