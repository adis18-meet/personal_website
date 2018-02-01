from flask import Flask 
from flask import render_template
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
from flask import request

class signup(db.Model):
	__tablename__ = "signup"
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(25))
	password = db.Column(db.String(20))
db.create_all()

@app.route('/submit_form', methods=['POST'])
def submit_form():
	username = request.form['uname']
	password = request.form ['psw']
	users = signup.query.all()
	user = signup(username=username, password=password)
	db.session.add(user)
	db.session.commit()
	return render_template("home.html", signuppopup = True, username1 = username)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/workouts")
def workouts():
	urls = [
        'https://www.youtube.com/embed/YdB1HMCldJY',
        'https://www.youtube.com/embed/11WLF24-5iM',
        'https://www.youtube.com/embed/8MPb0O9xApA',
        'https://www.youtube.com/embed/03JKamVnbfs',	
        'https://www.youtube.com/embed/oCB6Cu8PEdI&t=140s',
    ]
	return render_template("workouts.html", urls=urls)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/Quotes")
def quotes():
	return render_template("Quotes.html")
@app.route("/Workoutplans")
def workoutplans():
	return render_template("Workoutplans.html")

@app.route("/abs")
def abs():
	return render_template("abs.html")

@app.route("/glutes")
def glutes():
	return render_template("glutes.html")

@app.route("/chest")
def chest():
	return render_template("chest.html")

@app.route("/arms")
def arms():
	return render_template("arms.html")

@app.route("/legs")
def legs():
	return render_template("legs.html")

@app.route("/fullbody")
def fullbody():
	return render_template("fullbody.html")

@app.route("/login")
def login():
	return render_template("home.html")


