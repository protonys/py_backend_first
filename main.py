from flask import Flask
from flask_restful import Api
import API.endpoints as endpoints
import API.config as cfg
from dba.connector.dbcon import DBConnect
from dba.connector.dbormcon import DBORMConnect
from dba.interaction.interaction import DbInteraction
from mysql.connector import connect, Error
from peewee import *

 #from dba.models.models import Space, setConnectorDB

app = Flask(__name__)
api = Api(app)

endpoints.addEndPoints(api)

if __name__ == '__main__':

    # Подключение к базе MySQL и получаем курсор
    conn = DBConnect()

    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()  

    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    cursor.execute("SELECT * FROM spaces")

    # setConnectorDB(conn) # Передача ссылки на подключение к БД в глобальную переменную модуля models    

    connORM = DBORMConnect()

    # Определяем базувую модельль от которой будем наследовать все остальные
    class BaseModel(Model):
        class Meta:
            database = connORM

    # Определяем модель для таблицы Spaces
    class Spaces(BaseModel):
        space_id = AutoField(column_name = 'space_id') #, primary_key = True, null = False, index = True
        space_nam = TextField(column_name = 'space_nam')
        space_descript = TextField(column_name = 'space_descript')
        db_nam = TextField(column_name = 'db_nam')
        block = SmallIntegerField(column_name = 'block')

        class Meta:
            table_name = 'spaces' #можно не задавать, тогода именем таблицы будет счистаться название класса   

    query = Spaces.select()

    #print(query)

    spaces_selected = query.dicts().execute()
    print(spaces_selected)  # <peewee.ModelDictCursorWrapper object at 0x7f6fdd9bdda0>    

    for space in spaces_selected:
        print('space: ', space)   # artist:  {'artist_id': 9, 'name': 'BackBeat'}

    # Запускаем сервер с заданными в констнанатах парамертрами
    app.run(
        host = cfg.SERVER_HOST, 
        port = cfg.SERVER_PORT, 
        debug = True
    )

'''
    db = DbInteraction(
        host='192.168.1.120',
        port=3360,
        user='root',
        password='familia',
        dbname='some_db',
        rebuild_db=True
    )
'''