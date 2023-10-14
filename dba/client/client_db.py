import sqlalchemy
from sqlalchemy.orm import sessionmaker

class MySQLConnection:

    def __init__(self, host, port, user, password, dbname, rebuild_db=False):
        self.user = user
        self.password = password
        self.dbname = dbname

        self.host = host
        self.port = port

        self.rebuild_db = rebuild_db
        self.connection = self.connect()

        session= sessionmaker(
            autocommit=True,
            bind=self.connection.engine,
            autoflush=True,
            enable_backed_queries=False,
            expire_on_commit=True
        )

        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname if db_created else ""}'
        )
        return engine.connect()

    def connect(self):
        connection = self.get_connection()
        if self.rebuild_db:
            connection.execute(f'DROP DATABASE IF EXISTS {self.dbname}')
            connection.execute(f'CREATE DATABASE {self.dbname}')

        return self.get_connection(db_created=True)
    
    def execute_query(self, query):
        res = self.connection.execute(query)
        return res
