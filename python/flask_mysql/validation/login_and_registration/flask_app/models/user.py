# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mydb = 'login_and_registration'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db( query, data)
        one_user = []
        for user in results:
            one_user.append(cls(user))
        return one_user
        
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, password) VALUES ( %(fname)s , %(lname)s , %(email)s, %(password)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(mydb).query_db( query, data )
        
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(mydb).query_db( query, data)
        
        if len(results) < 1:
            return False
        
        return cls(results[0])
    
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!",'email')
            is_valid = False
        
        if len(user['fname']) < 1 or user['fname'].isspace():
            flash("First name is blank")
            is_valid = False
        
        if len(user['lname']) < 1 or user['lname'].isspace():
            flash("Last name is blank")
            is_valid = False
        
        if len(user['password']) < 1 or user['password'].isspace():
            flash("Password is blank")
            is_valid = False
        
        caps_in_pw = re.findall("[A-Z]",user['password'])
        nums_in_pw = re.findall("[0-9]",user['password'])
        if len(caps_in_pw) < 1 or  len(nums_in_pw) < 1:
            flash("Password requires at least one capital letter and at least one number")
            is_valid = False
            
        if len(user['confirmpassword']) < 1 or user['confirmpassword'].isspace():
            flash("Confirm Password is blank")
            is_valid = False
        
        if user['password'] != user['confirmpassword']:
            flash("Passwords do not match")
        
        return is_valid
    
    """
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(mydb).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
        
    @classmethod
    def update(cls, data ):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = %(updated_at)s WHERE id = %(id)s;"
        return connectToMySQL(mydb).query_db( query, data )
    
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(mydb).query_db(query, data)
    """
    