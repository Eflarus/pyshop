from mainframes import UserFrame, AdminFrame, EnterFrame
from loader import root_frame, usermode


def handle_focus_user(event):
    if event.widget == root_frame:
        app.view_data()


if __name__ == "__main__":

    EnterFrame(root_frame)
    if usermode == 'Admin':
        app = AdminFrame(root_frame)
        app.pack()
        root_frame.bind("<FocusIn>", handle_focus_user)
    elif usermode == 'Customer':
        app = UserFrame(root_frame)
        app.pack()
        root_frame.bind("<FocusIn>", handle_focus_user)
    elif usermode == 'Picker':
        app = UserFrame(root_frame)
        app.pack()

    root_frame.title("Shop")
    root_frame.geometry("590x450+300+200")
    root_frame.resizable(False, False)
    root_frame.mainloop()

