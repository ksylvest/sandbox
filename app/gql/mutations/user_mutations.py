import strawberry

from ...models.user import User
from ...tasks.user_greet_task import user_greet_task


@strawberry.type
class UserMutations:
    user: strawberry.Private[User]

    def __init__(self, user: User):
        self.user = user

    @strawberry.mutation
    def greet(self, greeting: str) -> None:
        user_greet_task.delay(self.user.id, greeting)
