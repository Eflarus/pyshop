import tkinter as tk
from tkinter import ttk
from loader import udb
from tkinter import messagebox as ms
from app import run_app

class EnterFrame:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title("Shop Login")
        self.frame.geometry("+300+200")
        self.regfr = tk.Frame(self.frame)
        self.logfr = tk.Frame(self.frame)
        self.db = udb
        self.usermode = tk.StringVar
        self.login_frame()
        self.frame.mainloop()

    def login_frame(self):
        head = tk.Label(self.logfr, text='LOGIN',font = ('',35),pady = 10)
        head.grid(row=0, column=0, columnspan=2)
        label_username = tk.Label(self.logfr, text='Username: ')
        label_username.grid(row=1, column=0, padx=20, pady=10)
        label_password = tk.Label(self.logfr, text='Password: ')
        label_password.grid(row=2, column=0, padx=20, pady=10)
        self.entry_username = ttk.Entry(self.logfr)
        self.entry_username.grid(row=1, column=1, padx=20, pady=10)
        self.entry_password = ttk.Entry(self.logfr)
        self.entry_password.grid(row=2, column=1, padx=20, pady=10)
        button_login = ttk.Button(self.logfr, text='Enter',
                                  command=lambda: self.login(
                                      self.entry_username.get(), self.entry_password.get()))
        button_login.grid(row=3, column=0, padx=20, pady=10)
        button_register = ttk.Button(self.logfr, text='Register', command=self.log_to_reg)
        button_register.grid(row=3, column=1, padx=20, pady=10)

        self.logfr.pack()

    def login(self, username, password):
        self.db.find_user_db(username, password)
        if self.db.c.fetchall():
            usermode = self.set_usermode(username)
            print('login destroy', f'with {usermode} mode')
            self.logfr.pack_forget()
            run_app(usermode)
        else:
            ms.showerror('Oops!', 'Username or Password Not Found.')

    def log_to_reg(self):
        self.logfr.pack_forget()
        self.register_frame()

    def register_frame(self):
        head = tk.Label(self.regfr, text='Create New User',font = ('',35),pady = 10)
        head.grid(row=0, column=0, columnspan=2)
        lbl_unm = tk.Label(self.regfr, text='Username: ')
        lbl_unm.grid(row=1, column=0, padx=20, pady=10)
        lbl_pwd = tk.Label(self.regfr, text='Password: ')
        lbl_pwd.grid(row=2, column=0, padx=20, pady=10)
        lbl_umode = tk.Label(self.regfr, text='User Role: ')
        lbl_umode.grid(row=3, column=0, padx=20, pady=10)
        self.entry_username = ttk.Entry(self.regfr)
        self.entry_username.grid(row=1, column=1, padx=20, pady=10)
        self.entry_password = ttk.Entry(self.regfr)
        self.entry_password.grid(row=2, column=1, padx=20, pady=10)
        self.cbox_umode = ttk.Combobox(self.regfr, state="readonly", values=[u'Admin', u'Customer', u'Picker'])
        self.cbox_umode.grid(row=3, column=1, padx=20, pady=10)
        self.cbox_umode.current(0)
        button_register = ttk.Button(self.regfr,
                                     text='Create Account',
                                     command=lambda: self.register(
                                         self.entry_username.get(), self.entry_password.get(), self.cbox_umode.get()))
        button_register.grid(row=4, column=0, padx=20, pady=30)
        button_login = ttk.Button(self.regfr, text='Back to Login', command=self.reg_to_log)
        button_login.grid(row=4, column=1, padx=20, pady=30)
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
            usermode = self.set_usermode(username)
            print('reg destroy', f'with {usermode} mode')
            self.regfr.pack_forget()
            run_app(usermode)

    def reg_to_log(self):
        self.regfr.pack_forget()
        self.login_frame()

    def set_usermode(self, username):
        self.db.find_usermode_db(username)
        return self.db.c.fetchone()[0]

