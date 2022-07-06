class User:

    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        User.users.append(self)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)


    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        
    def spend_points(self, amount):
        self.gold_card_points -= amount


user1 = User('Tyler', 'Maxwell', 'tmax@email.com', 39)

print(dir(user1))
print(user1.first_name)

