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

    @classmethod
    def save_dojo_to_db(cls, data):
        query = """
                INSERT INTO dojos(dojo_name, created_at, updated_at)
                VALUES(%(dojo_name)s, NOW(), NOW());
                """
        dojo_id = connectToMySQL(cls.db).query_db(query, data)
        return dojo_id
    
    @classmethod
    def get_all_dojos_in_db(cls):
        query = """
                SELECT *
                FROM dojos;
                """
        
        result = connectToMySQL(cls.db).query_db(query)

        dojos = []
        
        for row in result:
            dojos.append(Dojo( row ))
        return dojos
    
    @classmethod
    def get_one_dojo_in_db(cls, data):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas
                ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s;
                """
        data = {
            "ninja_id": request.form['ninja_id'],
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "age": request.form['age']
        }
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        
        if results:
            dojo = cls(results[0])
        
            for result in results:

                dojo.ninjas.append(
                
                    cls({
                        "id": result['ninjas.id'],
                        "first_name": result['ninjas.first_name'],
                        "last_name": result['ninjas.last_name']
                    })
                )
            return dojo
        
        return None   
    
    @classmethod
    def delete_dojo_from_db(cls, id):
        query = """
                DELETE FROM dojos
                WHERE id = %(id)s;
                """
        data = {"id": id}
        return connectToMySQL(cls.db).query_db(query, data)
        