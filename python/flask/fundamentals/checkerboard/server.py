#Created by: Michael Akinosho
#Date created: November 16, 2021
from logging import error
from flask import Flask, render_template
app = Flask(__name__)

#Decided to add multiple decorators to accommodate the six variations of calling the page, there could be more but limit 6
@app.route('/')
@app.route('/checkboarder')
@app.route('/checkboarder/<int:nrows>')
@app.route('/checkboarder/<int:nrows>/<int:ncolumns>')
@app.route('/checkboarder/<int:nrows>/<int:ncolumns>/<string:nfirst_color>')
@app.route('/checkboarder/<int:nrows>/<int:ncolumns>/<string:nfirst_color>/<string:nsecond_color>')
def checkboarder(nrows=8,ncolumns=8,nfirst_color='red',nsecond_color='black'):
    return render_template("index.html",rows=nrows,columns=ncolumns,first_color=nfirst_color,second_color=nsecond_color)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! Page Not Available."

if __name__=="__main__":
    app.run(debug=True)