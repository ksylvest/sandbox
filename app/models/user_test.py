import pytest
from .user import User


def test_all():
    users = User.all()
    assert len(users) > 0


def test_find_matching_id():
    user = User.find(3)
    assert isinstance(user, User)


def test_find_missing_id():
    user = User.find(0)
    assert isinstance(user, ValueError)


def test_filter():
    users = User.filter(ids=[1, 2, 3])
    assert len(users) == 3
