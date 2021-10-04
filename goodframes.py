from tkinter import ttk
from loader import gdb, tk
from tkinter import messagebox as ms


class AddFrame(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.db = gdb
        self.init_child()
        self.geometry('+900+500')
        self.resizable(False, False)
        self.widgets()
        self.grab_set()
        self.focus_set()

    def init_child(self):
        self.title('Add good')
        self.btn_ok = ttk.Button(self, text='Add')

    def widgets(self):
        self.label_sum = tk.Label(self, text='Price:')
        self.label_description = tk.Label(self, text='Description:')
        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.entry_money = ttk.Entry(self)
        self.entry_description = ttk.Entry(self)
        self.label_description.grid(row=0, column=0, padx=20, pady=10)
        self.label_sum.grid(row=1, column=0, padx=20, pady=10)
        self.entry_description.grid(row=0, column=1, padx=20, pady=10)
        self.entry_money.grid(row=1, column=1, padx=20, pady=10)
        self.btn_cancel.grid(row=2, column=1, padx=30, pady=10)
        self.btn_ok.grid(row=2, column=0, padx=30, pady=10)
        self.btn_ok.bind('<Button-1>', self.safe_set)

    def safe_set(self, event):
        descr = self.entry_description.get()
        price = self.entry_money.get()
        if descr=='' or price=='':
            ms.showerror('Oops!', 'All fields are required to set!')
        else:
            try:
                self.try_set(descr, price)
                self.destroy()
            except:
                ms.showerror('Oops!', 'Price must be numeric!')

    def try_set(self, descr, price):
        self.db.insert_data_db(descr, float(price))


class EditFrame(AddFrame):
    def __init__(self, sel_id):
        super().__init__()
        self.sel_id = sel_id
        self.default_data()

    def init_child(self):
        self.title('Edit good')
        self.btn_ok = ttk.Button(self, text='Edit')

    def try_set(self, descr, price):
        self.db.edit_record_db(descr, float(price), self.sel_id)

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
        self.geometry('+400+300')
        self.resizable(False, False)
        self.ok_button()
        self.label_description.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.btn_cancel.grid(row=1, column=1, padx=30, pady=10)
        self.btn_ok.grid(row=1, column=0, padx=30, pady=10)
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

class clean_cart(DelFrame):
    def __init__(self):
        super().__init__(0)
        self.title('Clean Cart')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Clean')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.clean_cart_db(),
                                                      self.destroy()])
