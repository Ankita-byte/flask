from flask import Flask
app=Flask(__name__)

@app.route('/project/')
def project():
    return 'Project'
    
 @app.route(/about)
 def about():
     return 'About'
