import strawberry
import typing
from models.user import users
from conn.db import conn


@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, id:int) -> User:
        return conn.execute(users.select().where(users.c.id == id)).fetchone()
    @strawberry.field
    def users(self, info) -> typing.List[User]:
        return conn.execute(users.select()).fetchall()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str, password: str) -> bool:
        query = users.insert().values(name=name, email=email, password=password)
        result = conn.execute(query)
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    #def update_user(self, info, id: int, name: str, email: str, password: str) -> bool: