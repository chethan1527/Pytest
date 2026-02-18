class Database:
    """Simulates a basic user database."""
    def __init__(self):
        self.users = {} #In-memory database

    def add_user(self, user_id, name):
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = name

    def get_user(self, user_id):
        return self.users.get(user_id,None)
    
    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
        else:
            raise ValueError("User not found")



