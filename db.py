import sqlite3


class GoodsDB:
    def __init__(self):
        self.conn = sqlite3.connect('goods.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS goods (id integer primary key, description text, costs real, cart text)''')
        self.conn.commit()

    def insert_data_db(self, description, cost):
        self.c.execute('''INSERT INTO goods(description, costs, cart) VALUES (?, ?, ?)''',
                       (description, cost, 'No'))
        self.conn.commit()

    def edit_record_db(self, description, cost, sel_id):
        self.c.execute('''UPDATE goods SET description=?, costs=? WHERE ID=?''',
                       (description, cost, sel_id))
        self.conn.commit()

    def add_to_cart_db(self, sel_id):
        self.c.execute('''UPDATE goods SET cart=? WHERE ID=?''',
                       ('In Cart', sel_id))
        self.conn.commit()

    def rm_from_cart_db(self, sel_id):
        self.c.execute('''UPDATE goods SET cart=? WHERE ID=?''',
                       ('No', sel_id))
        self.conn.commit()

    def view_data_db(self):
        self.c.execute('''SELECT * FROM goods''')

    def delete_records_db(self, sel_id):
        self.c.execute('''DELETE FROM goods WHERE id=?''', (sel_id,))
        self.conn.commit()
        print(sel_id, 'deld')

    # def search_records_db(self, description):
    #     description = ('%' + description + '%',)
    #     self.c.execute('''SELECT * FROM goods WHERE description LIKE ?''', description)

    def show_cart_db(self):
        description = ('%In Cart%',)
        self.c.execute('''SELECT * FROM goods WHERE cart LIKE ?''', description)

    def default_data_db(self, sel_id):
        self.c.execute('''SELECT * FROM goods WHERE id=?''', (sel_id,))
        print(sel_id, 'edd')

class UsersDB:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL, 
        role TEXT NOT NULL);''')
        self.conn.commit()

    def find_user_db(self, username, password):
        self.c.execute('''SELECT * FROM user WHERE username = ? and password = ?''', (username, password))

    def create_user_db(self, username, password, role):
        self.c.execute('''INSERT INTO user(username,password, role) VALUES(?,?,?)''', (username, password, role))
        self.conn.commit()

    def find_username_db(self, username):
        self.c.execute('''SELECT username FROM user WHERE username = ?''', (username,))

    def find_usermode_db(self, username):
        self.c.execute('''SELECT role FROM user WHERE username = ?''', (username,))