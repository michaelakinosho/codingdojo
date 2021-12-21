from flask import Flask, render_template, request, redirect, session, flash# import the class from friend.py
from flask_app.models.message import Message
from flask_app.models.user import User
from flask_app import app
from werkzeug.datastructures import ImmutableMultiDict
import socket


@app.route('/send_message',methods=['POST'])
def send_message():
    
    if int(request.form['sender_id']) != int(session['id']):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        log_data = {
            'hostname': hostname,
            'ip_address': ip_address,
            'id':session['id']
        }
        
        results = User.get_by_id(log_data)
        session.clear()
        
        print("Your hostname:",log_data['hostname'])
        print("Your IP Address is:",log_data['ip_address'])
        return render_template("final_warning.html",log_info=log_data,user_info=results)
    # end of code block identifying and logging out the hacker
    
    request_form = ImmutableMultiDict(request.form)
    message = request_form['message']
    message_recipients = request_form.getlist('message_recipients')
    message_recipients = list(map(int, message_recipients))
    
    if not validate_message( message_recipients, message):
        session['message'] = message
        return redirect("/user/dashboard")

    data = {
        'message':request.form['message'],
        'user_sender_id':request.form['sender_id'],
        'recipient': message_recipients
    }
    Message.save_message(data)    
    
    return redirect("/user/dashboard")

def validate_message (message_recipients, message):
    is_valid = True
    
    if len(message) < 1 or message.isspace():
        flash("Message is blank","send_message")
        is_valid = False
    if len(message_recipients)<1:
        flash("No recipients selected","send_message")
        is_valid = False
    
    return is_valid