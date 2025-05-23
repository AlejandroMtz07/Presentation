from flask import Flask, render_template, request
from flask_mail import Mail, Message
import requests
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/me")
def me():
    return render_template("introduction.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/mail",methods=['POST'])
def send_mail():
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        requests.post(
            os.getenv('FORMSPREE'),
            data={
                 "name":name,
                 "email":email,
                 "message":message
            },
            headers={"Accept":"aplication/json"}
        )
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)