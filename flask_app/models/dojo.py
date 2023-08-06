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
        return connectToMySQL(cls.db).query_db(query, data)
    
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
                WHERE dojo.id = %(id)s;
                """
        dojo_from_db = connectToMySQL(cls.db).query_db(query, data)
        return cls(dojo_from_db[0])    
    
    @classmethod
    def delete_dojo_from_db(cls, id):
        query = """
                DELETE FROM dojos
                WHERE id = %(id)s;
                """
        data = {"id": id}
        return connectToMySQL(cls.db).query_db(query, data)
        