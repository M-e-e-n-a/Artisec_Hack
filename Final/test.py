from flask import Flask, request, render_template, redirect, session
from generate_url import *
from datetime import datetime
from QR import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///finance.db"
db = database()

db2=SQLAlchemy(app)

class Sdata(db2.Model):
    id=db2.Column(db2.Integer, primary_key=True)
    usn=db2.Column(db2.String(100), nullable=False)
    dob=db2.Column(db2.String, nullable=False)

    def __repr__(self) -> str:
        return f'{self.usn} :- {self.dob}'

with app.app_context():
    db2.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usn =  request.form['usn']
        dob = request.form['dob']
        temp = Sdata(usn = usn, dob=dob)
        db2.session.add(temp)
        db2.session.commit()

        return redirect(f'/dashboard/{usn}/{dob}')

    return render_template('login.html')

@app.route('/dashboard/<string:usn>/<string:dob>', methods=['GET', 'POST'])
def dashboard(usn,dob):
    return "done"


@app.route('/add_device', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add_this', methods=['GET', 'POST'])
def add_this():
    ip= request.remote_addr
    details = Sdata.query.all()
    details = details[-1]
    usn = details.usn
    dob = details.dob
    whitelist(ip, usn ,dob)
    return render_template('deviceadd.html', ip=ip)

@app.route('/add_other', methods=['GET', 'POST'])
def add_other():
    details = Sdata.query.all()
    details = details[-1]
    usn = details.usn
    count= get_count(usn)
    return render_template('choice.html', allowed=count)

@app.route('/add_mobile', methods=['GET', 'POST'])
def add_mobile():
    endpoint = generate_url()
    url='127.0.0.1:5000'+endpoint
    obj = qr()
    obj.generate(url)
    return render_template('mobile.html')

@app.route('/add_laptop', methods=['GET', 'POST'])
def add_laptop():
    endpoint = generate_url()
    url='127.0.0.1:5000'+endpoint
    surl = shorten_url(url)
    return render_template('laptop.html',surl=surl)


@app.route('/generate/<uuid:token>', methods=['GET', 'POST'])
def generate(token):
    ip= request.remote_addr
    details = Sdata.query.all()
    details = details[-1]
    usn = details.usn
    dob = details.dob
    t = whitelist(ip,usn,dob)
    if t == "not allowed":
        return render_template('notallowed.html')
    elif t == "already allowed":
        return render_template('alreadyallowed.html')
    else:
        return render_template('success.html',ip=ip, count = get_count(usn))

if __name__ == '__main__':
    app.run(debug=True)