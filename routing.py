from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/home')
def home():
    return 'Hello World!'

#Add variable to URL

@app.route('/user/<name>')
def username(name):
    return 'Hello {}'.format(name)
