from typing import Union


class User:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def all(cls) -> list["User"]:
        return [
            User(id=1, name="John"),
            User(id=2, name="Paul"),
            User(id=3, name="George"),
            User(id=4, name="Ringo"),
        ]

    @classmethod
    def find(cls, id: int) -> "User":
        for user in cls.all():
            if user.id == id:
                return user
        raise ValueError(f"unknown id={id}")

    @classmethod
    def filter(cls, ids: list[int]) -> list["User"]:
        users = [cls.find(id) for id in ids]
        return [user for user in users if not isinstance(user, ValueError)]
