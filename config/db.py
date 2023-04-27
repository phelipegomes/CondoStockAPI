from sqlalchemy import create_engine, MetaData

class Database:
    def __init__(self, model, user, password, url, database):
        self.model = model
        self.user = user
        self.password = password
        self.url = url
        self.database = database

db = Database("mysql+pymysql", "you_user", "your_password", "127.0.0.1:3306", "your_dbname")

param = f'{db.model}://{db.user}:{db.password}@{db.url}/{db.database}'

engine = create_engine(param)

meta = MetaData()

conn = engine.connect()