from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja



class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []



# ? --------------------------------------
    # READ all dojos, display on frontend
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        
        return dojos
# ? --------------------------------------



# ? --------------------------------------
    # CREATE new dojos, add form data to database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(new_dojo)s, NOW(), NOW());"

        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        dojo = cls(results[0])
        # ! what to do if there is no ninja added to a dojo, how to stop None and the action links from appearing on the frontend

        for row in results:
            data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(data))
            
        print(dojo)
        return dojo
# ? --------------------------------------



# ? --------------------------------------
    # READ one dojos, show on frontend
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;" 
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return cls(result[0]) 
# ? --------------------------------------



# ? --------------------------------------
    # UPDATE dojos with form data
    @classmethod
    def update_one(cls, data):
        query  = "UPDATE dojos SET name = %(new_dojo)s, updated_at = NOW() WHERE id = %(id)s;" 

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # DELETE dojos
    # ! How would you handle deleting a dojo if there were ninjas assigned to it?
    # @classmethod
    # def remove_one(cls, data):
    #     query = "DELETE FROM dojos WHERE id = %(id)s;"

    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# ? --------------------------------------

