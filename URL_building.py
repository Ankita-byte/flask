from flask import *
app=Flask(__name__)

@app.route('/animal')
def cat():
    return "I am pet"

@app.route('/user')
def user():
    return redirect(url_for('cat'))
