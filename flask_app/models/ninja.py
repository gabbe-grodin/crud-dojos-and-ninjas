from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    DB = 'dojos_and_ninjas'
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.ninjas = []

    @classmethod
    def save_ninja_to_db(cls, data):
        query = """
                INSERT INTO ninjas(first_name, last_name, age)
                VALUES (%(first_name)s, %(last_name)s, %(age)s);
                """