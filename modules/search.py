import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms


# tk.TopLevel означает что окно будет поевлятся поверх предыдущего
class Search(tk.Toplevel):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self.initChild()

    # Создает окно для внесения новой строки
    def initChild(self):
        self.title("Изменить название")
        self.geometry('400x260+400+300')
        self.resizable(False, False)

        # создание лейбла
        consoleTitle = tk.Label(self, text="Название консоли")
        consoleTitle.place(x=50, y=50)

        # создание поля ввода
        self.consoleTitleEntry = ttk.Entry(self)
        self.consoleTitleEntry.place(x=200, y=50)


        # Если вам необходимо получать данные поля ввода по нажатию на кнопку это лучше делать через lamba event:
        def querry():
            return self.db.cur.execute(f'''Select id From consoles Where title = "{self.consoleTitleEntry.get()}%";''')

        # updateRow = lambda event: ms.showinfo('id is ', f'{querry}')
        # updateRow = lambda event: print(self.db.cur.execute(f'''Select * from consoles;'''))
        updateRow = lambda event: ms.showinfo("possible id:", self.db.searchConsoles(self.consoleTitleEntry.get()))
        btnOk = tk.Button(self, text="Ок", command=self.destroy)
        btnOk.place(x=220, y=170)
        btnOk.bind('<Button-1>', updateRow)

        self.grab_set()
        self.focus_set()