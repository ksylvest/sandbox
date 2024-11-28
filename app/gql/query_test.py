import pytest

from app.gql.context import Context
from app.gql.schema import schema


@pytest.mark.asyncio
async def test_query_users():
    gql = """
      query Users {
        users {
          id
          name
        }
      }
    """

    context = Context()
    result = await schema.execute(gql, context_value=context)
    assert result.errors is None
    assert result.data is not None
    assert result.data["users"] is not None


@pytest.mark.asyncio
async def test_query_user():
    gql = """
      query User {
        user(id: 2) {
          id
          name
        }
      }
    """

    context = Context()
    result = await schema.execute(gql, context_value=context)
    assert result.errors is None
    assert result.data is not None
    assert result.data["user"] is not None
