from sqlalchemy import create_engine, MetaData

class Database:
    """A class representing a database connection."""
    def __init__(self, model, user, password, url, database):
        """
        Initializes a new database connection.

        Args:
            model (str): The database model to use.
            user (str): The username to connect to the database.
            password (str): The password to connect to the database.
            url (str): The URL of the database server.
            database (str): The name of the database to connect to.
        """
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