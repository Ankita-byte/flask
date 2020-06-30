from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/home')
def home():
    return 'Hello World!'

#Add variable(String) to URL
@app.route('/user/<name>')
def username(name):
    return 'Hello {}'.format(name)

#Add variable(Integer) to URL
@app.route('/user/<int:age>')
def userage(age):
    return 'You are {} years old'.format(age)
