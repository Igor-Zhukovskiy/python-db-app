import tkinter as tk
from tkinter import ttk

class Login():
    # хранит в себе проверку зарегестрирован юзер или нет
    loginStatus = False
    root = tk.Tk()

    def __init__(self):

        self.loginCheck()

    def setLogin(self):
        print(self.loginStatus)
        self.loginStatus = True
        self.root.destroy()

    def loginCheck(self):
        btnCheck = tk.Button(self.root, text="login", bd=0, command=self.setLogin)
        btnCheck.pack()