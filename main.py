from options import *
from tkinter import *


def main():
    window = Tk()
    window.title('Math Functions')
    window.geometry('250x160')
    window.resizable(False, False)
    widgets = Options(window)
    window.mainloop()


if __name__ == '__main__':
    main()