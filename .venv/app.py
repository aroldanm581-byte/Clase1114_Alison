from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Aplication 11-14 by Alison!</p>"
