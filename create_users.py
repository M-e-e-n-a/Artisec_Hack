from app import create_app, db, User

# Create the Flask application instance
app = create_app()

# App context is necessary to work with the database
with app.app_context():
    # Create the database tables (if they don't exist)
    db.create_all()

    # Insert predefined user data
    user1 = User(usn='1ms21cs110', dob='2004-01-31')
    user2 = User(usn='1ms21cs129', dob='2004-01-31')

    # Add the users to the database
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

print("Predefined users created successfully!")
