from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def save_ninja_to_db(cls, data):
        query = """
                INSERT INTO ninjas(dojo_id, first_name, last_name, age)
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s) ;
                """
        data = {
            "dojo_id": data['dojo_id'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "age": data['age']}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result