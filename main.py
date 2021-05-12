# Caleb Stanton and Matt Rieckenberg
# Political Compass for 2021

import tkinter as tk
from tkinter import ttk
import datetime

# from tkinter.messagebox import showinfo

# Constants
N = -1
P = +1

x = datetime.datetime.now()

currentDate = x.strftime("%A")+", "+x.strftime("%B")+" "+x.strftime("%d")+", "+x.strftime("%Y")
#print(currentDate)


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

    def isPositive(self):
        if (self.getPolarity() == P):
            # print("Positive polarity")
            return True
        else:
            # print("Negative polarity")
            return False


# State Axis Questions

Q1 = Question(1, "Citizens of a nation should hold the right to bear arms", "state", N)

Q2 = Question(2, "Recreational drugs and alcohol should be decriminalized", "state", N)

Q3 = Question(3,
              "My government should restrict immigration or miscegenation to preserve the cultural character of my nation",
              "state", P)

Q4 = Question(4, "Mask mandates and lockdowns are needed to prevent the spread of disease", "state", P)

Q5 = Question(5, "To become a truly free country, police departments need to be reformed or demilitarized", "state", N)

Q6 = Question(6, "Transgenderism should be treated as a mental illness", "state", P)

Q7 = Question(7, "Meat and dairy products need to be limited to combat the climate emergency", "state", P)

Q8 = Question(8, "Sometimes violence is unavoidable in advancing the interests of my political cause", "state", P)

Q9 = Question(9, "I believe in freedom of speech even for those who’s views I despise most", "state", N)

Q10 = Question(10,
               "The primary aim of the justice system is protection of the innocent, not rehabilitation of the guilty",
               "state", P)

Q11 = Question(11, "Government has no business in the bedrooms of the nation", "state", N)

Q12 = Question(12, "Religious practices should be taught in school and enforced by the state", "state", P)

Q13 = Question(13, "Every company should be required to have at least one woman on its board", "state", P)

Q14 = Question(14, "Sexwork should be bought and sold as a commodity", "state", N)

Q15 = Question(15, "Security from criminals and terrorists is more precious than personal privacy", "state", P)

Q16 = Question(16, "A baker has no obligation to make a cake for a gay wedding", "state", N)

# Economic Axis Questions

Q17 = Question(17, "Nuclear power is a safe, viable source of energy", "econ", P)

Q18 = Question(18, "Increasing regulations on fossil fuels will have ambiguous benefits and cripple the economy",
               "econ", P)

Q19 = Question(6, "The industrial revolution and it’s consequences have been a disaster for the human race", "econ", N)

Q20 = Question(20, "Single payer healthcare is preferable to a privatized system", "econ", N)

Q21 = Question(21, "Free trade and globalization have been our greatest allies in alleviating poverty", "econ", P)

Q22 = Question(21, "A state-planned economy cannot scale to the efficiency or complexity of the free market", "econ", P)

Q23 = Question(23, "Deficit spending is necessary to rebuild our public infrastructure", "econ", N)

Q24 = Question(24, "Water should be a public resource that anyone can access freely", "econ", N)

Q25 = Question(25, "Education would be much more effective if school choice was left to the parents", "econ", P)

Q26 = Question(26, "We lose more in taxes than government could ever give back", "econ", P)

Q27 = Question(27, "Industry should be democratically owned and controlled by labour unions", "econ", N)

Q28 = Question(28, "Raising the minimum wage will not help the working class", "econ", P)

Q29 = Question(29, "Helping the unemployed is of greater urgency than slowing down inflation", "econ", N)

Q30 = Question(30, "Precious metals and cryptocurrencies are more trustworthy than federal banking systems", "econ", P)

Q31 = Question(31, "I support regulations enforcing net neutrality", "econ", N)

Q32 = Question(32,
               "The military, courts and police could be replaced with voluntary legal agreements and private protection agencies",
               "econ", P)

Q33 = Question(33, "It’s a tragedy that art and culture are commodified and cheapened by the capitalist system", "econ",
               N)

Q34 = Question(34, "Affordable housing programs to little except destroy property values", "econ", P)

Q35 = Question(35, "A federal jobs initiative is an excellent remedy to economic downturns", "econ", N)

Q36 = Question(36, "Economic growth without equality is an injustice", "econ", N)


# Foreign Policy Axis --- Positive means isolationist, negative means internationalist

