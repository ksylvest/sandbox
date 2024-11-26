import strawberry


@strawberry.type
class Mutation:
    @strawberry.mutation
    def restart(self) -> None:
        print(f"Rebooting")
