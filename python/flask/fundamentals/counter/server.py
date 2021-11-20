#Created by: Michael Akinosho
#Date created: November 19, 2021
from logging import debug, error
from flask import Flask, render_template, request, redirect, session
from werkzeug.exceptions import RequestEntityTooLarge
import base64

app = Flask(__name__)
key_name = b'\xb76\xf6O\x80\x04\xdc\x8f\xc0\xda\x13\xebVK\xf7\x91'
app.secret_key = key_name

@app.route('/')
def index():
    if 'username' in session:
        if 'user_visits' in session:
            session['user_visits'] += 1
        else:
            session['user_visits'] = 1
        
        if 'actual_visits' in session:
            session['actual_visits'] += 0
    
    for k,v in request.cookies.items():
        print(v)
    myList = v.split(".")
    print(myList)
    for x in myList:
        myStr = ("'" + x+'===' + "'")
        print(base64.urlsafe_b64decode(myStr))
    
    for k,v in session.items():
        print(k,v)
    
    return render_template("index.html")

@app.route('/reset', methods=['POST'])
def reset():
    close_sessions()
    return redirect('/')

@app.route('/user',methods=['POST'])
def update_user():
    
    if 'username' not in session:
        session['username'] = request.form['username']
        session['actual_visits'] = 1
        session['user_visits'] = 0
    else:
        if session['username'] == request.form['username']:
            session['actual_visits'] += 1
            session['user_visits'] += 0
        else:
            session['username'] = request.form['username']
            session['actual_visits'] = 1
            session['user_visits'] = 0
        
    return redirect('/')

@app.route('/process', methods=['POST'])
def count_two():
    session['user_visits'] += (1)
    #session['actual_visits'] += -1 
    return redirect('/')

@app.route('/user_counts', methods=['POST'])
def increase_counts():
    num = int(request.form['count'])
    session['user_visits'] += (num - 1 )
        
    return redirect('/')

@app.route('/success')
def show_counter():
    return render_template("index.html")

@app.route('/destroy_session')
def close_sessions():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)