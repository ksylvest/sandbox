from typing import List

import strawberry

from ..models.user import User
from .context import Context
from .types.user_type import UserType


@strawberry.type
class Query:
    @strawberry.field
    def greeting(self, name: str) -> str:
        return f"Hello {name}!"

    @strawberry.field(graphql_type=List[UserType])
    def users(self) -> List[User]:
        return User.all()

    @strawberry.field(graphql_type=UserType)
    def user(self, info: strawberry.Info[Context], id: strawberry.ID):
        loader = info.context.user_loader
        return loader.load(int(id))
