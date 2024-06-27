from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, email, password, created_at=None):
        self.email = email
        self.password = generate_password_hash(password)
        self.created_at = created_at or datetime.now(timezone.utc)
    
    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        return User(
            email=data['email'],
            password=data['password'],
            created_at=data.get('created_at', datetime.now(timezone.utc))
        )
    
    def check_password(self, password):
        print(password)
        print(self.password)
        print(check_password_hash(self.password, password))
        return check_password_hash(self.password, password)


class Item:
    def __init__(self, name, description, created_at=None, created_by=None):
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now(timezone.utc)
        self.created_by = created_by
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "created_by": self.created_by
        }
