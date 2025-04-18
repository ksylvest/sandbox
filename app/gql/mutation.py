import strawberry

from app.gql.mutations.user_mutations import UserMutations
from app.models.user import User


@strawberry.type
class Mutation:
    @strawberry.field(graphql_type=UserMutations)
    def user(self, id: strawberry.ID):
        user = User.find(id=int(id))
        return UserMutations(user=user)
