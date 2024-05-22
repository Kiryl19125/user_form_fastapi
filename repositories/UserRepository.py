from sqlalchemy.orm import Session
from typing import List
from models.User import User


class UserRepository:

    def __init__(self, engine, base):
        self.engine = engine
        self.base = base
        self.base.metadata.create_all(engine)

    def add_user(self, user: User) -> None:
        with Session(self.engine) as session:
            session.add(user)
            session.commit()

    def get_all_users(self) -> List[User]:
        result: List[User] = []
        with Session(self.engine) as session:
            users = session.query(User).all()
            for user in users:
                result.append(User(user.name, user.surname, user.email, user.phone_number))
        return result
