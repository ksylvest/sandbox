import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def greeting(self, name: str) -> str:
        return f"Hello {name}!"
