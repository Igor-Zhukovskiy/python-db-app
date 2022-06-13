import mysql.connector

# последовательность подключения к бд
        # cnx = connect(host, user, passowrd, database) для подключения к базе данных
        # cur = cnx.cursor(buffered = True) подготовка к передаче запроса
        # cur.execute(''' SQL запрос ''') запрос
        # cur.fetchall() возвращает результат запроса
        # cnx.commit() завершает вводимую комманду

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

    # для внесения данных в таблицу consoles
    def insertConsole(self, consoleName):
        self.cur.execute(f'''Insert into consoles(title) values ("{consoleName}"); ''')
        self.cnx.commit()

    # для внесения данных в таблицу employees
    def insertEmployee(self, name, password):
        self.cur.execute(f'''Insert into employees(name, password) values ("{name}", "{password}")''')
        self.cnx.commit()
    
    def getEmployee(self, name, password):
        self.cur.execute(f'''Select name, password From employees Where name = "{name}" and password = "{password}"''')
        return self.cur.fetchall()

    def updateConsoles(self, id, title):
        self.cur.execute(f'''Update consoles Set title = "{title}" Where id = {id};''')
        self.cnx.commit()
    
    def removeConsoles(self, id):
        self.cur.execute(f'''Delete From consoles Where id = {id} ''')
        self.cnx.commit()

    def searchConsoles(self, title):
        self.cur.execute(f'''Select id From consoles Where title Like '{title}%' ''')
        return self.cur.fetchall()
        # self.cnx.commit()