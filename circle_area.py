import math
import tkinter.messagebox
from tkinter import *


class Circle:
    """
    A class representing details for a Circle object.
    """
    def __init__(self, window):
        """
        Constructor that creates frames, labels, error box, entry for radius of the circle
        and a button to calculate area of a circle for Circle object.
        :param window: takes the window that is made with tkinter.
        """
        self.window = window
        self.frame_circle_text = Frame(self.window)
        self.label_circle_text = Label(self.frame_circle_text, text='Area Of Circle', font=('Arial', 13, 'bold'))
        self.label_circle_text.pack()
        self.frame_circle_text.pack()

        self.frame_radius = Frame(self.window)
        self.label_radius = Label(self.frame_radius, text='Enter radius')
        self.entry_radius = Entry(self.frame_radius)
        self.label_radius.pack(padx=5, side='left')
        self.entry_radius.pack(padx=5, side='left')
        self.frame_radius.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='Calculate', command=self.circle_area)
        self.button_calculate.pack()
        self.frame_button.pack()

        self.frame_circle_area = Frame(self.window)
        self.label_circle_area = Label(self.frame_circle_area)
        self.label_circle_area.pack(padx=5, side='left')
        self.frame_circle_area.pack(anchor='w', pady=10)

        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='')
        self.label_error.pack(padx=5, side='left')
        self.frame_error.pack(anchor='w', pady=10)

    def circle_area(self):
        """
        Method for calculating area of a circle and handling exceptions along with
        displaying the result.
        """
        radius = self.entry_radius.get()
        try:
            radius = 2 * math.pi * float(radius)
            circle_area = f'Area of the circle is: {radius:.2f}'
            self.entry_radius.delete(0, END)
            if radius <= 0:
                tkinter.messagebox.showwarning('Not Positive', 'Value must be greater than 0.')
                self.entry_radius.delete(0, END)
            else:
                self.label_circle_area.config(text=circle_area)

        except ValueError:
            tkinter.messagebox.showwarning('Value Error', 'Enter numeric input only.')
            self.entry_radius.delete(0, END)
