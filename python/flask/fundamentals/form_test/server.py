#Created by: Michael Akinosho
#Date created: November 17, 2021
from logging import debug, error
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = b'\xba\x15R\x90\xc7?\x1aj9\xa2\xcb&\xff\xc5\xfa\xa5'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    #Here we add two properties to session to store the name and email
    session['det'] = request.form
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    print(session['det']['name'])
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__=="__main__":
    app.run(debug=True)