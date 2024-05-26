"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.button = tk.Button(self, text='Joke', fg='black', font=('courier new', 17, 'bold'))
        self.button.place(relx=0.0, rely=.0, relwidth=.5, relheight=1)

        self.button2 = tk.Button(self, text='Punchline', fg='black', font=('courier new', 17, 'bold'))
        self.button2.place(relx=0.5, rely=.0, relwidth=.5, relheight=1)
        # TODO: Place the 2 buttons next to each other (see example image)

        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        self.button.bind('<ButtonPress>', self.on_joke)

        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        self.button2.bind('<ButtonPress>', self.on_punchline)
    def on_joke(self, event):
        print('Why did the chicken cross the road?')

        # TODO: Write your joke below!

    def on_punchline(self, event):
        print('To get to the other side')

        # TODO: Write a punchline to your joke!


if __name__ == '__main__':
    pass
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end
    chuckle_clicker = ChuckleClicker()

    chuckle_clicker.geometry()
    chuckle_clicker.mainloop()
