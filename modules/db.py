from multiprocessing import connection
import mysql.connector

# Используется для работы с БД
class Db:
    def __init__(self):
        # подключение к базе данных, важно соблюдать последовательность
        self.cnx = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password", # при необходимости введите пароль от своего локального сервера
            database = "python_app_db"
        )

        # используется для создания запросов
        self.cur = self.cnx.cursor(buffered = True)

        # последовательность подключения к бд
        # cnx = connect(host, user, passowrd, database) для подключения к базе данных
        # cur = cnx.cursor(buffered = True) подготовка к передаче запроса
        # cur.execute(''' SQL запрос ''') запрос
        # cur.fetchall() возвращает результат запроса
