import tkinter.messagebox
from tkinter import *


class Triangle:
    """
    A class representing details for a triangle object.
    """
    def __init__(self, window):
        """
        Constructor that creates frames, labels, error box, entry for base and height of the triangle
        and a button to calculate area of a triangle for triangle object.
        :param window: takes the window that is made with tkinter.
        """
        self.window = window
        self.frame_triangle_text = Frame(self.window)
        self.label_triangle_text = Label(self.frame_triangle_text, text='Area of Triangle', font=('Arial', 13, 'bold'))
        self.label_triangle_text.pack()
        self.frame_triangle_text.pack()

        self.frame_triangle_base = Frame(self.window)
        self.label_triangle_base = Label(self.frame_triangle_base, text='Enter the base')
        self.entry_triangle_base = Entry(self.frame_triangle_base)
        self.label_triangle_base.pack(padx=3, side='left')
        self.entry_triangle_base.pack(padx=9, side='left')
        self.frame_triangle_base.pack(anchor='w', pady=10)

        self.frame_triangle_height = Frame(self.window)
        self.label_triangle_height = Label(self.frame_triangle_height, text='Enter the height')
        self.entry_triangle_height = Entry(self.frame_triangle_height)
        self.label_triangle_height.pack(padx=3, side='left')
        self.entry_triangle_height.pack(padx=0, side='left')
        self.frame_triangle_height.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='Calculate', command=self.triangle_area)
        self.button_calculate.pack()
        self.frame_button.pack()

        self.frame_triangle_area = Frame(self.window)
        self.label_triangle_area = Label(self.frame_triangle_area)
        self.label_triangle_area.pack(padx=5, side='left')
        self.frame_triangle_area.pack(anchor='w', pady=10)

        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='')
        self.label_error.pack(padx=5, side='left')
        self.frame_error.pack(anchor='w', pady=10)

    def triangle_area(self):
        """
        Method for calculating area of a triangle and handling exceptions along with
        displaying the result.
        """
        base = self.entry_triangle_base.get()
        height = self.entry_triangle_height.get()

        try:
            base = float(base)
            height = float(height)
            triangle = (1/2) * base * height
            triangle_area = f'Area of Triangle is: {triangle:.2f}'
            self.entry_triangle_base.delete(0, END)
            self.entry_triangle_height.delete(0, END)
            if base <= 0 or height <= 0:
                tkinter.messagebox.showwarning('Not Positive', 'Enter value greater than 0.')
                self.entry_triangle_base.delete(0, END)
                self.entry_triangle_height.delete(0, END)
            else:
                self.label_triangle_area.config(text=triangle_area)

        except ValueError:
            tkinter.messagebox.showwarning('Value Error', 'Enter numeric input only.')
            self.entry_triangle_base.delete(0, END)
            self.entry_triangle_height.delete(0, END)
