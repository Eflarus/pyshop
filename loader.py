import tkinter as tk
from db import GoodsDB, UsersDB, OrdersDB

gdb = GoodsDB()
udb = UsersDB()
odb = OrdersDB()

root_frame = tk.Tk()
root_frame.resizable(False, False)


