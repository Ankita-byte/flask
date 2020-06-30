from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/home')
def home():
    return 'Hello World!'