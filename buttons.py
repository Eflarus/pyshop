from goodframes import *


class DefaultButton(tk.Frame):
    """Дефолтный конструктор кнопок"""
    def __init__(self, toolbar, text, command, image, side='l'):
        super().__init__(toolbar)
        btn_open_dialog = tk.Button(toolbar, text=text, command=command, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=image)
        if side == 'r':
            btn_open_dialog.pack(side=tk.RIGHT)
        else:
            btn_open_dialog.pack(side=tk.LEFT)


class AddButton(DefaultButton):
    """Кнопка добавления товара"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/add.png')
        super().__init__(toolbar=frame.toolbar,
                         text='Add Good',
                         command=AddFrame,
                         image=self.img)


class DelButton(DefaultButton):
    """Кнопка удаления товара"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/rm.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Delete Good',
                         command=lambda: self.safe_del(),
                         image=self.img)

    def safe_del(self):
        """Срабатывание только при выбранном товаре"""
        try:
            DelFrame(self.frame.get_sel_id())
        except:
            pass


class EditGoodButton(DefaultButton):
    """Кнопка редактирования товара"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/edit.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Edit Good',
                         command=lambda: self.safe_edit(),
                         image=self.img)

    def safe_edit(self):
        """Срабатывание только при выбранном товаре"""
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
        """Срабатывание только при выбранном товаре"""
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
        """Срабатывание только при выбранном товаре"""
        try:
            RmFromCartFrame(self.frame.get_sel_id())
        except:
            pass


class ShowCartButton(DefaultButton):
    """Кнопка просмотр корзины"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/show-cart.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Show Cart',
                         command=lambda: frame.show_cart(),
                         image=self.img)


class DelCartButton(DefaultButton):
    """Кнопка очистки корзины"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/clean-cart.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Clean Cart',
                         command=lambda: CleanCart(),
                         image=self.img)


class OrderButton(DefaultButton):
    """Кнопка оформления заказа"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/order.png')
        super().__init__(frame.toolbar,
                         text='Order',
                         command=lambda: OrderFrame(frame.session_username),
                         image=self.img,
                         side='r')


class ShowOrdersButton(DefaultButton):
    """Кнопка просмотр заказов юзера"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/sent.png')
        super().__init__(frame.toolbar,
                         text='My Orders',
                         command=lambda: ShowOrdersFrame(frame.session_username),
                         image=self.img,
                         side='r')


class ChangeStateButton(DefaultButton):
    """Кнопка смены статуса заказа"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/edit.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Change Status',
                         command=lambda: self.safe_change(),
                         image=self.img)

    def safe_change(self):
        """Срабатывание только при выбранном заказе"""
        try:
            ChangeStatusFrame(self.frame.get_sel_id())
        except:
            pass


class DelOrderButton(DefaultButton):
    """Кнопка удаления заказа"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/rm.png')
        self.frame = frame
        super().__init__(frame.toolbar,
                         text='Delete Order',
                         command=lambda: self.safe_del_order(),
                         image=self.img)

    def safe_del_order(self):
        """Срабатывание только при выбранном заказе"""
        try:
            RmOrderFrame(self.frame.get_sel_id())
        except:
            pass


class UpdateButton(DefaultButton):
    """Кнопка перезагрузки дерева отображения"""
    def __init__(self, frame):
        self.img = tk.PhotoImage(file='icons/updating.png')
        super().__init__(frame.toolbar,
                         text='Refresh',
                         command=lambda: frame.view_data(),
                         image=self.img,
                         side='r')
