from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the database URI for SQLite (in-memory database)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(20), unique=True, nullable=False)
    dob = db.Column(db.String(10), nullable=False)

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usn = request.form['usn']
        dob = request.form['dob']

        # Check if the entered login and password match the predefined values
        user = User.query.filter_by(usn=usn, dob=dob).first()

        if user:
            return 'Logged in successfully!'  # Redirect to a success page or perform further actions
        else:
            return 'Invalid login or password'  # Display an error message if the login or password is incorrect

    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()

