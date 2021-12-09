from flask import Flask, render_template, request, redirect, session, flash# import the class from friend.py
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
import datetime

bcrypt = Bcrypt(app)

@app.route("/")
def index():

    return render_template("index.html")

@app.route('/register/user',methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect("/")
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form['email'],
        "password": pw_hash
    }
    
    user_id = User.save(data)
    session['id'] = user_id
    
    return redirect("/user/dashboard")

@app.route('/login/user',methods=['POST'])
def login():
    data = { "email": request.form['email']  }
    user = User.get_by_email(data)
    
    if not user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect("/")

    session['id'] = user.id
    
    return redirect("/user/dashboard")

@app.route('/user/dashboard')
def show_user():
    print(session['id'])
    data = {
        "id": session['id']
    }
    user_info = User.get_by_id(data)
    return render_template("/user/dashboard.html", one_user = user_info)

@app.route('/logout', methods= ['POST'])
def close_sessions():
    session.clear()
    return redirect('/')
