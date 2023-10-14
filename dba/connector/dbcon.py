from mysql.connector import connect, Error

def DBConnect():

    # Подключение к базе MySQL
    conn = connect(host='127.0.0.1', user='root', password='root', database='spaces')

    return conn