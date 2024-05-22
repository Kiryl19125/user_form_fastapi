from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)

    def __init__(self, name: str, surname: str, email: str, phone_number: str):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.email}, {self.phone_number}"
