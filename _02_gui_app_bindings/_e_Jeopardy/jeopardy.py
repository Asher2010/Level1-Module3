"""
 Create a _e_Jeopardy trivia game!
"""
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk


class Jeopardy(tk.Tk):

    def __init__(self, categories):
        super().__init__()

        button_width, button_height, num_buttons = self.setup_buttons(categories)

        # TODO: Create a member variable for the list of categories
        self.categories = categories
        # TODO: Create a member variable for the score/money
        self.score = 0
        for i in range(num_buttons):
            row_num = int(i / len(categories))
            col_num = int(i % len(categories))
            row_y = row_num * button_height
            col_x = col_num * button_width
            category = self.categories[col_num]

            # Create the category header and buttons where
            # row 0 is the category title
            if row_num == 0:
                pass
                # TODO: To get the category name, use the categories member variable and column num

                # TODO: Place the Label using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables
                self.label = tk.Label(self, bg='black',
                                      fg='white', font=('arial', 32, 'bold'), relief='solid', text=category.name)
                self.label.place(x=col_x, y=row_y, width=button_width, height=button_height)
            elif len(category.questions) > row_num - 1:
                value = category.questions[row_num - 1].value

                # TODO: Create a tk.Button with the questions' value on the button
                self.button = tk.Button(self, fg='blue',
                                        font=('courier new', 20, 'bold'), text=value)
                self.button.place(x=col_x, y=row_y, width=button_width, height=button_height)
                # TODO: Place the Button using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables

                # TODO: Call the button's bind() method so the
                #  on_button_press() method is called when a mouse button is pressed
                #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)
                self.button.bind('<ButtonPress>', self.on_button_press)
                # TODO: Add the button to the category's list of buttons
                category.buttons.append(self.button)

    def on_button_press(self, event):
        button_pressed = event.widget
        print('button ' + repr(button_pressed) + ' clicked!')

        # TODO: Call the ask_question() method with button_pressed as an input
        self.ask_question(button_pressed)

    def ask_question(self, button_pressed):
        for category in self.categories:
            for i, button in enumerate(category.buttons):
                if button == button_pressed:
                    if category.questions[i].has_been_asked is False:
                        category.questions[i].has_been_asked = True
                        question = category.questions[i].question
                        answer = category.questions[i].answer
                        value = category.questions[i].value

                        # TODO: At this point the question corresponding to the button is found
                        #  Use the 'question', 'answer', and 'value' variables to ask the user
                        #  the question and get their response. If their response is correct,
                        #  increase the score member variable by the value. Otherwise, subtract
                        #  value from the score
                        response = simpledialog.askstring(title="Video Games", prompt=question)
                        if response == answer:
                            self.score += value
                        else:
                            self.score -= value



    def setup_buttons(self, categories):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        # Get category with the max num of questions to determine the
        # total number of buttons to create
        questions_per_category = 0
        for category in categories:
            if len(category.questions) > questions_per_category:
                questions_per_category = len(category.questions)

        # +1 for the category title
        num_rows = questions_per_category + 1
        num_buttons = len(categories) * num_rows

        button_width = int(self.winfo_width() / len(categories))
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height, num_buttons


class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.questions = list()
        self.buttons = list()

    def add_question(self, question, answer, value):
        new_question = Category.Question(question, answer, value)
        self.questions.append(new_question)

    class Question:
        def __init__(self, question, answer, value):
            self.has_been_asked = False
            self.question = question
            self.answer = answer
            self.value = value


if __name__ == '__main__':
    video_games = Category("Video Games")
    science = Category("Science")
    math = Category("Math")
    j_categories = [video_games, science, math]

    # TODO: Use the Category class above to create at least 3 question categories
    #  for your _e_Jeopardy game



    # TODO: For each Category, use the add_question method to add a question, answer, and
    #  a value for each question

    video_games.add_question("What was the first video game?", "Tennis for two", 100)
    science.add_question("Do identical twins have the same fingerprints", "No", 100)
    math.add_question("What do the addition of the numbers on the opposite sides of dice add up to?", "7", 100)
    video_games.add_question("What job did Mario originally have?", "A Carpenter", 200)
    science.add_question("How old can Great White Sharks live for?", "50 years", 200)
    math.add_question("What is 111,111,111 * 111,111,111?", "12,345,678,987,654,321", 200)
    video_games.add_question("What is the most popular video game?", "Minecraft", 300)
    science.add_question("What do lizards use to smell?", "Their tongues", 300)
    math.add_question("What is 1,089 * 9", "9,801", 300)

    game = Jeopardy(j_categories)
    game.title('_e_Jeopardy')
    game.mainloop()
