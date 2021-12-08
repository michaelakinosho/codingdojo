from flask import Flask, render_template, request, redirect, session# import the class from friend.py
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route("/dojos")
@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)


@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    data = {
        "name" : request.form["name"]
    }
    
    if data['name'].isspace() or len(data['name']) < 1:
        return redirect("/dojos")
    
    Dojo.save(data)
    return redirect("/dojos")

@app.route('/dojo/show/<int:num>')
def show_dojo_ninjas(num):
    data = {
        "id" : int(num)
    }
    dojo = Dojo.get_dojos_with_ninjas(data)
    return render_template("/dojo/show.html", one_dojo = dojo)