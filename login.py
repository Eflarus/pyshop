import tkinter as tk
from tkinter import ttk
from buttons import *
from loader import udb
from tkinter import messagebox as ms
from app import run_app

class EnterFrame:
    def __init__(self, root_frame):
        self.regfr = tk.Frame(root_frame)
        self.logfr = tk.Frame(root_frame)
        self.db = udb
        self.register_frame()

    def login_frame(self):
        head = tk.Label(self.logfr, text='LOGIN')
        head.grid(row=0, column=0)
        # head.pack()
        label_username = tk.Label(self.logfr, text='Username: ')
        label_username.grid(row=1, column=0)
        label_password = tk.Label(self.logfr, text='Password: ')
        label_password.grid(row=2, column=0)
        self.entry_username = ttk.Entry(self.logfr)
        self.entry_username.grid(row=1, column=1)
        self.entry_password = ttk.Entry(self.logfr)
        self.entry_password.grid(row=2, column=1)
        button_login = ttk.Button(self.logfr, text='Enter',
                                  command=lambda: self.login(
                                      self.entry_username.get(), self.entry_password.get()))
        button_login.grid(row=3, column=0)
        button_register = ttk.Button(self.logfr, text='Register', command=self.log_to_reg)
        button_register.grid(row=3, column=1)

        self.logfr.pack()

    def login(self, username, password):
        self.db.find_user_db(username, password)
        if self.db.c.fetchall():
            self.set_usermode(username)
            print(128)
            self.logfr.pack_forget()
            run_app()


        else:
            ms.showerror('Oops!', 'Username or Password Not Found.')

    def log_to_reg(self):
        self.logfr.pack_forget()
        self.register_frame()

    def register_frame(self):
        head = tk.Label(self.regfr, text='Create New User')
        head.grid(row=0, column=0)
        lbl_unm = tk.Label(self.regfr, text='Username: ')
        lbl_unm.grid(row=1, column=0)
        lbl_pwd = tk.Label(self.regfr, text='Password: ')
        lbl_pwd.grid(row=2, column=0)
        lbl_umode = tk.Label(self.regfr, text='User Role: ')
        lbl_umode.grid(row=3, column=0)
        self.entry_username = ttk.Entry(self.regfr)
        self.entry_username.grid(row=1, column=1)
        self.entry_password = ttk.Entry(self.regfr)
        self.entry_password.grid(row=2, column=1)
        self.cbox_umode = ttk.Combobox(self.regfr, values=[u'Admin', u'Customer', u'Picker'])
        self.cbox_umode.grid(row=3, column=1)
        # cbox_umode.current(0)
        button_register = ttk.Button(self.regfr,
                                     text='Create Account',
                                     command=lambda: self.register(
                                         self.entry_username.get(), self.entry_password.get(), self.cbox_umode.get()))
        button_register.grid(row=4, column=0)
        button_login = ttk.Button(self.regfr, text='Back to Login', command=self.reg_to_log)
        button_login.grid(row=4, column=1)
        self.regfr.pack()

    def register(self, username, password, umode):
        self.db.find_username_db(username)
        if self.db.c.fetchall():
            ms.showerror('Oops!', 'Username already exists.')
        elif password== '':
            ms.showerror('Oops!', 'Password must be set')
        elif username== '':
            ms.showerror('Oops!', 'Username must be set')
        else:
            self.db.create_user_db(username, password, umode)
            self.set_usermode(username)
            print(173)
            self.regfr.pack_forget()

    def reg_to_log(self):
        self.regfr.pack_forget()
        self.login_frame()

    def set_usermode(self, username=1):
        self.db.find_usermode_db(username)
        self.umode = self.db.c.fetchone()[0]
