# Caleb Stanton and Matt Rieckenberg
# Political Compass for 2021

import tkinter as tk
from tkinter import ttk

# from tkinter.messagebox import showinfo


Negative = -1
Positive = +1


class Question:
    def __init__(self, number, text, axis, polarity):
        self.text = text
        self.number = number
        self.axis = axis
        self.polarity = polarity

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text

    def getAxis(self):
        return self.axis

    def getPolarity(self):
        return self.polarity


Q1 = Question(1, "Citizens of a nation should hold the right to bear arms", "state", Negative)

Q2 = Question(2, "Recreational drugs and alcohol should be decriminalized", "state", Negative)

Q3 = Question(3,
              "My government should restrict immigration or miscegenation to preserve the cultural character of my nation",
              "state", Positive)

Sample = [Q1, Q2, Q3]


class OpeningWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Political Compass Test 2021')
        self.geometry('5000x500')
        self.configure(bg="green")

        # labels
        self.welcomeLabel1 = ttk.Label(self, text='Welcome to the Political Compass Test for 2021')
        self.welcomeLabel1.pack()
        self.welcomeLabel2 = ttk.Label(self,
                                       text='This test is a new and improved version of the popular political compass test which has become the subject of a lot of memes')
        self.welcomeLabel2.pack()

        # button
        self.button = ttk.Button(self, text='Start test')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        print("Starting the quiz")
        self.destroy()
        app = QuestionWindow()


class QuestionWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        index = 0

        # configure the question window
        self.title('Questions')
        self.geometry('5000x500')
        self.configure(bg="blue")

        # labels
        self.questionLabel = ttk.Label(self, text=Sample[index].getText())
        self.questionLabel.pack()

        def stronglyAgree_onClick():
            print("Strongly Agree clicked")
            self.destroy()
            app = LastQuestionWindow()


        def moderatelyAgree_onClick():
            print("Moderately Agree clicked")
            self.destroy()
            app = LastQuestionWindow()

        def moderatelyDisagree_onClick():
            print("Moderately Disagree clicked")
            self.destroy()
            app = LastQuestionWindow()

        def stronglyDisagree_onClick():
            print("Strongly Disagree clicked")
            self.destroy()
            app = LastQuestionWindow()

        # Option buttons
        self.stronglyAgree = ttk.Button(self, text="Strongly Agree", command=stronglyAgree_onClick).pack()
        self.moderatelyAgree = ttk.Button(self, text="Moderately Agree", command=moderatelyAgree_onClick).pack()
        self.moderatelyDisagree = ttk.Button(self, text="Moderately Disagree",
                                             command=moderatelyDisagree_onClick).pack()
        self.stronglyDisagree = ttk.Button(self, text="Strongly Disagree", command=stronglyDisagree_onClick).pack()


class LastQuestionWindow(QuestionWindow):
    pass

    # Should inherit or extend the QuestionWindow class
    # On the last question, the command should take it to the results page


class ResultsWindow(tk.Tk):
    pass  # fill this in once the question windows are sorted out
    # Should display the compass, scales to show the different results and a button to export the results
    # to a .txt file


if __name__ == "__main__":

    # Test print
    print("There are "+str(len(Sample))+" questions")
    print("-------------------------------------")


    for x in Sample:
        print("Question number " + str(x.getNumber()))
        print("The question is " + x.getText())
        print("Its polarity is " + str(x.getPolarity()))
        print("Its axis is " + x.getAxis())
        print("-------------------------------------")





    app = OpeningWindow()
    app.mainloop()
