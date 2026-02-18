# def get_weather(temp):
#     if temp > 25:
#         return "Hot"
#     elif temp > 15:
#         return "Warm"
#     else:
#         return "Cold"

# def add(a,b):
#     return a + b

# def divide(a,b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b

class UserManager:
    def __init__(self):
        self.users = {}
        
    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True
    
    def get_user(self,username):
        return self.users.get(username)