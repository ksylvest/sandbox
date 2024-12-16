import pytest

from app.models.user import User


@pytest.fixture
def test_user():
    user = User.create(name="Ringo")
    yield user
    user.delete_instance()


def test_user_id():
    assert test_user.id is not None


def test_user_name():
    assert test_user.name == "Ringo"
