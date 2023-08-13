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



    # CREATE
    @classmethod
    def save_ninja_to_db(cls, data):
        query = """
                INSERT INTO ninjas(dojo_id, first_name, last_name, age)
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)
                """
        data = {
                "dojo_id": data['dojo_id'],
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "age": data['age']}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result


    # READ form
    @classmethod
    def get_one_ninja_by_id(cls, ninja_id):
        query = """
                SELECT * FROM ninjas
                WHERE id = %(ninja_id)s
                """
        data = {
                "ninja_id": ninja_id}
        result_list = connectToMySQL(cls.db).query_db(query, data)
        ninja = cls(result_list[0])
        return ninja


    # DELETE
    @classmethod
    def delete_ninja_by_id(cls, ninja_id):
        query = """
                DELETE FROM ninjas
                WHERE id = %(ninja_id)s
                """
        data = {
                "ninja_id": ninja_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result



    # UPDATE
    @classmethod
    def update_ninja_by_id(cls,data):
        query = """
                UPDATE ninjas
                SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, updated_at=NOW(), dojo_id=%(dojo_id)s
                WHERE id = %(id)s
                """
        # data = {"dojo_id": data['dojo_id'],
        #         "first_name": data['first_name'],
        #         "last_name": data['last_name'],
        #         "age": data['age']}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result