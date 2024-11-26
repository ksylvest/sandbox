import time

from ..config.celery import celery

from ..models.user import User


@celery.task(name="user_greet_task")
def user_greet_task(user_id: int):
    user = User.find(user_id)

    if isinstance(user, ValueError):
        raise user

    time.sleep(2)
    print(f"Howdy {user.name}!")
    time.sleep(2)
