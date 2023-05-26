from flask import Flask, render_template,request
from flask_pymongo import PyMongo
app = Flask(__name__)
mongo=PyMongo(app)
# Home page
@app.route('/')
def home():
    return render_template('index.html')



    
# Link a device
@app.route('/link_device')
def link_device():
    # Add your logic here to handle linking a device
    return "Device linked successfully."

if __name__ == '__main__':
    app.run()
