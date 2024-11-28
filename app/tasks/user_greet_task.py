import time

from ..config.celery import celery
from ..models.user import User


@celery.task(name="user_greet_task")
def user_greet_task(user_id: int, greeting: str) -> None:
    user = User.find(user_id)

    time.sleep(2)
    print(f"{greeting} {user.name}!")
    time.sleep(2)
