# Импортируем библиотеку, соответствующую типу нашей базы данных 
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
from peewee import *
from dba.connector.dbcon import DBConnect

conn = None

def setConnectorDB(conndb):
    conn = conndb

# Определяем базувую модельль от которой будем наследовать все остальные
class BaseModel(Model):
    class Meta:
        database = conn

# Определяем модель Spaces
class Spaces(BaseModel):
    space_id = AutoField(column_name = 'space_id') #, primary_key = True, null = False, index = True
    space_nam = TextField(column_name = 'space_nam')
    space_descript = TextField(column_name = 'space_descript')
    db_nam = TextField(column_name = 'db_nam')
    block = SmallIntegerField(column_name = 'block')

    class Meta:
        table_name = 'spaces' #можно не задавать, тогода именем таблицы будет счистаться название класса   
