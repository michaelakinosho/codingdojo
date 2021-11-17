#Created by: Michael Akinosho
#Date created: November 15, 2021
from logging import error
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",times=0)

@app.route('/play')
def play():
    return render_template("index.html",times=3)

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("index.html",times=num)

@app.route('/play/<int:num>/<string:myColor>')
def play_num_color(num,myColor):
    return render_template("index.html",times=num,color=myColor)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! Page Not Available."

if __name__=="__main__":
    app.run(debug=True)