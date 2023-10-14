from peewee import *

def DBORMConnect():

    # Подключение к базе MySQL 
    connORM = MySQLDatabase(database = 'spaces', host='127.0.0.1', user='root', password='root') 

    return connORM