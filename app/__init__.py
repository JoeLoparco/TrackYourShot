#Imports said Object Constrcutor from flask library
from flask import Flask
#Creates instance of a Flask Application
appInstance = Flask(__name__, template_folder='templates')
#IN the name of thorughoussness I will tell you what this does if you cou;dn't figur it out. it importes the routes.py from our app package
from app.routes import routes
from app.routes import auth