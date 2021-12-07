from datetime import datetime
from logging import debug, error
from flask import Flask, render_template, request, redirect, session# import the class from friend.py
from user import User
import datetime
app = Flask(__name__)

@app.route("/users")
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/user/new")
def open_new():
    return render_template("/user/new.html")

@app.route('/add_user',methods=["POST"])
def add_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form['email']
    }
    
    id = User.save(data)
    temp = "/user/show/" + str(id)
    return redirect(temp)

@app.route('/update_user',methods=['POST'])
def update_user():
    data = {
        "id": request.form['id'],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form['email'],
        "updated_at": datetime.datetime.now()
    }
    User.update(data)
    id = data['id']
    temp = "/user/show/" + str(id)
    return redirect(temp)

@app.route('/delete_user/<int:num>')
def delete_user(num):
    data = {
        "id": num
    }
    User.delete(data)
    users = User.get_all()
    return render_template("index.html",all_users = users)

@app.route('/cancel_edit',methods=['POST'])
def cancel_edit():
    
    id = request.form['id']
    temp = "/user/show/" + id
        
    return redirect(temp)
    

@app.route('/user/edit/<int:num>')
def edit_user(num):
    data = {
        "id": num
    }
    
    user = User.get_one(data)
    return render_template("/user/edit.html", one_user = user)

@app.route('/user/show/<int:num>')
def show_user(num):
    data = {
        "id": num
    }
    
    user = User.get_one(data)
    return render_template("/user/show.html", one_user = user)
    
            
if __name__ == "__main__":
    app.run(debug=True)