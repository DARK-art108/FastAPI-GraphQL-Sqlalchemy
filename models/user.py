from conn.db import meta
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

users = Table('user', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('age', Integer),
    Column('email', String(100)),
    Column('password', String(100))
)