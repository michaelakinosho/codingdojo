#Created by: Michael Akinosho
#Date created: November 15, 2021
from logging import error
from flask import Flask
app = Flask(__name__)
@app.route('/')
def understanding_routing():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:firstname>')
def user(firstname):
    return "Hi " + firstname + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    return (word +'\n') * num

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)