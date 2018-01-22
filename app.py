from flask import Flask 
from flask import render_template
app = Flask(__name__)

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