Q37 = Question(37, "My country should spread its values around the world, even if it requires military forces","foreign",N)

Q38 = Question(38,"NATO membership is beneficial to my country","foreign",N)

Q39 = Question(39,"Russian aggression is one of the most serious geopolitical threats today","foreign",N)

Q40 = Question(40,"My country should seek to have better relations with Russia","foreign",P)

Q41 = Question(41,"My country should seek to solve its own internal problems before worrying about the rest of the world","foreign",P)

Q42 = Question(42,"Free trade is beneficial to my country","foreign",N)

Q43 = Question(43,"War is ultimately harmful to my country and it should be only used as a defensive measure","foreign",P)

Q44 = Question(44,"The war in Afghanistan is pointless and should be ended soon","foreign",P)

Q45 = Question(45,"The Iraq War was a mistake","foreign",P)

Q46 = Question(46,"NATO’s campaigns in Serbia and Libya benefitted the world by removing dictators","foreign",N)

Q47 = Question(47,"Supranational organizations like the European Union are beneficial","foreign",N)

Q48 = Question(48,"My country has an important obligation to support the State of Israel","foreign",N)

Q49 = Question(49,"My country should support opposition groups to dictators","foreign",N)


# Cultural Axis --- Positive means tradition, negative means progress

Q50 = Question(50,"Things were better in the past","cultural",P)

Q51 = Question(51,"Jazz music is degenerate and an example of the corruption of traditional culture","cultural",P)

Q52 = Question(52,"Modern art is an example of our cultural decay","cultural",P)

Q53 = Question(53,"There are foreign and subversive elements in positions of power that are corrupting our culture","cultural",P)

Q54 = Question(54,"Immigration is a net positive to my country","cultural",N)

Q55 = Question(55,"Multiculturalism is an important value for my country to have","cultural",N)

Q56 = Question(56,"Tradition is silly since it refuses to move on and look to the future","cultural",N)

Q57 = Question(57,"I do not enjoy our current popular culture","cultural",P)


# Question Lists

# stateAxis = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16]

# econAxis  = [Q17,Q18,Q19,Q20,Q21,Q22,Q23,Q24,Q25,Q26,Q27,Q28,Q29,Q30,Q31,Q32,Q33,Q34,Q35,Q36]

class Score:
    myName = ""
    StateScore = 0
    EconScore = 0
    ForeignScore = 0
    CulturalScore = 0

# Test Questions
stateAxis = [Q1, Q2]
econAxis = [Q17, Q18]
foreignAxis = [Q48,Q49]
cultureAxis = [Q56,Q57]


class OpeningWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Political Compass Test 2021')
        self.geometry('1000x500')
        self.configure(bg="green")

        # labels
        self.welcomeLabel1 = ttk.Label(self, text='Welcome to the Political Compass Test for 2021')
        self.welcomeLabel1.pack()
        self.welcomeLabel2 = ttk.Label(self,
                                       text='This test is a new and improved version of the popular political compass test which has become the subject of a lot of memes')
        self.welcomeLabel2.pack()



        # Name textbox
        self.nameEntryBox = tk.Entry(self,justify='center')
        self.nameEntryBox.pack()



        # Button
        self.button = ttk.Button(self, text='Start test')
        self.button['command'] = self.button_clicked
        self.button.pack()


        # Date Label
        self.DateLabel = ttk.Label(self, text=currentDate).pack()

    def button_clicked(self):

        print("Starting the quiz")
        Score.myName = self.nameEntryBox.get()
        print("Name is "+self.nameEntryBox.get())
        self.destroy()






