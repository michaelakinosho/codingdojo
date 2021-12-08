#import the functioon that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # class methods to query our database
    @classmethod
    def save( cls, data):
        query = "SELECT id FROM dojos WHERE name = %(name)s LIMIT 1;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)
        print(results)
        data['dojo_id'] = results[0]['id']
        
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data), results[0]['id']