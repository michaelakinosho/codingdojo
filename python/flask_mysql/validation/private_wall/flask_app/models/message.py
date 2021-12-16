# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Message:
    db = 'private_wall'
    def __init__( self , data ):
        self.id = data['id']
        self.message = data['message']
        self.user_sender_id = data['user_sender_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
        
    @classmethod
    def save_message(cls, data ):
        query = "INSERT INTO messages ( message , user_sender_id ) VALUES ( %(message)s , %(user_sender_id)s );"
        # Message id returned after message is saved
        message_id = connectToMySQL(cls.db).query_db( query, data )
        
        sub_data = {'message_id': message_id }
        
        for i in data['recipient']:
            print(i)
            sub_data['user_recipient_id'] = i
            query = "INSERT INTO messages_to_users ( message_id, user_recipient_id ) VALUE (%(message_id)s, %(user_recipient_id)s );"
            connectToMySQL(cls.db).query_db( query, sub_data )
        
        # data is a dictionary that will be passed into the save method from server.py
        
        query = "SELECT * FROM view_messages_from_to WHERE sender_id = %(user_sender_id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE messages SET message = %(message)s, updated_at = %(updated_at)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    """
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(mydb).query_db(query, data)
    """
    