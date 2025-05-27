from app import appInstance, db, User
from flask import render_template, request, session, redirect

@appInstance.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Look up user in database
        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
            session['user_id'] = user.id
            return render_template('loginValid.html')
        else:
            return render_template('loginInvalid.html')