from tkinter import ttk
from loader import gdb, tk, odb
from tkinter import messagebox as ms


class AddFrame(tk.Toplevel):
    """Окно добавления товара"""
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
        """Безопасная передача данных в бд"""
        descr = self.entry_description.get()
        price = self.entry_money.get()
        if descr == '' or price == '':
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
    """Окно редактирования товара"""
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
        """Подставление старых данных из бд"""
        self.db.default_data_db(self.sel_id)
        row = self.db.c.fetchone()
        self.entry_description.insert(0, row[1])
        self.entry_money.insert(0, row[2])


class DelFrame(tk.Toplevel):
    """Окно подтверждения удаления товара"""
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
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.del_record_db(self.sel_id),
                                                      self.destroy()])


class AddToCartFrame(DelFrame):
    """Окно подтверждения добавления товара в корзину"""
    def __init__(self, sel_id):
        super().__init__(sel_id)
        self.title('Cart+')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Add')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.add_to_cart_db(self.sel_id),
                                                      self.destroy()])


class RmFromCartFrame(DelFrame):
    """Окно подтверждения удаления товара из корзины"""
    def __init__(self, sel_id):
        super().__init__(sel_id)
        self.title('Cart-')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Remove')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.rm_from_cart_db(self.sel_id),
                                                      self.destroy()])


class CleanCart(DelFrame):
    """Окно подтверждения очистки корзины"""
    def __init__(self):
        super().__init__(0)
        self.title('Clean Cart')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Clean')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.clean_cart_db(),
                                                      self.destroy()])


class OrderFrame(tk.Toplevel):
    """Окно подтверждения заказа"""
    def __init__(self, username):
        super().__init__()
        self.db = gdb
        self.odb = odb
        self.init_child()
        self.username = username

        self.goods_ids = ''
        self.goods_names = ''
        self.total = 0

        self.order_info()
        self.widgets()

        self.grab_set()
        self.focus_set()

    def order_info(self):
        """Получение товаров из корзины"""
        self.db.show_cart_db()
        rows = self.db.c.fetchall()
        names, ids = [], []
        for row in rows:
            print(row[0], row[1], row[2])
            ids.append(row[0])
            names.append(row[1])
            self.total += row[2]
        self.goods_names = ", ".join(names)
        self.goods_ids = ", ".join(str(e) for e in ids)
        self.total = round(self.total, 2)
        print(self.goods_ids, self.goods_names)

    def init_child(self):
        self.title('Order')
        self.geometry('+900+500')
        self.resizable(False, False)
        self.btn_ok = ttk.Button(self, text='Order')

    def widgets(self):
        self.label_goods = tk.Label(self, text='Goods in Cart:')
        self.label_goods_list = tk.Label(self, text=self.goods_names)
        self.label_total = tk.Label(self, text='Total:')
        self.label_total_value = tk.Label(self, text=f'${self.total}')
        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.label_goods.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        self.label_goods_list.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
        self.label_total.grid(row=2, column=0, padx=20, pady=10)
        self.label_total_value.grid(row=2, column=1, padx=20, pady=10)
        self.btn_cancel.grid(row=3, column=1, padx=30, pady=10)
        self.btn_ok.grid(row=3, column=0, padx=30, pady=10)
        self.btn_ok.bind('<Button-1>', self.safe_order)

    def safe_order(self, event):
        """Безопасное оформление заказа"""
        if self.goods_names == '':
            ms.showerror('Oops!', 'Cart is empty!')
        else:
            try:
                self.odb.create_order_db(self.username, self.goods_ids, self.total)
                self.db.clean_cart_db()
                self.destroy()
            except:
                ms.showerror('Oops!', 'Something incorrect!')


class ChangeStatusFrame(tk.Toplevel):
    """Окно смены статуса заказа"""
    def __init__(self, sel_id):
        super().__init__()
        self.sel_id = sel_id
        self.db = odb

        self.default_data()
        self.init_child()
        self.title('Order Status')
        self.widgets()
        self.geometry('+300+500')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def init_child(self):
        self.label_uid = tk.Label(self, text=f'Client ID: {self.client_id}')
        self.cbox_state = ttk.Combobox(self, state="readonly", values=[u'Paid', u'Sent'])
        self.label_state = tk.Label(self, text='Order Status:')
        self.label_goods = tk.Label(self, text=f'Goods in order: {self.goods}')
        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.btn_ok = ttk.Button(self, text='Update')

    def default_data(self):
        """Получение информации о заказе из бд"""
        self.db.default_data_db(self.sel_id)
        row = self.db.c.fetchone()
        self.client_id = row[1]
        self.goods = row[2]
        self.state = row[4]

    def widgets(self):
        self.cbox_state.current(0)
        self.label_uid.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        self.label_goods.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
        self.label_state.grid(row=3, column=0, padx=20, pady=10)
        self.cbox_state.grid(row=3, column=1, padx=20, pady=10)
        self.btn_ok.grid(row=4, column=0, padx=20, pady=10)
        self.btn_cancel.grid(row=4, column=1, padx=20, pady=10)
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.update_order_state_db(self.sel_id, self.cbox_state.get()),
                                                      self.destroy()])


class RmOrderFrame(DelFrame):
    """Окно подтверждения удаления заказа"""
    def __init__(self, sel_id):
        super().__init__(sel_id)
        self.db = odb
        self.title('Order-')

    def ok_button(self):
        self.btn_ok = ttk.Button(self, text='Delete')
        self.btn_ok.bind('<Button-1>', lambda event: [self.db.delete_order_db(self.sel_id),
                                                      self.destroy()])


class ShowOrdersFrame(tk.Toplevel):
    """Окно просмотра заказов"""
    def __init__(self, uid):
        super().__init__()
        self.uid = uid
        self.db = odb
        self.tree = ttk.Treeview(self, columns=('ID', 'total', 'state'), height=15, show='headings',
                                 selectmode="browse")   # Дерево отображения заказов юзера
        self.scroll = tk.Scrollbar(self, command=self.tree.yview)
        self.init_child()
        self.title("My Orders")
        self.geometry('225x150+300+300')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def init_child(self):
        self.get_data_by_user()

        self.tree.column('ID', width=75, anchor=tk.CENTER)
        self.tree.column('total', width=77, anchor=tk.CENTER)
        self.tree.column('state', width=50, anchor=tk.CENTER)

        self.tree.heading('ID', text='Order ID')
        self.tree.heading('total', text='Total $')
        self.tree.heading('state', text='Status')
        self.tree.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scroll.set)

    def get_data_by_user(self):
        """Передача данных о заказах из бд в дерево отображения"""
        self.db.get_orders_by_username_db(self.uid)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
