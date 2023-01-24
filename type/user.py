import strawberry
import typing
from models.index import users
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
    def update_user(self, info, id: int, name: str, email: str, password: str) -> bool:
        query = users.update().where(users.c.id == id).values(name=name, email=email, password=password)
        result = conn.execute(query)
        return str(result.rowcount)+ " row(s) updated"
    @strawberry.mutation
    def delete_user(self, info, id: int) -> bool:
        query = users.delete().where(users.c.id == id)
        result = conn.execute(query)
        return result.rowcount > 0