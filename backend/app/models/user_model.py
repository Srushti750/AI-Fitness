# Includes user documents

from datetime import datetime

class UserModel:
    def __init__(
            self,
            username: str,
            email: str,
            password: str,
            full_name: str = None,
            age: int = None,
            gender: str = None,
            height: float = None,
            current_weight: float = None,
            fitness_level: str = None
        ):
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.height = height
        self.current_weight = current_weight
        self.fitness_level = fitness_level
        self.created_at = datetime.now()
        self.updated_at = None

    def to_dict(self):
        return {
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "full_name" : self.full_name,
            "age" : self.age,
            "gender" : self.gender,
            "height" : self.height,
            "current_weight" : self.current_weight,
            "fitness_level" : self.fitness_level,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at
        }