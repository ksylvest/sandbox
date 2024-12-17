from invoke.context import Context
from invoke.tasks import task
from strawberry.printer import print_schema

from app.gql.schema import schema
from app.models.user import User
from config.database import database


@task
def codegen(_context: Context):
    """
    Print the GraphQL schema to the console.
    """
    print(print_schema(schema))


@task
def setup(_context: Context):
    """
    Setup the database schema.
    """

    database.create_tables([User])


@task
def seed(_context: Context):
    """
    Populate the database data.
    """
    names = ["John", "Paul", "George", "Ringo"]
    for name in names:
        if User.select().where(User.name == name).exists():
            continue
        user = User(name=name)
        user.save()
