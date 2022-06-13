from tkinter import *
from tkinter import messagebox as ms
import sqlite3

class Login:
    master = Tk()
    master.title('Авторизация')
    login_seccessful = False

    def __init__(self):
        self.create_db_if_not_exists()
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def create_db_if_not_exists(self):
        with sqlite3.connect('./db/avtoriz.db') as db:
            c = db.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL);')
        db.commit()
        db.close()

    def login(self):
        with sqlite3.connect('./db/avtoriz.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.login_seccessful = True
            self.master.destroy()
        else:
            ms.showerror('Уведомление', 'Данный пользователь не найден!')
    
    def new_user(self):
        with sqlite3.connect('./db/avtoriz.db') as db:
            c = db.cursor()
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Уведомление!', 'Имя пользователя занято, Попробуйте другое.')
        else:
            ms.showinfo('Успех!', 'Пользователь создан!!')
            self.log()
        insert = 'INSERT INTO user(username, password) VALUES(?, ?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Создать пользователя'
        self.crf.pack()
        
    def widgets(self):
        self.head = Label(self.master, text='Авторизация', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Логин: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Пароль: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Войти ', bd=3, font=('', 15), pady=5, padx=5, command=self.login).grid()
        Button(self.logf, text=' Создать пользователя ', bd=3, font=('', 15), pady=5, padx=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Логин: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Пароль: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15)).grid(row=1, column=1)
        Button(self.crf, text='Создать пользователя', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Назад', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)
