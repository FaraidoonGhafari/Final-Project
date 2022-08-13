from circle_area import *
from square_area import *
from rectangle_area import *
from triangle_area import *
from factorial import *


class Options:
    """
    A class representing details for a options object.
    """
    def __init__(self, window):
        """
        Constructor that creates frames, labels for options and radio buttons for
        circle, square, rectangle, triangle, and factorial for Options object.
        :param window: takes the window that is made with tkinter.
        """
        self.window = window
        self.frame_options = Frame(self.window)
        self.label_options = Label(self.frame_options, text='Options', font=('Arial', 14, 'bold'), fg='gray')
        self.frame_options.pack(anchor='w', padx=80)

        self.frame_option0 = Frame(self.window)
        self.radio_0 = IntVar()
        self.radio_0.set(0)
        self.radio_circle = Radiobutton(self.frame_option0, text='Circle', variable=self.radio_0, value=1,
                                        command=self.circle)
        self.radio_rectangle = Radiobutton(self.frame_option0, text='Rectangle', variable=self.radio_0, value=2,
                                           command=self.rectangle)
        self.label_options.pack(padx=5, pady=5, side='left')
        self.radio_circle.pack(padx=30, side='left')
        self.radio_rectangle.pack(padx=15, side='left')

        self.frame_option0.pack(anchor='w', pady=0)
        self.frame_option1 = Frame(self.window)
        self.radio_square = Radiobutton(self.frame_option1, text='Square', variable=self.radio_0, value=3,
                                        command=self.square)
        self.radio_square.pack(padx=30, side='left')
        self.radio_triangle = Radiobutton(self.frame_option1, text='Triangle', variable=self.radio_0, value=4,
                                          command=self.triangle)
        self.radio_triangle.pack(padx=10, side='left')
        self.frame_option1.pack(anchor='w', pady=10)

        self.frame_option2 = Frame(self.window)
        self.radio_factorial = Radiobutton(self.frame_option2, text='Factorial', variable=self.radio_0, value=5,
                                           command=self.factorial)
        self.radio_factorial.pack(padx=30, side='left')
        self.frame_option2.pack(anchor='w', pady=3)

    def circle(self):
        """
        Create a window to calculate area of a circle and pass
        the window to the circle class.
        """
        window = Toplevel()
        window.title('Final Project')
        window.geometry('250x150')
        window.resizable(False, False)
        widgets = Circle(window)
        window.mainloop()

    def rectangle(self):
        """
        Create a window to calculate area of a rectangle and pass
        the window to the rectangle class.
        """
        window = Toplevel()
        window.title('Final Project')
        window.geometry('250x180')
        window.resizable(False, False)
        widgets = Rectangle(window)
        window.mainloop()

    def square(self):
        """
        Create a window to calculate area of a square and pass
        the window to the square class.
        """
        window = Toplevel()
        window.title('Final Project')
        window.geometry('240x150')
        window.resizable(False, False)
        widgets = Square(window)
        window.mainloop()

    def triangle(self):
        """
        Create a window to calculate area of a triangle and pass
        the window to the triangle class.
        """
        window = Toplevel()
        window.title('Final Project')
        window.geometry('250x180')
        window.resizable(False, False)
        widgets = Triangle(window)
        window.mainloop()

    def factorial(self):
        """
        Create a window to calculate factorial of a number and pass
        the window to the factorial class.
        """
        window = Toplevel()
        window.title('Final Project')
        window.geometry('250x150')
        window.resizable(False, False)
        widgets = Factorial(window)
        window.mainloop()