class StateQuestionWindow(tk.Tk, Question, Score):
    def __init__(self, question):
        super().__init__()
        self.question = question

        # configure the question window
        self.title('State Axis Questions')
        self.geometry('1000x500')
        self.configure(bg="blue")

        # labels
        self.questionLabel = ttk.Label(self, text=question.getText())
        self.questionLabel.pack()

        def stronglyAgree_onClick():
            # print("Strongly Agree clicked")
            self.destroy()
            if (question.isPositive() == True):
                Score.StateScore += 3
                print("My current State Score is " + str(Score.StateScore))
            else:
                Score.StateScore += -2
                print("My current State Score is " + str(Score.StateScore))

        def moderatelyAgree_onClick():
            # print("Moderately Agree clicked")
            self.destroy()
            if (question.isPositive() == True):
                Score.StateScore += 2
                print("My current State Score is " + str(Score.StateScore))
            else:
                Score.StateScore += -1
                print("My current State Score is " + str(Score.StateScore))

        def moderatelyDisagree_onClick():
            # print("Moderately Disagree clicked")
            self.destroy()
            if (question.isPositive() == True):
                Score.StateScore += -1
                print("My current State Score is " + str(Score.StateScore))
            else:
                Score.StateScore += 2
                print("My current State Score is " + str(Score.StateScore))

        def stronglyDisagree_onClick():
            # print("Strongly Disagree clicked")
            self.destroy()
            if (question.isPositive() == True):
                Score.StateScore += -2
                print("My current State Score is " + str(Score.StateScore))
            else:
                Score.StateScore += 3
                print("My current State Score is " + str(Score.StateScore))

        # Option buttons
        self.stronglyAgree = ttk.Button(self, text="Strongly Agree", command=stronglyAgree_onClick).pack()
        self.moderatelyAgree = ttk.Button(self, text="Moderately Agree", command=moderatelyAgree_onClick).pack()
        self.moderatelyDisagree = ttk.Button(self, text="Moderately Disagree",
                                             command=moderatelyDisagree_onClick).pack()
        self.stronglyDisagree = ttk.Button(self, text="Strongly Disagree", command=stronglyDisagree_onClick).pack()


class EconQuestionWindow(tk.Tk, Question, Score):
    def __init__(self, question):
        super().__init__()
        self.question = question

        # configure the question window
        self.title('Economic Axis Questions')
        self.geometry('1000x500')
        self.configure(bg="purple")

        # Labels
        self.questionLabel = ttk.Label(self, text=question.getText())
        self.questionLabel.pack()

        def stronglyAgree_onClick():
            # print("Strongly Agree clicked")
            self.destroy()
            if question.number == 32:
                Score.EconScore += 7
                print("My current Economic Score is " + str(Score.EconScore))
            if question.number == 27:
                Score.EconScore += -7
                print("My current Economic Score is " + str(Score.EconScore))
            elif (question.isPositive() == True):
                Score.EconScore += 2
                print("My current Economic Score is " + str(Score.EconScore))
            else:
                Score.EconScore += -2
                print("My current Economic Score is " + str(Score.EconScore))

        def moderatelyAgree_onClick():
            # print("Moderately Agree clicked")
            self.destroy()
            if question.number == 32:
                Score.EconScore += 4
                print("My current Economic Score is " + str(Score.EconScore))
            elif question.number == 27:
                Score.EconScore += -4
                print("My current Economic Score is " + str(Score.EconScore))
            elif (question.isPositive() == True):
                Score.EconScore += 1
                print("My current Economic Score is " + str(Score.EconScore))
            else:
                Score.EconScore += -1
                print("My current Economic Score is " + str(Score.EconScore))

        def moderatelyDisagree_onClick():
            # print("Moderately Disagree clicked")
            self.destroy()
            if question.number == 32:
                Score.EconScore += -1
                print("My current Economic Score is " + str(Score.EconScore))
            elif question.number == 27:
                Score.EconScore += 1
                print("My current Economic Score is " + str(Score.EconScore))
            elif (question.isPositive() == True):
                Score.EconScore += -1
                print("My current Economic Score is " + str(Score.EconScore))
            else:
                Score.EconScore += 1
                print("My current Economic Score is " + str(Score.EconScore))

        def stronglyDisagree_onClick():
            # print("Strongly Disagree clicked")
            self.destroy()
            if question.number == 32:
                Score.EconScore += -2
                print("My current Economic Score is " + str(Score.EconScore))
            elif question.number == 27:
                Score.EconScore += 2
                print("My current Economic Score is " + str(Score.EconScore))
            elif (question.isPositive() == True):
                Score.EconScore += -2
                print("My current Economic Score is " + str(Score.EconScore))
            else:
                Score.EconScore += 2
                print("My current Economic Score is " + str(Score.EconScore))

        # Option buttons
        self.stronglyAgree = ttk.Button(self, text="Strongly Agree", command=stronglyAgree_onClick).pack()
        self.moderatelyAgree = ttk.Button(self, text="Moderately Agree", command=moderatelyAgree_onClick).pack()
        self.moderatelyDisagree = ttk.Button(self, text="Moderately Disagree",
                                             command=moderatelyDisagree_onClick).pack()
        self.stronglyDisagree = ttk.Button(self, text="Strongly Disagree", command=stronglyDisagree_onClick).pack()

