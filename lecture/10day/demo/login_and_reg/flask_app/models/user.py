import re	# the regex module
from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'login_and_reg'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        ## prepared statement varibles must match keys in data dict
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return User(result[0])
        
    @staticmethod
    def validate_user(user:dict):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("you messed up, try again!!!", "first_name")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("you messed up again, dummy, try again!!!", "last_name")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least eight characters.", "password")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        if user['password'] != user['password_confirmation']: 
            flash("passwords must match", "password_confirmation")
            is_valid = False

        
        return is_valid


