from mainframes import UserFrame, AdminFrame
from loader import root_frame


def handle_focus_user(event):
    if event.widget == root_frame:
        app.view_data()


if __name__ == "__main__":
    frame_mode = '1'
    if frame_mode == '1':
        app = UserFrame(root_frame)
    elif frame_mode == '0':
        app = AdminFrame(root_frame)
    app.pack()
    root_frame.bind("<FocusIn>", handle_focus_user)
    root_frame.title("Shop")
    root_frame.geometry("590x450+300+200")
    root_frame.resizable(False, False)
    root_frame.mainloop()