class ForeignPolicyQuestionWindow(tk.Tk, Question, Score):
    def __init__(self, question):
        super().__init__()
        self.question = question

        # configure the question window
        self.title('Foreign Policy Axis Questions')
        self.geometry('1000x500')
        self.configure(bg="pink")

        # Labels
        self.questionLabel = ttk.Label(self, text=question.getText())
        self.questionLabel.pack()

        # Change this -----------------------------------------------------------------------------------------------
        def stronglyAgree_onClick():
            # print("Strongly Agree clicked")
            self.destroy()
            if question.number == 32:
                Score.ForeignScore += 7
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            if question.number == 27:
                Score.ForeignScore += -7
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif (question.isPositive() == True):
                Score.ForeignScore += 2
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            else:
                Score.ForeignScore += -2
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))

        def moderatelyAgree_onClick():
            # print("Moderately Agree clicked")
            self.destroy()
            if question.number == 32:
                Score.ForeignScore += 4
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif question.number == 27:
                Score.ForeignScore += -4
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif (question.isPositive() == True):
                Score.ForeignScore += 1
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            else:
                Score.ForeignScore += -1
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))

        def moderatelyDisagree_onClick():
            # print("Moderately Disagree clicked")
            self.destroy()
            if question.number == 32:
                Score.ForeignScore += -1
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif question.number == 27:
                Score.ForeignScore += 1
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif (question.isPositive() == True):
                Score.ForeignScore += -1
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            else:
                Score.ForeignScore += 1
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))

        def stronglyDisagree_onClick():
            # print("Strongly Disagree clicked")
            self.destroy()
            if question.number == 32:
                Score.ForeignScore += -2
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif question.number == 27:
                Score.ForeignScore += 2
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            elif (question.isPositive() == True):
                Score.ForeignScore += -2
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))
            else:
                Score.ForeignScore += 2
                print("My current Foreign Policy Score is " + str(Score.ForeignScore))

        # -----------------------------------------------------------------------------------------------

        # Option buttons
        self.stronglyAgree = ttk.Button(self, text="Strongly Agree", command=stronglyAgree_onClick).pack()
        self.moderatelyAgree = ttk.Button(self, text="Moderately Agree", command=moderatelyAgree_onClick).pack()
        self.moderatelyDisagree = ttk.Button(self, text="Moderately Disagree",
                                             command=moderatelyDisagree_onClick).pack()
        self.stronglyDisagree = ttk.Button(self, text="Strongly Disagree", command=stronglyDisagree_onClick).pack()


class CulturalAxisQuestionWindow(tk.Tk, Question, Score):
    def __init__(self, question):
        super().__init__()
        self.question = question

        # configure the question window
        self.title('Cultural Axis Questions')
        self.geometry('1000x500')
        self.configure(bg="brown")

        # Labels
        self.questionLabel = ttk.Label(self, text=question.getText())
        self.questionLabel.pack()

        # Change this -----------------------------------------------------------------------------------------------
        def stronglyAgree_onClick():
            # print("Strongly Agree clicked")
            self.destroy()
            if question.number == 32:
                Score.CulturalScore += 7
                print("My current Cultural Score is " + str(Score.CulturalScore))
            if question.number == 27:
                Score.CulturalScore += -7
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif (question.isPositive() == True):
                Score.CulturalScore += 2
                print("My current Cultural Score is " + str(Score.CulturalScore))
            else:
                Score.CulturalScore += -2
                print("My current Cultural Score is " + str(Score.CulturalScore))

        def moderatelyAgree_onClick():
            # print("Moderately Agree clicked")
            self.destroy()
            if question.number == 32:
                Score.CulturalScore += 4
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif question.number == 27:
                Score.CulturalScore += -4
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif (question.isPositive() == True):
                Score.CulturalScore += 1
                print("My current Cultural Score is " + str(Score.CulturalScore))
            else:
                Score.CulturalScore += -1
                print("My current Cultural Score is " + str(Score.CulturalScore))

        def moderatelyDisagree_onClick():
            # print("Moderately Disagree clicked")
            self.destroy()
            if question.number == 32:
                Score.CulturalScore += -1
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif question.number == 27:
                Score.CulturalScore += 1
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif (question.isPositive() == True):
                Score.CulturalScore += -1
                print("My current Cultural Score is " + str(Score.CulturalScore))
            else:
                Score.CulturalScore += 1
                print("My current Cultural Score is " + str(Score.CulturalScore))

        def stronglyDisagree_onClick():
            # print("Strongly Disagree clicked")
            self.destroy()
            if question.number == 32:
                Score.CulturalScore += -2
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif question.number == 27:
                Score.CulturalScore += 2
                print("My current Cultural Score is " + str(Score.CulturalScore))
            elif (question.isPositive() == True):
                Score.CulturalScore += -2
                print("My current Cultural Score is " + str(Score.CulturalScore))
            else:
                Score.CulturalScore += 2
                print("My current Cultural Score is " + str(Score.CulturalScore))

        # -----------------------------------------------------------------------------------------------

        # Option buttons
        self.stronglyAgree = ttk.Button(self, text="Strongly Agree", command=stronglyAgree_onClick).pack()
        self.moderatelyAgree = ttk.Button(self, text="Moderately Agree", command=moderatelyAgree_onClick).pack()
        self.moderatelyDisagree = ttk.Button(self, text="Moderately Disagree",
                                             command=moderatelyDisagree_onClick).pack()
        self.stronglyDisagree = ttk.Button(self, text="Strongly Disagree", command=stronglyDisagree_onClick).pack()



class LastQuestionWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="orange")
        self.geometry('1000x500')
        self.title("The quiz is now complete!")

        def finishQuiz_onClick():
            print("Quiz completed")
            #print("My final State Axis Score is " + str(Score.StateScore))
            #print("My final Economic Axis Score is " + str(Score.EconScore))
            #print("My final Foreign Policy Axis Score is " + str(Score.ForeignScore))
            #print("My final Cultural Axis Score is " + str(Score.CulturalScore))
            self.destroy()


        self.finishQuizButton = ttk.Button(text="Finish quiz and see results", command=finishQuiz_onClick).pack()

    # Should inherit or extend the QuestionWindow class
    # On the last question, the command should take it to the results page


class ResultsWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="red")
        self.geometry('1000x500')
        self.title("Here are your results!")

        self.StateAxisLabel = ttk.Label(self,text="My final State Axis Score is " + str(Score.StateScore)).pack()
        self.EconomicAxisLabel = ttk.Label(self,text="My final Economic Axis Score is " + str(Score.EconScore)).pack()
        self.ForeignAxisLabel = ttk.Label(self,text="My final Foreign Policy Axis Score is " + str(Score.ForeignScore)).pack()
        self.CulturalAxisLabel = ttk.Label(self,text="My final Cultural Axis Score is " + str(Score.CulturalScore)).pack()

        def exportToTextFile():
            f = open("my_results.txt", "w")
            f.write("Results for " +Score.myName+" on "+currentDate+'\n')
            f.write('\n')
            f.write("Your final State Axis Score is " + str(Score.StateScore)+'\n')
            f.write("Your final Economic Axis Score is " + str(Score.EconScore)+'\n')
            f.write("Your final Foreign Policy Axis Score is " + str(Score.ForeignScore)+'\n')
            f.write("Your final Cultural Axis Score is " + str(Score.CulturalScore)+'\n')
            f.close()

        self.ExportTextButton = ttk.Button(self,text="Export to a text file",command=exportToTextFile).pack()






if __name__ == "__main__":

    # Test print
    # print("There are "+str(len(Sample))+" questions")
    # print("-------------------------------------")
    # for x in Sample:
    # print("Question number " + str(x.getNumber()))
    # print(x.getText())
    # print("Its polarity is " + str(x.getPolarity()))
    # print("Its axis is " + x.getAxis())
    # print("-------------------------------------")

    app = OpeningWindow()
    app.mainloop()

    for i in range(len(stateAxis)):
        app = StateQuestionWindow(stateAxis[i])
        app.mainloop()

    for j in range(len(econAxis)):
        app = EconQuestionWindow(econAxis[j])
        app.mainloop()

    for l in range(len(foreignAxis)):
        app = ForeignPolicyQuestionWindow(foreignAxis[l])
        app.mainloop()

    for m in range(len(cultureAxis)):
        app = CulturalAxisQuestionWindow(cultureAxis[m])
        app.mainloop()

    app = LastQuestionWindow()
    app.mainloop()

    app = ResultsWindow()
    app.mainloop()
