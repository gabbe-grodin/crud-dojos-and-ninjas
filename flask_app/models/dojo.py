from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    # Create
    @classmethod
    def create_dojo(cls, data):
        query = """
                INSERT INTO dojos(dojo_name)
                VALUES(%(dojo_name)s)
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result
    

    # Read
    @classmethod
    def get_all_dojos(cls):
        query = """
                SELECT *
                FROM dojos
                """
        result = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for row in result:
            dojos.append(cls( row ))
        return dojos
    
    # GET ONE #! needs fixing: if no ninja yet added to dojo, do not render 'none' in ninja list with update and delete buttons, as they won't work. Do I do this with a conditional before appending to ninja list?
    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas
                ON dojo_id = dojos.id
                WHERE dojos.id = %(dojo_id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        this_dojo = cls(results[0]) # This creates an instance of a dojo

        for row in results:
            if row['ninjas.id']: # This conditional prevents dojos with code any ninjas from creating an instance of a ninja and printing 'None'
                ninja_data = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at'],
                    "dojo_id": row['dojo_id']} 
                this_dojo.ninjas.append(ninja.Ninja(ninja_data))
        return this_dojo
        


    # DELETE
    @classmethod
    def delete_dojo_from_db(cls, id):
        query = """
                DELETE FROM dojos
                WHERE id = %(id)s
                """
        data = {"id": id}
        return connectToMySQL(cls.db).query_db(query, data)