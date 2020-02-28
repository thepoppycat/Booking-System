from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/homepage')
def index():
    return render_template('index.html',email=True)

@app.route('/booking-consult')
def bookingConsult():
    return render_template('booking-consult.html',email=True)

@app.route('/create')
def bookingCreate():
    return render_template('booking-create.html',email=True)