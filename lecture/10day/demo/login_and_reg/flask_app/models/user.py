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

    @classmethod
    def get_by_email(cls, data) -> object or bool:
        pass

    @classmethod
    def get_one_with_things(cls, data:dict)-> list:
        pass

    @staticmethod
    def validate_user(user:dict):
        is_valid = True
        # validations go here
        return is_valid


