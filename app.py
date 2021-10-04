from mainframes import UserFrame, AdminFrame
from loader import root_frame





def run_app(usermode):
    print(usermode)
    if usermode == 'Admin':
        root_frame.title("Shop: Admin")
        app = AdminFrame(root_frame)
        app.pack()

    elif usermode == 'Customer':
        root_frame.title("Shop")
        app = UserFrame(root_frame)
        app.pack()

    elif usermode == 'Picker':
        root_frame.title("Shop: Picker")
        app = UserFrame(root_frame)
        app.pack()

    root_frame.mainloop()
