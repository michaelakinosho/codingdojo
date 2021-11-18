#Created by: Michael Akinosho
#Date created: November 16, 2021
from logging import error
from flask import Flask, render_template
app = Flask(__name__)

users_info = [{'first_name' : 'Michael', 'last_name' : 'Choi'},{'first_name' : 'John', 'last_name' : 'Supsupin'},{'first_name' : 'Mark', 'last_name' : 'Guillen'},{'first_name' : 'KB', 'last_name' : 'Tonel'}]

@app.route('/index.html')
@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html",users=users_info)

@app.route('/list.html')
@app.route('/list')
def list():
    return render_template("list.html",users=users_info)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! Page Not Available."

if __name__=="__main__":
    app.run(debug=True)