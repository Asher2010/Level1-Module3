"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
import random

# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class TypingTutor(tk.Tk):


    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize a member variable to hold a
        #  random letter to type

        self.letter = generate_random_letter()

        # TODO: Declare and initialize a label (tk.Label) and set the text to the random letter

        self.label = tk.Label(self, text=self.letter, bg='green', font=('Rockwell', 20, 'normal', 'underline'))
        self.label.focus_set()
        self.label.bind('<KeyRelease>', self.on_key_release)
        self.label.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
        # TODO: Place the label in the center of the window

        # TODO: Call the label's focus_set() method so key presses can be detected

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released



    def on_key_release(self, event):
        letter_pressed = event.char
        print('key ' + letter_pressed + ' released!')

        # TODO: If the user pressed the correct key,
        #         change the label's background to green
        #       If the user pressed the wrong key,
        #         change the label's background to red
        #  example: self.label.configure(bg='green')
        if letter_pressed == self.letter:
            self.label.configure(bg='green')

        else:
            self.label.configure(bg='red')
        # TODO: Get a new random letter and place it on the label
        #  example: self.label.configure(text=self.rand_letter)
        self.letter = generate_random_letter()
        self.label.configure(text=self.letter)

if __name__ == '__main__':
    pass
    # TODO: Create a new _b_TypingTutor object and set the title and geometry.
    #  Remember to call mainloop() at the end
    typing_tutor = TypingTutor()
    typing_tutor.geometry()
    typing_tutor.mainloop()
