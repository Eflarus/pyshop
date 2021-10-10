from mainframes import UserFrame, AdminFrame, PickerFrame
from loader import root_frame


def run_app(usermode, username):
    print(usermode)
    if usermode == 'Admin':
        root_frame.title(f"Shop: Admin {username}")
        app = AdminFrame(root_frame)
        app.pack()

    elif usermode == 'Customer':
        root_frame.title(f"Shop: {username}")
        app = UserFrame(root_frame, username)
        app.pack()

    elif usermode == 'Picker':
        root_frame.title(f"Shop: Picker {username}")
        app = PickerFrame(root_frame)
        app.pack()

    root_frame.mainloop()
