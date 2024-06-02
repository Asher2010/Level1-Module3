"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = ''
        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.entry = tk.Entry(self, textvariable=self.text, bg='yellow',
                              fg='blue', font=('arial', 32, 'bold'), relief='solid')
        self.entry.place(relx=0.0, rely=0.5, relwidth=0.4, relheight=0.3)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.button = tk.Button(self, text='Translate', fg='blue',
                                font=('courier new', 20, 'bold'))
        self.button.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.3)
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.label = tk.Label(self, text=self.text, bg='yellow',
                              fg='blue', font=('arial', 32, 'bold'), relief='solid')
        self.label.place(relx=0.6, rely=0.5, relwidth=0.4, relheight=0.3)
        self.label.bind('<KeyRelease>', self.on_key_release)
        # TODO: Look at the example image () and place all the
        #  components in the same order

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released

    def on_key_release(self, event):

    #def on_key_press(self, event):
        print('button pressed!')

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry
        self.tt = self.text.translate()

if __name__ == '__main__':
    pass
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
    plt = PigLatinTranslator()
    plt.geometry('1000x1000')
    plt.mainloop()
