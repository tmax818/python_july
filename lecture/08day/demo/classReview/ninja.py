ninjas = [
    {'first_name': 'Tyler', 'age': 39},
    {'first_name': 'Ed', 'age': 32},
    {'first_name': 'Tim', 'age': 34},
]


class Ninja:

    ninjas = []

    def __init__(self, data) -> None:
        self.first_name = data['first_name']
        self.age = data['age']

    def write_code(self):
        print("I am learning Python!!!")

    @classmethod
    def create_ninjas(cls, ninja_list):
        for ninja in ninja_list:
            Ninja.ninjas.append(cls(ninja))
