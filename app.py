from mainframes import UserFrame, AdminFrame
from loader import root_frame, usermode


def handle_focus_user(event, app):
    if event.widget == root_frame:
        app.view_data()


def run_app():
    print('hi')
    if usermode == 'Admin':
        app = AdminFrame(root_frame)
        app.pack()
        root_frame.bind("<FocusIn>", lambda: handle_focus_user(app))
    elif usermode == 'Customer':
        app = UserFrame(root_frame)
        app.pack()
        root_frame.bind("<FocusIn>", lambda: handle_focus_user(app))
    elif usermode == 'Picker':
        app = UserFrame(root_frame)
        app.pack()
    root_frame.mainloop()
