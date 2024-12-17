import os
from urllib.parse import urlparse

from peewee import PostgresqlDatabase

DATABASE_URL = urlparse(
    os.getenv("DATABASE_URL", "postgres://postgres:postgres@localhost:5432/sandbox")
)

POSTGRES_DB = DATABASE_URL.path[1:]  # e.g. 'sandbox'
POSTGRES_USER = DATABASE_URL.username
POSTGRES_PASSWORD = DATABASE_URL.password
POSTGRES_HOST = DATABASE_URL.hostname
POSTGRES_PORT = DATABASE_URL.port

database = PostgresqlDatabase(
    POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    schema="psycopg3",
)
