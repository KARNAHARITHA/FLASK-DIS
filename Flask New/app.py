from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/index.html")
def index():
    return render_template ("index.html")

@app.route("/html/AboutUS.html")
def AboutUs():
    return render_template ("AboutUS.html")

@app.route("/html/FindYourAdventure.html")
def FindYourAdventure():
    return render_template ("FindYourAdventure.html")

@app.route("/html/GoldenGate.html")
def GoldenGate():
    return render_template ("GoldenGate.html")

@app.route("/html/Login.html")
def Login():
    return render_template ("Login.html")

@app.route("/html/NiagraFalls.html")
def NiagraFalls():
    return render_template ("NiagraFalls.html")

@app.route("/html/PaymentMethod.html")
def PaymentMethod():
    return render_template ("PaymentMethod.html")

@app.route("/html/Signup.html")
def Signup():
    return render_template ("Signup.html")

@app.route("/html/StatueOfLiberty.html")
def StatueOfLiberty():
    return render_template ("StatueOfLiberty.html")


