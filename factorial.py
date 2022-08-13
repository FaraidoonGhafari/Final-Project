import tkinter.messagebox
from tkinter import *


class Factorial:
    """
    A class representing details for a factorial object.
    """
    def __init__(self, window):
        """
        Constructor that creates frames, labels and button for the factorial object.
        :param window: check the window that is already made with tkinter
        """
        self.window = window
        self.frame_text = Frame(self.window)
        self.label_text = Label(self.frame_text, text='Factorial of a number', font=('Arial', 13, 'bold'))
        self.label_text.pack()
        self.frame_text.pack()

        self.frame_num = Frame(self.window)
        self.label_num = Label(self.frame_num, text='Enter a number')
        self.entry_num = Entry(self.frame_num)
        self.label_num.pack(padx=5, side='left')
        self.entry_num.pack(padx=5, side='left')
        self.frame_num.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='Calculate', command=self.calculate_factorial)
        self.button_calculate.pack()
        self.frame_button.pack()

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(padx=5, side='left')
        self.frame_result.pack(anchor='w', pady=10)

        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='')
        self.label_error.pack(padx=5, side='left')
        self.frame_error.pack(anchor='w', pady=10)

    def calculate_factorial(self):
        """
        Method for calculating factorial of a number and handling exceptions along with
        displaying the result.
        """
        num = self.entry_num.get()
        try:
            num = int(num)
            self.entry_num.delete(0, END)

            if num < 0:
                tkinter.messagebox.showwarning('Not Positive', 'Value must be greater than 0.')
                self.entry_num.delete(0, END)

            else:
                result = f'The factorial of {num} is: {fact(num)}'
                self.label_result.config(text=result)

        except ValueError:
            tkinter.messagebox.showwarning('Value Error', 'Enter whole number only.')
            self.entry_num.delete(0, END)


def fact(n):
    """
    Recursive function for finding factorial of a number
    :param n: a number
    :return: factorial of a number or  n * fact(n - 1)
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
