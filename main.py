from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from gql.schema import schema

app = FastAPI()


@app.get("/up")
def up():
    return {"Status": "OK"}


app.include_router(GraphQLRouter(schema), prefix="/graphql")
