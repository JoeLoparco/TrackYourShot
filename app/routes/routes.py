from app import appInstance
from flask import render_template, send_from_directory

@appInstance.route('/') # Home page 'Route'
def home(): # Def home function for home page
    return render_template('index.html') # Returns Asscoaited HTML File using flask library render_template
@appInstance.route('/learnMore') # Home page 'Route'
def learnMore(): # Def home function for home page
    return render_template('learnMore.html') # Returns Asscoaited HTML File using flask library render_template
