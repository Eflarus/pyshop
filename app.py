from mainframes import UserFrame, AdminFrame, PickerFrame
from loader import root_frame, udb


class RunApp:
    """Класс вызова визуальных интерфейсов по ролям"""
    def __init__(self, username):
        self.db = udb
        self.username = username
        self.set_usermode()
        self.run_app()

    def run_app(self):
        print(self.usermode, 'qq')
        if self.usermode == 'Admin':
            root_frame.title(f"Shop: Admin {self.username}")
            app = AdminFrame(root_frame)
            app.pack()

        elif self.usermode == 'Customer':
            root_frame.title(f"Shop: Customer {self.username}")
            app = UserFrame(root_frame, self.username)
            app.pack()

        elif self.usermode == 'Picker':
            root_frame.title(f"Shop: Picker {self.username}")
            app = PickerFrame(root_frame)
            app.pack()

    def set_usermode(self):
        """Получение юзермода по юзернейму из дб"""
        self.db.find_usermode_db(self.username)
        self.usermode = self.db.c.fetchone()[0]

