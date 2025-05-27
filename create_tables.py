from app import appInstance, db, User

with appInstance.app_context():
    # Create all tables
    db.create_all()
    print("Database tables created!")
    
    # Create a test user
    test_user = User(
        email='loparcoJoseph@gmail.com',
        password='pkwVtk3n!',  # We'll hash this later
        username='Joseph'
    )
    
    db.session.add(test_user)
    db.session.commit()
    print("Test user created!")