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
    
@appInstance.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')
    elif request.method == 'POST':
        # Grab User Info from Forms in the HTML page
        email = request.form['email']
        password = request.form['password']
        userName = request.form['userName']

        #[TODO]# Query DB to See if User Exits 
        user = User.query.filter_by(email=email, password=password).first()
        if user is not None:
            return f"Sorry a USer Already Exists with those Credential Please Try a new email"
        #[TODO]# Add User to the DB if they dont exist
        else:
            with appInstance.app_context(): ## Nedded when Working with Ative Db gives flask our 'context'
                new_user = User(
                    email= email,
                    password= password,  # We'll hash this later
                    username= userName
                )
                db.session.add(new_user)
                db.session.commit()

            return render_template('signUpCompleted.html')
