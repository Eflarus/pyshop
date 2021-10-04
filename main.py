from loader import root_frame, usermode
from login import EnterFrame


if __name__ == "__main__":

    EnterFrame(root_frame)
    print(usermode)
    root_frame.title("Shop")
    root_frame.geometry("590x450+300+200")
    root_frame.resizable(False, False)
    root_frame.mainloop()

