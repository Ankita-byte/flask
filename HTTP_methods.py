from flask import *
app=Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    name=request.form['uname']
    pwd=request.form['pass']
    if name=='Ankita' and pwd=='India':
        return 'Welcome to this page {}'.format(name)

