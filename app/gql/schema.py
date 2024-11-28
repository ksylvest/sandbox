from strawberry import Schema

from app.gql.mutation import Mutation
from app.gql.query import Query

schema = Schema(mutation=Mutation, query=Query)
