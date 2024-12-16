from invoke.context import Context
from invoke.tasks import task
from strawberry.printer import print_schema

from app.gql.schema import schema


@task
def codegen(_context: Context):
    ###
    # Print the schema to the console.
    ###
    print(print_schema(schema))
