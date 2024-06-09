"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter


class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()



        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.input_entry = tk.Entry(self, bg='black',
                              fg='white', font=('arial', 32, 'bold'), relief='solid')
        self.input_entry.place(relx=0.0, rely=0.4, relwidth=0.4, relheight=0.2)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.button = tk.Button(self, text='Translate', fg='blue',
                                font=('courier new', 20, 'bold'))
        self.button.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2)
        self.button.bind('<ButtonPress>', self.on_button_press)
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.label = tk.Label(self, bg='black',
                              fg='white', font=('arial', 32, 'bold'), relief='solid')
        self.label.place(relx=0.6, rely=0.4, relwidth=0.4, relheight=0.2)
        self.input_entry.bind('<KeyRelease>', self.on_key_release)
        # TODO: Look at the example image () and place all the
        #  components in the same order

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released

    def on_button_press(self, event):
        print('button pressed')
        self.tt = PigLatinConverter.translate(self.input_entry.get())
        self.label.config(text=self.tt)


    def on_key_release(self, event):
        pass


        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry


if __name__ == '__main__':
    
    pass
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
    plt = PigLatinTranslator()
    plt.geometry('1000x1000')
    plt.mainloop()
