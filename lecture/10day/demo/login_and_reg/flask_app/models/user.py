from flask_app import flash
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
        pass

    @staticmethod
    def validate_user(user:dict):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("you messed up, try again!!!")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("you messed up again, dummy, try again!!!")
            is_valid = False
        
        return is_valid


