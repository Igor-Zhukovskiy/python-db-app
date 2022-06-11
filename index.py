# Жуковский Егор Романович

# это файл для старта программы

# ипортирование модулей python
from asyncore import ExitNow
import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql

# импротирование локальных модулей
from modules.login import Login

# основной класс программы
class Main(tk.Frame):
    # конструктор
    def __init__(self, root):
        self.root = root
        # позволяет реализовывать функцию start(), без него работать не будет
        super().__init__(root)
        self.initMain()
    
    # метод для отрисовки основного окна
    def initMain(self):
        toolBar = tk.Frame(bg='#aaaaaa', bd=5)
        toolBar.pack(side=tk.TOP, fill=tk.X)

        btnAdd = tk.Button(toolBar, text="Add", bd=0)
        btnAdd.pack(side=tk.LEFT)

        btnRemove = tk.Button(toolBar, text="Remove", bd=0)
        btnRemove.pack(side=tk.LEFT)

        btnSearch = tk.Button(toolBar, text="Search", bd=0)
        btnSearch.pack(side=tk.LEFT)
    
    def getData(self):
        dbData = mysql.connect

# функция запуску окна входа пользователя
# использует условие с exit(), если не выполняется то остонавливает выполнения программы 
def loginCheck():
    login = Login()
    login.root.mainloop()
    if login.loginStatus == False:
        exit()
# функция запуска основного приложения
def start():
    root = tk.Tk()
    mainWindow = Main(root)
    mainWindow.pack()
    root.resizable(False, False)
    root.geometry('650x450+300+200')
    root.mainloop()

if __name__ == "__main__":
    loginCheck()
    start()