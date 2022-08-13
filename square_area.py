import tkinter.messagebox
from tkinter import *


class Square:
    """
    A class representing details for a Square object.
    """
    def __init__(self, window):
        """
        Constructor that creates frames, labels, error box, entry for length of the square
        and a button to calculate area of a square for Square object.
        :param window: takes the window that is made with tkinter.
        """
        self.window = window
        self.frame_square_text = Frame(self.window)
        self.label_square_text = Label(self.frame_square_text, text='Area of Square', font=('Arial', 13, 'bold'))
        self.label_square_text.pack()
        self.frame_square_text.pack()

        self.frame_square_length = Frame(self.window)
        self.label_length = Label(self.frame_square_length, text='Enter length of square')
        self.entry_square_length = Entry(self.frame_square_length)
        self.label_length.pack(padx=5, side='left')
        self.entry_square_length.pack(padx=5, side='left')
        self.frame_square_length.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='Calculate', command=self.square_area)
        self.button_calculate.pack()
        self.frame_button.pack()

        self.frame_square_area = Frame(self.window)
        self.label_square_area = Label(self.frame_square_area)
        self.label_square_area.pack(padx=5, side='left')
        self.frame_square_area.pack(anchor='w', pady=10)

        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='')
        self.label_error.pack(padx=5, side='left')
        self.frame_error.pack(anchor='w', pady=10)

    def square_area(self):
        """
        Method for calculating area of a square and handling exceptions along with
        displaying the result.
        """
        square_length = self.entry_square_length.get()
        try:
            square_length = float(square_length) ** 2
            square_area = f'Area is: {square_length:.2f}'
            self.entry_square_length.delete(0, END)
            if square_length <= 0:
                tkinter.messagebox.showwarning('Not Positive', 'Value must be greater than 0.')
                self.entry_square_length.delete(0, END)
            else:
                self.label_square_area.config(text=square_area)

        except ValueError:
            tkinter.messagebox.showwarning('Value Error', 'Enter numeric input only.')
            self.entry_square_length.delete(0, END)
