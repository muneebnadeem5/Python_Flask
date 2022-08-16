from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return   "<h1>Welcome to My_Application Index Page....! </h1> "


@app.route("/Hi!/")
def who():
    return   "<h1>Who are you</h1>"

@app.route("/Hi!/<username>")
def greet(username):
    return   f"<h1>Hi! There, {username}! </h1>"
