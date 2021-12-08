#import the functioon that will return an instance of a connection
from flask.templating import render_template
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

# model the class after the friend table from our database
class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # We create a list so that we can add in all the ninjas that are associated with a dojo
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        #making sure to call the connectToMySQL function with the targetted schema
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        #creating an empty list to append instances of dojos
        dojos = []
        #Iterating through the db results and creating instances of dojos with cls
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_dojos_with_ninjas( cls, data ):
        query = "SELECT * FROM dojos JOIN  ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['first_name'],
                "last_name" : row_from_db['last_name'],
                "age" : row_from_db['age'],
                "created_at" : row_from_db['ninjas.created_at'],
                "updated_at" : row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        
        return dojo 