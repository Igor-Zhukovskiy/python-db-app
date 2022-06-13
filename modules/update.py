import tkinter as tk
from tkinter import ttk


# tk.TopLevel означает что окно будет поевлятся поверх предыдущего
class Update(tk.Toplevel):
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

        consoleId = tk.Label(self, text="Id консоли")
        consoleId.place(x=50, y=90)

        self.consoleIdEntry = ttk.Entry(self)
        self.consoleIdEntry.place(x=200, y=90)

        btnCancel = tk.Button(self, text="Отмена", command=self.destroy)
        btnCancel.place(x=300, y=170)

        # Если вам необходимо получать данные поля ввода по нажатию на кнопку это лучше делать через lamba event:
        # updateRow = lambda event: self.db.cur.execute(f'''Update consoles Set title = "{self.consoleTitleEntry.get()}" Where id = {self.consoleIdEntry.get()};''')
        updateRow = lambda event: self.db.updateConsoles(self.consoleIdEntry.get(), self.consoleTitleEntry.get())
        btnOk = tk.Button(self, text="Ок", command=self.destroy)
        btnOk.place(x=220, y=170)
        btnOk.bind('<Button-1>', updateRow)

        self.grab_set()
        self.focus_set()