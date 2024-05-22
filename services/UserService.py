from repositories.UserRepository import UserRepository
from models.User import User
from typing import List
import re


def _validate_user(user: User):
    _validate_name(user.name)
    _validate_surname(user.surname)
    _validate_email(user.email)
    # _validate_phone_number(user.phone_number)


def _validate_name(name: str):
    if not name.isalpha():
        raise ValueError("Name must contain only alphabetic characters.")


def _validate_surname(surname: str):
    if not surname.isalpha():
        raise ValueError("Surname must contain only alphabetic characters.")


def _validate_email(email: str):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")


def _validate_phone_number(phone_number: str):
    pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    if not pattern.match(phone_number):
        raise ValueError("Phone number must contain only digits.")


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def add_user(self, user: User) -> None:
        _validate_user(user)
        self.__user_repository.add_user(user)

    def get_all_users(self) -> List[User]:
        return self.__user_repository.get_all_users()
