#Created by: Michael Akinosho
#Date created:
from logging import debug, error
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
key_name = "needs to be binary and unique for each app"
app.secret_key = key_name

@app.route('/')
def index():
    my_num = random.randrange(1,101)
    if 'myNum' not in session:
        session['myNum'] = my_num
    
    if 'yourGuesses' not in session:
        session['yourGuesses'] = list()
    
    nresults = 'start'
    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def check_guess():
    curGuess = int(request.form['num_guess'])
    if session['myNum'] == curGuess:
        session['results'] = 'correctGuess'
    elif session['myNum'] > curGuess:
        session['results'] = 'tooLow'
    elif session['myNum'] < curGuess:
        session['results'] = 'tooHigh'
        
    myList = session['yourGuesses']
    myList.append(curGuess)
    session['yourGuesses'] = myList
    print(session['myNum'])
    print(session['yourGuesses'])
    print(session['results'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_game():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! Page Not Available."

if __name__=="__main__":
    app.run(debug=True)