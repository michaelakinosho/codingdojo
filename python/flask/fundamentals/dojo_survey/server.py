#Created by: Michael Akinosho
#Date created:
from logging import debug, error
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
key_name = "needs to be binary and unique for each app"
app.secret_key = key_name

@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post_survey',methods=['POST'])
def something_to_post():
    #print(request.form['user_name'])
    interested_topics = ['Data Science','Software Development','Robotics','User Experience']
    session_data = request.form
    for k, v in session_data.items():
        session[k] = v
        print("key:",k,"value:",v)
        if v in interested_topics:
            if 'interested_topics' not in session:
                session['interested_topics'] = []
                session['interested_topics'].append(v)
            else:
                session['interested_topics'].append(v)
    
    return render_template('user_info.html')

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