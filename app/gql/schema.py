from strawberry import Schema

from .query import Query
from .mutation import Mutation

schema = Schema(mutation=Mutation, query=Query)
