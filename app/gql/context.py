from strawberry.dataloader import DataLoader
from strawberry.fastapi import BaseContext

from ..models.user import User
from .loaders.build_user_data_loader import build_user_data_loader


class Context(BaseContext):
    user_loader: DataLoader[int, User]

    def __init__(self):
        self.user_loader = build_user_data_loader()


async def context():
    return Context()
