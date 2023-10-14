from dba.client.client_db import MySQLConnection
from dba.exception import UserNotFoundException
from dba.models._models import Base, User


class DbInteraction:

    def __init__(self, host, port, user, password, dbname, rebuild_db=False):
        self.mysql_connection = MySQLConnection(
            host=host,
            port=port, 
            password=password, 
            user=user,
            dbname=dbname,
            rebuild_db=rebuild_db
        )

        self.engine = self.mysql_connection.connection.engine

        if rebuild_db:
            self.create_table_users()
            self.create_table_musical_compositions()


        def create_table_users(self):
            if not self.engine.dialect.has_table(self.engine, 'users'):
                Base.metadata.tabels['users'].create(self.engine)
            else:
                self.mysql_connection.execute_query('DTOP TABLE IF EXISTS users')
                Base.metadata.tabels['users'].create(self.engine)

        def create_table_musical_compositions(self):
            if not self.engine.dialect.has_table(self.engine, 'musical_compositions'):
                Base.metadata.tabels['musical_compositions'].create(self.engine)
            else:
                self.mysql_connection.execute_query('DTOP TABLE IF EXISTS musical_compositions')
                Base.metadata.tabels['musical_compositions'].create(self.engine)

        def add_userInfo(self, username, email, password):
            user = User(
                username=username,
                password=password, 
                email=email
            )

        def get_user_info(self, username):
            user = self.mysql_connection.session.query(User).filter_by(username=username).first()
            if user:
                self.mysql_connection.session.expire_all()
                return {'username': user.username, 'email': user.email, 'password': user.password}
            else:
                raise UserNotFoundException('User not found')
            