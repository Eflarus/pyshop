import tkinter as tk
from tkinter import ttk
from buttons import *
from loader import gdb, udb, usermode



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


