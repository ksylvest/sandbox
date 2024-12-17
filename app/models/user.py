from peewee import CharField

from app.models.base_model import BaseModel


class User(BaseModel):
    name = CharField()
