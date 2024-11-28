from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from .gql.context import context
from .gql.schema import schema
from .tasks.user_greet_task import user_greet_task

app = FastAPI()


@app.get("/up")
def up():
    return {"Status": "OK"}


@app.post("/users/{user_id}/greet")
def user_greet(user_id: int):
    user_greet_task.delay(user_id=user_id)
    return {"Status": "OK"}


app.include_router(GraphQLRouter(schema, context_getter=context), prefix="/graphql")
