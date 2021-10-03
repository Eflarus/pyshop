import tkinter as tk

import goodframes
from goodframes import *


class DefaultButton(tk.Frame):
    def __init__(self, toolbar, text, command, image, side='l'):
        super().__init__(toolbar)
        btn_open_dialog = tk.Button(toolbar, text=text, command=command, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=image)
        if side == 'r':
            btn_open_dialog.pack(side=tk.RIGHT)
        else:
            btn_open_dialog.pack(side=tk.LEFT)


class AddButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        super().__init__(toolbar=frame.toolbar,
                         text='Add Good',
                         command=AddFrame,
                         image=self.img)


class DelButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Delete Good',
                         command=lambda: self.safe_del(),
                         image=self.img)

    def safe_del(self):
        try:
            DelFrame(self.frame.get_sel_id())
        except:
            pass


class EditGoodButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Edit Good',
                         command=lambda: self.safe_edit(),
                         image=self.img)

    def safe_edit(self):
        try:
            EditFrame(self.frame.get_sel_id())
        except:
            pass


class AddToCartButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Add to Cart',
                         command=lambda: self.safe_add_to_cart(),
                         image=self.img)

    def safe_add_to_cart(self):
        try:
            AddToCartFrame(self.frame.get_sel_id())
        except:
            pass


class RmFromCartButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Remove from Cart',
                         command=lambda: self.safe_rm_from_cart(),
                         image=self.img)

    def safe_rm_from_cart(self):
        try:
            RmFromCartFrame(self.frame.get_sel_id())
        except:
            pass


class ShowCartButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Show Cart',
                         command=lambda: frame.show_cart(),
                         image=self.img)


class UpdateButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='def.gif')
        super().__init__(frame.toolbar,
                         text='Home',
                         command=lambda: frame.view_data(),
                         image=self.img,
                         side='r')
