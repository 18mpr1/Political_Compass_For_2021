# Caleb Stanton and Matt Rieckenberg
# Political Compass for 2021

import tkinter as tk

def Auth(ans):
    if ans == 'a':
        return 3
    if ans == 'b':
        return 2
    if ans == 'c':
        return -1
    if ans == 'd':
        return -2


def Lib(ans):
    if ans == 'd':
        return 3
    if ans == 'c':
        return 2
    if ans == 'b':
        return -1
    if ans == 'a':
        return -2


def Left(ans):
    if ans == 'd':
        return 2
    if ans == 'c':
        return 1
    if ans == 'b':
        return -1
    if ans == 'a':
        return -2


def Right(ans):
    if ans == 'a':
        return 2
    if ans == 'b':
        return 1
    if ans == 'c':
        return -1
    if ans == 'd':
        return -2


def Socialism(ans):
    if ans == 'a':
        return -7
    if ans == 'b':
        return -4
    if ans == 'c':
        return 1
    if ans == 'd':
        return 2


def McPolice(ans):
    if ans == 'a':
        return 7
    if ans == 'b':
        return 4
    if ans == 'c':
        return -1
    if ans == 'd':
        return -2


def StateAxis():
    Score = 0
    A = "Citizens of a nation should hold the right to bear arms"
    print(A)
    a = Lib(input())
    Score += a
    B = "Recreational drugs and alcohol should be decriminalized"
    print(B)
    b = Lib(input())
    Score += b
    C = "My government should restrict immigration or miscegenation to preserve the cultural character of my nation"
    print(C)
    c = Auth(input())
    Score += c
    D = "Mask mandates and lockdowns are needed to prevent the spread of disease"
    print(D)
    d = Auth(input())
    Score += d
    E = "To become a truly free country, police departments need to be reformed or demilitarized"
    print(E)
    e = Lib(input())
    Score += e
    F = "Transgenderism should be treated as a mental illness"
    print(F)
    f = Auth(input())
    Score += f
    G = "Meat and dairy products need to be limited to combat the climate emergency"
    print(G)
    g = Auth(input())
    Score += g
    H = "Sometimes violence is unavoidable in advancing the interests of my political cause"
    print(H)
    h = Auth(input())
    Score += h
    I = "I believe in freedom of speech even for those who’s views I despise most"
    print(I)
    i = Lib(input())
    Score += i
    J = "The primary aim of the justice system is protection of the innocent, not rehabilitation of the guilty"
    print(J)
    j = Auth(input())
    Score += j
    K = "Government has no business in the bedrooms of the nation"
    print(K)
    k = Lib(input())
    Score += k
    L = "Religious practices should be taught in school and enforced by the state"
    print(L)
    l = Auth(input())
    Score += l
    M = "Every company should be required to have at least one woman on its board"
    print(M)
    m = Auth(input())
    Score += m
    N = "Sexwork should be bought and sold as a commodity"
    print(N)
    m = Lib(input())
    O = "Security from criminals and terrorists is more precious than personal privacy"
    print(O)
    o = Auth(input())
    Score += o
    P = "A baker has no obligation to make a cake for a gay wedding"
    print(P)
    p = Lib(input())
    Score += p
    print(Score)


def EconAxis():
    Score = 0
    A = "Nuclear power is a safe, viable source of energy"
    print(A)
    a = Right(input())
    Score += a
    B = "Increasing regulations on fossil fuels will have ambiguous benefits and cripple the economy"
    print(B)
    b = Right(input())
    Score += b
    C = "The industrial revolution and it’s consequences have been a disaster for the human race"
    print(C)
    c = Left(input())
    Score += c
    D = "Single payer healthcare is preferable to a privatized system"
    print(D)
    d = Left(input())
    Score += d
    E = "Free trade and globalization have been our greatest allies in alleviating poverty"
    print(E)
    e = Right(input())
    Score += e
    F = "A state-planned economy cannot scale to the efficiency or complexity of the free market"
    print(F)
    f = Right(input())
    Score += f
    G = "Deficit spending is necessary to rebuild our crumbling public infrastructure"
    print(G)
    g = Left(input())
    Score += g
    H = "Water should be a public resource that anyone can access freely"
    print(H)
    h = Left(input())
    Score += h
    I = "Education would be much more effective if school choice was left to the parents"
    print(I)
    i = Right(input())
    Score += i
    J = "We lose more in taxes than government could ever give back"
    print(J)
    j = Right(input())
    Score += j
    K = "Industry should be owned and controlled by labour unions"
    print(K)
    k = Socialism(input())
    Score += k
    L = "Raising the minimum wage will not help the working class"
    print(L)
    l = Right(input())
    Score += l
    M = "Helping the unemployed is of greater urgency than slowing down inflation"
    print(M)
    m = Left(input())
    Score += m
    N = "Precious metals and cryptocurrencies are more trustworthy than federal banking systems"
    print(N)
    n = Right(input())
    Score += n
    O = "I support regulations enforcing net neutrality"
    print(O)
    o = Left(input())
    Score += o
    P = "The military,courts and police could be replaced with voluntary legal agreements and private protection agencies"
    print(P)
    p = McPolice(input())
    Score += p
    Q = "It’s a tragedy that art and culture are commodified and cheapened by the capitalist system"
    print(Q)
    q = Left(input())
    Score += q
    R = "Affordable housing programs to little except destroy property values"
    print(R)
    n = Right(input())
    Score += n
    S = "A federal jobs initiative is an excellent remedy to economic downturns"
    print(S)
    s = Left(input())
    Score += s
    T = "Prosperity without equality is an injustice"
    print(T)
    t = Left(input())
    Score += t
    print(Score)

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
        self.welcomeLabel2 = ttk.Label(self,text='This test is a new and improved version of the popular political compass test which has become the subject of a lot of memes')
        self.welcomeLabel2.pack()


        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        print("Button clicked")
        self.destroy()
        app = QuestionWindow()



class QuestionWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the question window
        self.title('Questions')
        self.geometry('5000x500')
        self.configure(bg="blue")

        # labels
        self.questionLabel = ttk.Label(self,text="Question #: ....")
        self.questionLabel.pack()

        # checkboxes
        self.option1 = ttk.Checkbutton(self,text="Strongly Agree")
        self.option2 = ttk.Checkbutton(self,text="Moderately Agree")
        self.option3 = ttk.Checkbutton(self,text="Moderately Disagree")
        self.option4 = ttk.Checkbutton(self,text="Strongly Disagree")
        self.option1.pack()
        self.option2.pack()
        self.option3.pack()
        self.option4.pack()

        # button
        self.button = ttk.Button(self, text='Next question')
        self.button.pack()


class LastQuestionWindow(tk.Tk):
    # Should inherit or extend the QuestionWindow class
    pass # On the last question, the command should take it to the results page

class ResultsWindow(tk.Tk):
    pass # fill this in once the question windows are sorted out
    # Should display the compass, scales to show the different results and a button to export the results
    # to a .txt file


if __name__ == "__main__":
    app = OpeningWindow()
    app.mainloop()

    # Do some for-loop for the number of questions
