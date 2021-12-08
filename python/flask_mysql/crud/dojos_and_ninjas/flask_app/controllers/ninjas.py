from flask import Flask, render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/add_ninja', methods=["POST"])
def add_ninja():
    print(request.form["dojo_name"])
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "name" : request.form["dojo_name"]
    }
    print(data)
    ninja_id, dojo_id = Ninja.save(data)
    temp = "/dojo/show/" + str(dojo_id)
    return redirect(temp)

@app.route('/ninja/new')
def ninja_info():
    dojos = Dojo.get_all()
    return render_template("/ninja/new.html", all_dojos = dojos)