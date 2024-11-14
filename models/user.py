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
    def find(cls, id: int) -> Union["User", ValueError]:
        for user in cls.all():
            if user.id == id:
                return user
        return ValueError(f"unknown id={id}")
