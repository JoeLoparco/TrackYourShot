# Imports said Object Constructor from flask library
from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load environment variables
load_dotenv()

# Creates instance of a Flask Application
appInstance = Flask(__name__, template_folder='templates')

# Configure database and secret key
appInstance.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
appInstance.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
appInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(appInstance)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Import routes AFTER database setup
from app.routes import routes
from app.routes import auth