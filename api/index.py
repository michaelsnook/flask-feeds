from flask import Flask

app = Flask(__name__)


@app.route('/feeds/indiasky')
def home():
    return {"hello": "world"}


@app.route('/feeds/about')
def about():
    return 'About'
