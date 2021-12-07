from logging import debug, error
from flask import Flask, render_template, request, redirect, session# import the class from friend.py
from user import User
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

@app.route('/create_friend',methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form['email']
    }
    
    User.save(data)
    return redirect('/')
            
if __name__ == "__main__":
    app.run(debug=True)