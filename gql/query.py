from typing import List

import strawberry

from models.user import User

from .types.user_type import UserType


@strawberry.type
class Query:
    @strawberry.field
    def greeting(self, name: str) -> str:
        return f"Hello {name}!"

    @strawberry.field
    def users(self) -> List[UserType]:
        return User.all()

    @strawberry.field
    def user(self, info: strawberry.Info, id: int) -> UserType:
        loader = info.context.user_loader
        return loader.load(id)
