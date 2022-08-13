import tkinter.messagebox
from tkinter import *


class Rectangle:
    """
    A class representing details for a rectangle object.
    """
    def __init__(self, window):
        """
        Constructor that creates frames, labels, error box, entry for length and weidth of the rectangle
        and a button to calculate area of a rectangle for rectangle object.
        :param window: takes the window that is made with tkinter.
        """
        self.window = window
        self.frame_rectangle_text = Frame(self.window)
        self.label_rectangle_text = Label(self.frame_rectangle_text, text='Area of Rectangle',
                                          font=('Arial', 13, 'bold'))
        self.label_rectangle_text.pack()
        self.frame_rectangle_text.pack()

        self.frame_rectangle_length = Frame(self.window)
        self.label_rectangle_length = Label(self.frame_rectangle_length, text='Enter the length')
        self.entry_rectangle_length = Entry(self.frame_rectangle_length)
        self.label_rectangle_length.pack(padx=3, side='left')
        self.entry_rectangle_length.pack(padx=5, side='left')
        self.frame_rectangle_length.pack(anchor='w', pady=10)

        self.frame_rectangle_width = Frame(self.window)
        self.label_rectangle_width = Label(self.frame_rectangle_width, text='Enter the width')
        self.entry_rectangle_width = Entry(self.frame_rectangle_width)
        self.label_rectangle_width.pack(padx=5, side='left')
        self.entry_rectangle_width.pack(padx=5, side='left')
        self.frame_rectangle_width.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='Calculate', command=self.rectangle_area)
        self.button_calculate.pack()
        self.frame_button.pack()

        self.frame_rectangle_area = Frame(self.window)
        self.label_rectangle_area = Label(self.frame_rectangle_area)
        self.label_rectangle_area.pack(padx=5, side='left')
        self.frame_rectangle_area.pack(anchor='w', pady=10)

        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='')
        self.label_error.pack(padx=5, side='left')
        self.frame_error.pack(anchor='w', pady=10)

    def rectangle_area(self):
        """
        Method for calculating area of a rectangle and handling exceptions along with
        displaying the result.
        """
        lenght = self.entry_rectangle_length.get()
        width = self.entry_rectangle_width.get()
        try:
            length = float(lenght)
            width = float(width)
            rectangle = width * length
            rectangle_area = f'Area of Rectangle is: {rectangle:.2f}'
            self.entry_rectangle_length.delete(0, END)
            self.entry_rectangle_width.delete(0, END)

            if length <= 0 or width <= 0:
                tkinter.messagebox.showwarning('Not Positive', 'Enter value greater than 0.')
                self.entry_rectangle_length.delete(0, END)
                self.entry_rectangle_width.delete(0, END)
            else:
                self.label_rectangle_area.config(text=rectangle_area)

        except ValueError:
            tkinter.messagebox.showwarning('Value Error', 'Enter numeric input only.')
            self.entry_rectangle_length.delete(0, END)
            self.entry_rectangle_width.delete(0, END)
