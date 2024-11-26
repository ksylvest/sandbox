import strawberry


@strawberry.type(name="User")
class UserType:
    id: strawberry.ID
    name: str
