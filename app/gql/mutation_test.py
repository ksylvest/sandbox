from unittest.mock import patch

import pytest

from app.gql.context import Context
from app.gql.schema import schema


@pytest.mark.asyncio
async def test_mutation_user_greet():
    gql = """
      mutation UserGreet {
        user(id: 2) {
          greet(greeting: "Hello")
        }
      }
    """

    context = Context()
    with patch("app.tasks.user_greet_task.user_greet_task.delay") as task:
        result = await schema.execute(gql, context_value=context)
        assert result.errors is None
        task.assert_called_once_with(user_id=2, greeting="Hello")
