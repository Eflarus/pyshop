import tkinter as tk
from tkinter import ttk
from loader import gdb


class AddFrame(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.db = gdb
        self.init_child()

    def init_child(self):
        self.title('Add good')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Description:')
        label_description.place(x=50, y=50)
        label_sum = tk.Label(self, text='Price:')
        label_sum.place(x=50, y=80)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=80)

        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.btn_cancel.place(x=300, y=150)

        self.btn_ok = ttk.Button(self, text='Add')
        self.btn_ok.place(x=220, y=150)
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.insert_data_db(self.entry_description.get(),
                                                                             self.entry_money.get()),
                                                      self.destroy()])
        self.grab_set()
        self.focus_set()


class EditFrame(AddFrame):
    def __init__(self, sel_id):
        super().__init__()
        self.init_edit()
        self.sel_id = sel_id
        self.default_data()

    def init_edit(self):
        self.title('Edit good')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=205, y=150)
        btn_edit.bind('<Button-1>', lambda event: [self.db.edit_record_db(self.entry_description.get(),
                                                                          self.entry_money.get(),
                                                                          self.sel_id),
                                                   self.destroy()])
        self.btn_cancel.destroy()

    def default_data(self):
        self.db.default_data_db(self.sel_id)
        row = self.db.c.fetchone()
        self.entry_description.insert(0, row[1])
        self.entry_money.insert(0, row[2])


class DelFrame(tk.Toplevel):
    def __init__(self, sel_id):
        super().__init__()
        self.sel_id = sel_id
        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.label_description = tk.Label(self, text='Are you sure?')
        self.db = gdb
        self.init_child()

    def init_child(self):
        self.title('Delete')
        self.geometry('210x100+400+300')
        self.resizable(False, False)
        self.label_description.place(x=60, y=12)
        self.btn_cancel.place(x=110, y=60)
        self.ok_button()
        self.btn_ok.place(x=20, y=60)
        self.grab_set()
        self.focus_set()

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Remove')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.delete_records_db(self.sel_id),
                                                      self.destroy()])


class AddToCartFrame(DelFrame):
    def __init__(self, sel_id):
        super().__init__(sel_id)
        self.title('Cart+')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Add')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.add_to_cart_db(self.sel_id),
                                                      self.destroy()])

class RmFromCartFrame(DelFrame):
    def __init__(self, sel_id):
        super().__init__(sel_id)
        self.title('Cart-')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Remove')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.rm_from_cart_db(self.sel_id),
                                                      self.destroy()])
