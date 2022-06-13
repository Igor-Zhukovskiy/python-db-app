import tkinter as tk
from tkinter import ttk

# tk.TopLevel означает что окно будет поевлятся поверх предыдущего
class Insert(tk.Toplevel):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self.initChild()

    # Создает окно для внесения новой строки
    def initChild(self):
        self.title("Добавить консоль")
        self.geometry('400x260+400+300')
        self.resizable(False, False)

        # создание лейбла
        consoleTitle = tk.Label(self, text="Название консоли")
        consoleTitle.place(x=50, y=50)

        # создание поля ввода
        self.consoleTitleEntry = ttk.Entry(self)
        self.consoleTitleEntry.place(x=200, y=50)

        btnCancel = tk.Button(self, text="Отмена", command=self.destroy)
        btnCancel.place(x=300, y=170)

        # Если вам необходимо получать данные поля ввода по нажатию на кнопку это лучше делать через lamba event:
        addRow = lambda event: self.db.insertConsole(self.consoleTitleEntry.get())
        btnOk = tk.Button(self, text="Ок", command=self.destroy)
        btnOk.place(x=220, y=170)
        btnOk.bind('<Button-1>', addRow)

        self.grab_set()
        self.focus_set()

