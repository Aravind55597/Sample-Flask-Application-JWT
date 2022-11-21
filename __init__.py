import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from .admin import setup_admin
from .commands import setup_commands
from .utils import db; 
from flask_sqlalchemy import SQLAlchemy; 
from .routes import api; 

def create_app(): 

    ENV = os.getenv("FLASK_ENV")
    app = Flask(__name__)

    # database configuration--------------------------------------------------------------------------------------------------------------------------------------
    db = SQLAlchemy(app)

    db_url = os.getenv("DATABASE_URL")

    if db_url is not None:
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
            "postgres://", "postgresql://")
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Create database---------------------------------------------------------------------------------------------------------------------------------------------
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(80), unique=False, nullable=False)
        is_active = db.Column(db.Boolean(), unique=False, nullable=False)

        def __repr__(self):
            return f'<User {self.email}>'

        def serialize(self):
            return {
                "id": self.id,
                "email": self.email,
                # do not serialize the password, its a security breach
            }
    db.create_all(app=app)
    
    # Allow CORS requests to this API-----------------------------------------------------------------------------------------------------------------------------
    CORS(app)

    # add the admin-----------------------------------------------------------------------------------------------------------------------------------------------
    # setup_admin(app)

    # set up ability to seed database-----------------------------------------------------------------------------------------------------------------------------
    setup_commands(app)

    # Register your blueprints------------------------------------------------------------------------------------------------------------------------------------
    app.register_blueprint(api, url_prefix='/api')

    return app; 
