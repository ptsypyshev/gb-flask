import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
    
class User():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

class MemDB():
    def __init__(self):        
        self.user_id_pk = 0
        self.users = {}
    
    def create(self, user: User) -> int:
        if self.read_by_id(user.id):
            raise KeyError("user with the same id exists")   
        user.id = self.user_id_pk
        self.users[user.id] = user      
        self.user_id_pk += 1
        return user.id
    
    def read_by_id(self, user_id) -> User:
        return self.users.get(user_id, None)
    
    def read_all(self):
        return list(self.users.values())
    
    def update(self, user):
        if not self.read_by_id(user.id):
            logger.warning("user with the same id doesn't exist and will be created")
        self.users[user.id] = user
    
    def delete_by_id(self, user_id):
        if not self.read_by_id(user_id):
            raise KeyError("user with the same id doesn't exist and cannot be removed") 
        self.users.pop(user_id)

    def init(self):
        for i in range(10):
            try:
                self.create(User(i, f"name{i}", f"name{i}@domain.com", "pwd{1}"))
            except KeyError as e:
                logger.error(f'cannot create user: {e}')
