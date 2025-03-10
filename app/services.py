from app.gyphi import GyphiClient
from uuid import uuid4
from typing import Iterator

from app.repositories import UserRepository
from app.models import User



class SearchService:

    def __init__(self, gyphi_client: 'GyphiClient'):
        self.client = gyphi_client

    def run(self):
        print('Running main SearchService')
        print(self.client.run())
        return [1,2,3]


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self) -> User:
        uid = uuid4()
        return self._repository.add(email=f"{uid}@email.com", password="pwd")

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)