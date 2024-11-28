from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from strawberry.fastapi import GraphQLRouter

from app.gql.context import context
from app.gql.schema import schema
from app.tasks.user_greet_task import user_greet_task

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse("/graphql")


@app.get("/up")
def up():
    return {"Status": "OK"}


app.include_router(GraphQLRouter(schema, context_getter=context), prefix="/graphql")
