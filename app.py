from mainframes import UserFrame, AdminFrame
from loader import root_frame


def handle_focus_user(event, app):
    if event.widget == root_frame:
        app.view_data()


def run_app(usermode):
    print(usermode)
    if usermode == 'Admin':
        root_frame.title("Shop: Admin")
        app = AdminFrame(root_frame)
        app.pack()
        root_frame.bind("<FocusIn>", lambda: handle_focus_user(app))

    elif usermode == 'Customer':
        root_frame.title("Shop")
        app = UserFrame(root_frame)
        app.pack()
        root_frame.bind("<FocusIn>", lambda: handle_focus_user(app))

    elif usermode == 'Picker':
        root_frame.title("Shop: Picker")
        app = UserFrame(root_frame)
        app.pack()
    root_frame.mainloop()
