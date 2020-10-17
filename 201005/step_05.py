class MyAdminUser:
    def __init__(self):
        self.name = None
        self.age = None
        self.level = 0


user_1 = MyAdminUser()
# print(type(user_1))
# print(dir(user_1))
user_1.name = 'Иван'
user_1.age = 18
user_1.level = 0
print(user_1, user_1.name, user_1.age)

user_1.age = 19
print(user_1, user_1.name, user_1.age)

