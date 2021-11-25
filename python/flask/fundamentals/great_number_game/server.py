#Created by: Michael Akinosho
#Date created:
from logging import debug, error
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
#key_name = "needs to be binary and unique for each app"
key_name = b'\x93/\x8e*\xf8\xc5\xd4Lp%\x9d\xf5k\xabD\x11'
app.secret_key = key_name
leaderboard_list = []

@app.route('/')
def index():
    my_num = random.randrange(1,101)
    if 'myNum' not in session:
        session['myNum'] = my_num
    
    if 'yourGuesses' not in session:
        session['yourGuesses'] = list()
        session['yourGuesses_count'] = 0
        session['limitGuesses'] = 0

    if 'leaderBoard' not in session:
        session['leaderBoard'] = list()
    print(session['myNum'])
    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def check_guess():
    curGuess = int(request.form['num_guess'])
    if session['limitGuesses'] == 0:
        session['limitGuesses'] = int(request.form['radio_guess'])
    
    if session['myNum'] == curGuess:
        session['results'] = 'correctGuess'
    elif session['myNum'] > curGuess:
        session['results'] = 'tooLow'
    elif session['myNum'] < curGuess:
        session['results'] = 'tooHigh'
        
    myList = session['yourGuesses']
    myList.append(curGuess)
    session['yourGuesses'] = myList
    session['yourGuesses_count'] = len(myList)
    #print(session['myNum'])
    #print(session['yourGuesses'])
    #print(session['results'])
    #print('limit of guesses is:',session['limitGuesses'])
    
    if session['yourGuesses_count'] >= session['limitGuesses'] and session['results'] != 'correctGuess':
        session['results'] = 'youLose'
    
    return redirect('/')

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html",leaders=leaderboard_list)

@app.route('/board_name_submit',methods=['POST'])
def board_name_submit():
    global leaderboard_list
    new_entry = [request.form['user_name'],session['yourGuesses_count']]
    if session['yourGuesses_count'] > 0:
        if len(leaderboard_list) > 0:
            if new_entry[1] >= leaderboard_list[0][1]:
                leaderboard_list.append(new_entry)
            else:
                leaderboard_list.insert(0,new_entry)
        else:
            leaderboard_list.append(new_entry)
    
    session['yourGuesses_count'] = 0
    return redirect('/leaderboard')


@app.route('/reset',methods=['POST'])
def reset():
    close_sessions()
    return redirect('/')
    
@app.route('/destroy_session')
def close_sessions():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! Page Not Available."

if __name__=="__main__":
    app.run(debug=True)