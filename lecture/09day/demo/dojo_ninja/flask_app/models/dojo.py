# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database
from pprint import pprint
from flask_app.models.ninja import Ninja

DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( Dojo(dojo) )
        return dojos
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        dojo = result[0]
        return Dojo(dojo)

    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id  WHERE dojos.id = %(id)s;"
        # what does this do
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        ## makeing a dojo instance
        dojo = Dojo(results[0])
        for result in results:
            ninja_data = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'age': result['age'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
     
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
