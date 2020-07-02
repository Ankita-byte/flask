from flask import *
app=Flask(__name__)


@app.route('/login',methods=['GET'])
def login():
    name=request.args.get('uname')
    pwd=request.args.get('pass')
    if name=='Ankita' and pwd=='India':
        return 'Welcome to this page {}'.format(name)
