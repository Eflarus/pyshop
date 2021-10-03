import tkinter as tk
from tkinter import ttk
from buttons import *
from loader import gdb, udb, usermode

from tkinter import messagebox as ms

class MainFrame(tk.Frame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.tree = ttk.Treeview(self)
        self.db = gdb
        self.toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)


    def view_data(self):
        self.db.view_data_db()
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def get_sel_id(self):
        selected = self.tree.focus()
        return self.tree.item(selected, 'values')[0]


class AdminFrame(MainFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs'),
                                 height=15, show='headings', selectmode="browse")
        self.init_user()
        self.scroll = tk.Scrollbar(self, command=self.tree.yview)

    def init_user(self):
        add_button = AddButton(self)
        del_button = DelButton(self)
        edit_button = EditGoodButton(self)
        update_button = UpdateButton(self)

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Description')
        self.tree.heading('costs', text='Price')

        self.tree.pack(side=tk.LEFT)

        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scroll.set)


class UserFrame(MainFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.scroll = tk.Scrollbar(self, command=self.tree.yview)
        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'cart'),
                                 height=15, show='headings', selectmode="browse")
        self.init_user()
        self.show_cart()

    def init_user(self):
        add_to_cart_button = AddToCartButton(self)
        rm_from_cart_button = RmFromCartButton(self)
        cart_button = ShowCartButton(self)
        update_button = UpdateButton(self)

        self.tree.column('ID', width=50, anchor=tk.CENTER)
        self.tree.column('description', width=300, anchor=tk.CENTER)
        self.tree.column('costs', width=75, anchor=tk.CENTER)
        self.tree.column('cart', width=75, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Description')
        self.tree.heading('costs', text='Price')
        self.tree.heading('cart', text='Cart')

        self.tree.pack(side=tk.LEFT)

        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scroll.set)

    def show_cart(self):
        self.db.show_cart_db()
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


class EnterFrame:
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.db = udb
        self.um = usermode
        self.login_frame()

    def login_frame(self):
        head = tk.Label(self, text='LOGIN')
        head.pack()
        self.logfr = tk.Frame(self)
        label_username = tk.Label(self.logfr, text='Username: ')
        label_password = tk.Label(self.logfr, text='Password: ')
        entry_username = ttk.Entry(self.logfr)
        entry_password = ttk.Entry(self.logfr)
        button_login = ttk.Button(self.logfr, text='Enter',
                                  command=lambda: self.login(entry_username.get(), entry_password.get()))
        button_register = ttk.Button(self.logfr, text='Register', command=self.register_frame)
        self.logfr.pack()

    def login(self, unm, pwd):
        self.db.find_user_db(unm, pwd)
        if self.db.c.fetchall():
            self.um = 0
            self.logfr.destroy()
        else:
            ms.showerror('Oops!', 'Username or Password Not Found.')

    def register_frame(self):
        self.logfr.pack_forget()
        head = tk.Label(self, text='Create New User')
        head.pack()
        self.regfr = tk.Frame(self)
        label_username = tk.Label(self.regfr, text='Username: ')
        label_password = tk.Label(self.regfr, text='Password: ')
        label_usermode = tk.Label(self.regfr, text='User Rode: ')
        entry_username = ttk.Entry(self.regfr)
        entry_password = ttk.Entry(self.regfr)
        combobox_um = ttk.Combobox(self.regfr, values=[u'Admin', u'Customer', u'Picker'])
        self.combobox.current(0)
        button_login = ttk.Button(self.logfr, text='Enter',
                                  command=lambda: self.login(entry_username.get(), entry_password.get()))
        button_register = ttk.Button(self.logfr, text='Register', command=self.register_frame)
        self.logfr.pack()