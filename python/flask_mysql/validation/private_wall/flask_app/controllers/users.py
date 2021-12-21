from flask import Flask, render_template, request, redirect, session, flash# import the class from friend.py
from flask_app.models.user import User
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
from werkzeug.datastructures import ImmutableMultiDict

# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)

@app.route("/")
def index():

    return render_template("index.html")

@app.route('/register/user',methods=["POST"])
def register():
    data = { "email" : request.form['email']}
    user_with_email = User.get_by_email(data)
    if user_with_email:
        flash("Email is invalid or unable", "register")
        return render_template("index.html")

    if not validate_user(request.form):
        #form_info = request.form
        return render_template("index.html")
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form['email'],
        "password": pw_hash
    }
    
    session['id'] = User.save(data)
    
    return redirect("/user/dashboard")

@app.route('/login/user',methods=['POST'])
def login():
    data = { "email": request.form['email']  }
    user = User.get_by_email(data)

    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")

    session['id'] = user.id
    session['message'] = ""

    return redirect("/user/dashboard")

@app.route('/user/dashboard')
def show_user():
    print(session['id'])
    data = {
        "id": session['id']
    }
    user_info = User.get_by_id(data)
    all_users = User.get_all()
    msg_sent = User.messages_sent(data)
    msg_received = User.messages_received(data)
    #print(msg_sent)
    return render_template("/user/dashboard.html", one_user = user_info, all_users = all_users,sent_msg = msg_sent, recd_msg = msg_received)

@app.route('/logout')
def close_sessions():
    session.clear()
    return render_template("index.html")

def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if len(user['fname']) < 1 or user['fname'].isspace():
            flash("First name is blank","register")
            is_valid = False
        
        if len(user['lname']) < 1 or user['lname'].isspace():
            flash("Last name is blank","register")
            is_valid = False
        
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!","register")
            is_valid = False
            
        if len(user['password']) < 8 or user['password'].isspace():
            flash("Password must be at least 8 characters","register")
            is_valid = False
        
        caps_in_pw = re.findall("[A-Z]",user['password'])
        nums_in_pw = re.findall("[0-9]",user['password'])
        if len(caps_in_pw) < 0 or len(nums_in_pw) < 0:
            flash("Password requires at least one capital letter and at least one number","register")
            is_valid = False
            
        if len(user['confirmpassword']) < 1 or user['confirmpassword'].isspace():
            flash("Confirm Password is blank","register")
            is_valid = False
        
        if user['password'] != user['confirmpassword']:
            flash("Passwords do not match","register")
            is_valid = False
        
        return is_valid
