from app import appInstance
from flask import render_template, send_from_directory, request

@appInstance.route('/login', methods=['GET', 'POST'])  # Notice methods parameter! this toure must be able to handle mutliple types of requests!
def login(): 
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # Handle form submission
        email = request.form['email']
        password = request.form['password']
        
        #print(f"Email: {email}, Password: {password}")
        return "Login form submitted! Check your terminal."