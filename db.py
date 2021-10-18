import sqlite3


class ShopDB:
    def __init__(self):
        self.conn = sqlite3.connect('shop.db')
        self.c = self.conn.cursor()
        self._create_goods_db()
        self._create_users_db()
        self._create_orders_db()

    def _create_goods_db(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS goods (id INTEGER PRIMARY KEY, description TEXT NOT NULL, costs REAL NOT 
            NULL, cart TEXT)''')
        self.conn.commit()

    def _create_users_db(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL, 
                role TEXT NOT NULL);''')
        self.conn.commit()

    def _create_orders_db(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, username TEXT NOT NULL, 
                goods_ids TEXT NOT NULL, score REAL NOT NULL, state TEXT NOT NULL);''')
        self.conn.commit()

class GoodsDB(ShopDB):
    def __init__(self):
        super().__init__()
        self.clean_cart_db()

    def insert_data_db(self, description, cost):
        self.c.execute('''INSERT INTO goods(description, costs, cart) VALUES (?, ?, ?)''',
                       (description, cost, 'No'))
        self.conn.commit()

    def edit_record_db(self, description, cost, sel_id):
        self.c.execute('''UPDATE goods SET description=?, costs=? WHERE ID=?''', (description, cost, sel_id))
        self.conn.commit()

    def add_to_cart_db(self, sel_id):
        self.c.execute('''UPDATE goods SET cart=? WHERE ID=?''', ('In Cart', sel_id))
        self.conn.commit()

    def rm_from_cart_db(self, sel_id):
        self.c.execute('''UPDATE goods SET cart=? WHERE ID=?''', ('No', sel_id))
        self.conn.commit()

    def view_data_db(self):
        self.c.execute('''SELECT * FROM goods''')

    def delete_records_db(self, sel_id):
        self.c.execute('''DELETE FROM goods WHERE id=?''', (sel_id,))
        self.conn.commit()
        print(sel_id, 'deld')

    def show_cart_db(self):
        description = ('%In Cart%',)
        self.c.execute('''SELECT * FROM goods WHERE cart LIKE ?''', description)

    def default_data_db(self, sel_id):
        self.c.execute('''SELECT * FROM goods WHERE id=?''', (sel_id,))
        print(sel_id, 'edd')

    def clean_cart_db(self):
        self.c.execute('''UPDATE goods SET cart = "No"''')
        self.conn.commit()
        print('cart clean')


class UsersDB(ShopDB):
    def __init__(self):
        super().__init__()

    def find_user_db(self, username, password):
        self.c.execute('''SELECT * FROM users WHERE username = ? and password = ?''', (username, password))

    def create_user_db(self, username, password, role):
        self.c.execute('''INSERT INTO users(username,password, role) VALUES(?,?,?)''', (username, password, role))
        self.conn.commit()

    def find_username_db(self, username):
        self.c.execute('''SELECT username FROM users WHERE username = ?''', (username,))

    def find_usermode_db(self, username):
        self.c.execute('''SELECT role FROM users WHERE username = ?''', (username,))

class OrdersDB(ShopDB):
    def __init__(self):
        super().__init__()

    def view_data_db(self):
        self.c.execute('''SELECT * FROM orders''')

    def get_orders__by_username_db(self, username):
        self.c.execute('''SELECT ID, SCORE, STATE FROM orders WHERE username = ? ''', (username,))

    def default_data_db(self, sel_id):
        self.c.execute('''SELECT * FROM orders WHERE id=?''', (sel_id,))
        print(sel_id, 'getinfo')

    def create_order_db(self, username, goods_ids, score):
        self.c.execute('''INSERT INTO orders(username, goods_ids, score, state) VALUES(?,?,?,?)''',
                       (username, goods_ids, score, 'Paid'))
        self.conn.commit()

    def update_order_state_db(self, order_id, state):
        self.c.execute('''UPDATE orders SET state=? WHERE ID=?''', (state, order_id))
        self.conn.commit()

    def delete_order_db(self, order_id):
        self.c.execute('''DELETE FROM orders WHERE id=?''', (order_id,))
        self.conn.commit()
        print(order_id, ' order deld')
