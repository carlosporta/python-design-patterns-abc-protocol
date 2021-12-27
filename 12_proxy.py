from abc import ABC, abstractmethod
from time import sleep
from random import choices, randint
from string import ascii_lowercase


def random_name() -> str:
    size = randint(4, 8)
    return "".join(choices(ascii_lowercase, k=size))


class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.user_id = user_id
        self.name = name

    def __str__(self) -> str:
        return f"User(user_id={self.user_id}, name={self.name})"


class IUserRepository(ABC):
    @property
    @abstractmethod
    def users(self) -> dict[int, User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError


class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self._users = {i: User(i, random_name()) for i in range(10)}

    @property
    def users(self) -> dict[int, User]:
        return self._users

    def get_by_id(self, user_id: int) -> User:
        # heavy operation
        sleep(2)
        return self.users[user_id]


class UserRepositoryCache(IUserRepository):
    def __init__(self) -> None:
        self._repo = UserRepository()
        self._cache: dict[int, User] = {}

    @property
    def users(self) -> dict[int, User]:
        return self._repo.users

    def get_by_id(self, user_id: int) -> User:
        cached_user = self._cache.get(user_id)
        if not cached_user:
            cached_user = self._repo.get_by_id(user_id)
            self._cache[user_id] = cached_user
        return cached_user


if __name__ == "__main__":
    cache = UserRepositoryCache()

    print("Takes two seconds")
    print(cache.get_by_id(1))

    print("Cached value")
    print(cache.get_by_id(1))
