from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

products = Table('products', meta, 
    Column('id', Integer, primary_key=True), 
    Column('name', String(255)), 
    Column('description', String(255)),
    Column('price', Float),
    Column('quantity', Integer),
    Column('color', String(255)),
    Column('serial', String(255)))

meta.create_all(engine)
