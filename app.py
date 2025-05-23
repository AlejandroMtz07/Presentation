from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')

mail = Mail(app)


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
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        msg = Message('Hello',sender=os.getenv('EMAIL'),recipients=[email])
        msg.body = 'Hello i\'m'+name+' and '+message
        mail.send(msg)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)