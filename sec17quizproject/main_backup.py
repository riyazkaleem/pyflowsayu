#class declaration
class User:
    
    #constructor
    def __init__(self, id, name):
        print('a new user being created by constructor')
        self.id = id
        self.name = name

        #default parameters which are updated later
        self.salary = 1500

    #method to increase salary
    def increase_salary(self, delta):
        self.salary += delta

#objects creation
user1 = User(1, 'riyaz')
user2 = User(2, 'kaleem')

#printing to console
print(f'user1 details: user1 id: {user1.id}, user1 name: {user1.name}')
print(f'user2 details: user2 id: {user2.id}, user2 name: {user2.name}')

print(f'user1 salary before update: {user1.salary}')

user1.increase_salary(100)
print(f'user1 salary after update: {user1.salary}')