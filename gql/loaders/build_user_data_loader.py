from typing import List, Union
from strawberry.dataloader import DataLoader

from models.user import User


async def load_fn(keys: List[int]) -> List[Union[User, ValueError]]:
    return [User.find(key) for key in keys]


def build_user_data_loader() -> DataLoader[int, User]:
    return DataLoader(load_fn=load_fn)
