from abc import ABC, abstractmethod
from enum import Enum


class Permissions(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_permissions(self):
        pass
    """Observer"""
    def update(self, message):
        print(f"Notification for {self.name}: {message}")


class Student(User):
    def get_permissions(self):
        return Permissions.low.name


class Teacher(User):
    def get_permissions(self):
        return Permissions.medium.name


class Librarian(User):
    def get_permissions(self):
        return Permissions.high.name


class UserFactory:
    @staticmethod
    def create_user(user_type, name):
        if user_type == "Student":
            return Student(name)
        elif user_type == "Teacher":
            return Teacher(name)
        elif user_type == "Librarian":
            return Librarian(name)
        else:
            raise ValueError(f"Unknown user type: {user_type}")
