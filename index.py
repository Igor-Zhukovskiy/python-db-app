# ==========================================
# Жуковский Егор Романович
# это файл для старта программы
# ==========================================

# ипортирование модулей python
import tkinter as tk
from tkinter import ttk

# импротирование локальных модулей
# from modules.login import Login
from modules.db import Db

# основной класс программы
class Main(tk.Frame):
    # конструктор
    def __init__(self, root, db):
        self.root = root
        # позволяет реализовывать функцию start(), без него работать не будет
        super().__init__(root)
        self.initMain()
        self.db = db
        self.view_records()
    
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

        self.tree = ttk.Treeview(self.root, columns=('id', 'title'), height=15, show='headings')
        self.tree.column('id', width=30, anchor=tk.CENTER)
        self.tree.column('title', width=315, anchor=tk.CENTER)

        self.tree.heading('id', text='ID')  
        self.tree.heading('title', text='Название')
        self.tree.pack()

    # def view_records(self):
    #     self.cur.execute('''SELECT * FROM consoles''')
    #     [self.tree.delete(i) for i in self.tree.get_children()] 
    #     [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def view_records(self):
        self.db.cur.execute('''Select * From consoles;''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


# функция запуску окна входа пользователя
# использует условие с exit(), если не выполняется то остонавливает выполнения программы 

# def loginCheck():
#     login = Login()
#     login.root.mainloop()
#     if login.loginStatus == False:
#         exit()

# функция запуска основного приложения
def start():
    root = tk.Tk()
    db = Db()
    mainWindow = Main(root, db)
    mainWindow.pack()
    root.resizable(False, False)
    root.geometry('650x450')
    root.mainloop()

if __name__ == "__main__":
    # loginCheck()
    start()
