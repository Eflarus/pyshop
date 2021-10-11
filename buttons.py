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
        self.img = tk.PhotoImage(file='icons/add.png')
        super().__init__(toolbar=frame.toolbar,
                         text='Add Good',
                         command=AddFrame,
                         image=self.img)


class DelButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/rm.png')
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
        self.img = tk.PhotoImage(file='icons/edit.png')
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
        self.img = tk.PhotoImage(file='icons/add-cart.png')
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
        self.img = tk.PhotoImage(file='icons/rm-cart.png')
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
        self.img = tk.PhotoImage(file='icons/show-cart.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Show Cart',
                         command=lambda: frame.show_cart(),
                         image=self.img)


class DelCartButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/clean-cart.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Clean Cart',
                         command=lambda: clean_cart(),
                         image=self.img)


class OrderButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/order.png')
        super().__init__(frame.toolbar,
                         text='Order',
                         command=lambda: self.safe_order(frame),
                         image=self.img,
                         side='r')

    def safe_order(self, frame):
        try:
            OrderFrame(frame.session_username)
        except:
            pass


class ShowOrdersButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/sent.png')
        super().__init__(frame.toolbar,
                         text='My Orders',
                         command=lambda: ShowOrdersFrame(frame.session_username),
                         image=self.img,
                         side='r')


class ChangeStateButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/change.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Change Status',
                         command=lambda: self.safe_change(),
                         image=self.img)

    def safe_change(self):
        try:
            ChangeStatusFrame(self.frame.get_sel_id())
        except:
            pass


class DelOrderButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/delete.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Delete Order',
                         command=lambda: self.safe_del_order(),
                         image=self.img)

    def safe_del_order(self):
        try:
            RmOrderFrame(self.frame.get_sel_id())
        except:
            pass


class UpdateButton(DefaultButton):
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/updating.png')
        super().__init__(frame.toolbar,
                         text='Refresh',
                         command=lambda: frame.view_data(),
                         image=self.img,
                         side='r')
