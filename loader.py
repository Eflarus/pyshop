import tkinter as tk
from db import GoodsDB, UsersDB, OrdersDB
"""Подключение к таблицам бд"""
gdb = GoodsDB()
udb = UsersDB()
odb = OrdersDB()

root_frame = tk.Tk()    # Базовый пустой фрейм
root_frame.resizable(False, False)


