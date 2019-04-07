import tkinter as tk

import json

with open ('studentAnswers.json') as f:
    data = json.load(f)


standardFont = ("Helvetica", 14)
buttonFont = ("Helvetica", 16)
headerFont = ("Helvetica", 30)
subHeaderFont = ("Helvetica", 20)
answersFont = ("Helvetica", 10)

class Application(tk.Tk):

    def __init__(self, *args, **kwargs, ):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


#                                  MENU BAR 

###############################################################################
        menu = tk.Menu(container)

        systemMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=systemMenu, label="System")
        systemMenu.add_command(label="Home",
                            command=lambda: self.show_frame(ORPage))
        systemMenu.add_command(label="Logout")
        systemMenu.add_command(label="Exit", command=quit)

        resultsMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=resultsMenu, label="Test Results")
        resultsMenu.add_command(label="Formative Test Results",
                            command=lambda: self.show_frame(FormativeResultsPage))
        resultsMenu.add_command(label="Summative Test Results",
                            command=lambda: self.show_frame(SummativeResultsPage))

        tk.Tk.config(self, menu=menu)

##################################################################################


        # main loop for pages
        for F in (ORPage, FormativeResultsPage, SummativeResultsPage, PythonFormative, JavaFormative, WebDevFormative, CompSysFormative, PythonFormative1, PythonFormativeFeedback,
            PythonSummative, JavaSummative, WebDevSummative, CompSysSummative, JavaSummative1, JavaSummativeFeedback):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg='white')

        self.show_frame(ORPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class ORPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Test Results", bg='white', font=headerFont)
        label.pack(pady=10, padx=10)

        modulesBtn = tk.Button(self, text="Modules", font=buttonFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        modulesBtn.pack()

        button1 = tk.Button(self, text="Formative Results", font=buttonFont,
                        command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Summative Results", font=buttonFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        button2.pack()

#   *****   PAGES   *****

# ========== FORMATIVE TEST RESULTS ===========
class FormativeResultsPage(tk.Frame):

    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Formative Test Results",  font=headerFont, bg='white',)
        label.pack(pady=10, padx=10)


        moduleLabel = tk.Label(self, text="Choose Test Module:", fg="#807682", font=subHeaderFont, bg='white',)
        moduleLabel.pack(pady=10, padx=10)

        # need to use 'highlightbackground' instead of bg="" for mac
        module1Btn = tk.Button(self, text="Python", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(PythonFormative))
        module1Btn.pack(fill='x')

        module2Btn = tk.Button(self, text="Java", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(JavaFormative))
        module2Btn.pack(fill='x')

        module3Btn = tk.Button(self, text="Web Development", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(WebDevFormative))
        module3Btn.pack(fill='x')

        module4Btn = tk.Button(self, text="Computation Systems", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(CompSysFormative))
        module4Btn.pack(fill='x')

        button2 = tk.Button(self, text="View Summative Test Results", font=standardFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        button2.pack(pady=20)
        button1 = tk.Button(self, text="Home", font=standardFont,
                        command=lambda: controller.show_frame(ORPage))
        button1.pack(pady=10)

# Python Formative Test Results MAIN PAGE
class PythonFormative(tk.Frame):

    def __init__(self, parent, controller):

        with open('Python General Knowledge.json', 'r') as file:
            testData = json.load(file)

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Python Formative Test Results Available:", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        buttonTest = tk.Button(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=buttonFont, bg="#C6DDF5",
                            command=lambda: controller.show_frame(PythonFormative1))
        buttonTest.pack(pady=40, padx=10)


        button1 = tk.Button(self, text="Back", font=standardFont,
                        command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=standardFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack()

#Python Formative Test Results for test 1
class PythonFormative1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userID = '12'

        answers =[]

        with open ('Student/formative/lastAttempt/12 1.json', 'r') as f:
            data = json.load(f)



        # # access just the answer list
        #     for i in data:
        #         if i['studentID'] == userID:
        #             answers = i['answers']
        #             break
        #         else:
        #             print("Not found")

            data['answers'] = answers

            print()
            print(data['answers'])


        #### CORRECT FILE PATH NEEDS TO BE SET ###
        with open('Python General Knowledge.json', 'r') as file:
            testData = json.load(file)

        # Create a list of correct answers from the json
        correctList = []
        for i in range(1,11):
            correctList.append(testData["QnA"][str(i)]["correctA"])


        labelTitle = tk.Label(self, text='Results for Test: {} - {}'.format(testData["testID"], testData["name"]), font=subHeaderFont, fg='#8A5A76', bg='white')
        labelTitle.pack(pady=2)


        mark = 0


        # for i in range(10):
        #     if correctList[i][1] == answers[i]:
        #         mark += 1

        #         # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
        #         # labelQ.pack(pady=1, padx=2)

        #         labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tCorrect", bg='white', font=standardFont, anchor='w', width=100)
        #         labelA.pack(pady=1, padx=2)

        #         labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", bg='white', fg='#ebebeb')
        #         labelDash.pack()

        #     else:

        #         # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
        #         # labelQ.pack(pady=1, padx=2)

        #         labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tIncorrect", bg='white', font=standardFont, anchor='w', width=100)
        #         labelA.pack(padx=2)

        #         labelC = tk.Label(self, text="\t\t\t\t\t\t\t\tCorrect answer was: {}) {}".format(correctList[i][1], correctList[i][0]), fg="#57526B", bg='white', font=answersFont, anchor='w', width=100)
        #         labelC.pack()

        #         labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", bg='white', fg='#ebebeb')
        #         labelDash.pack()



        # labelTotal = tk.Label(self, text="Total Mark: " + str(mark) + "/10", fg="#8A5A76", bg='white', font=standardFont)
        # labelTotal.pack()

        # print("Total Mark: " , mark,"/10")



        button1 = tk.Button(self, text="View Feedback", font='buttonFont',
                        command=lambda: controller.show_frame(PythonFormativeFeedback))
        button1.pack()
        button2 = tk.Button(self, text="Back", font='buttonFont',
                        command=lambda: controller.show_frame(PythonFormative))
        button2.pack(pady=5)

# Formative Feedback for Python1
class PythonFormativeFeedback(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        with open('Python General Knowledge.json', 'r') as file:
            testData = json.load(file)

        label = tk.Label(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=headerFont, bg='white')
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Feedback for test", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)


        # Create a list of the test questions
        questionList = []
        for i in range(1,11):
            questionList.append(testData["QnA"][str(i)]["q"])


        # Create a list of the test feedback
        feedback = []
        for i in range(1,11):
            feedback.append(testData["QnA"][str(i)]["feedback"])



        for i in range(10):
            # if questionList[i] == feedback[i]:

            labelQ = tk.Label(self, text="Question " + str(i+1) + ") {}".format(questionList[i]), fg="#57526B", bg='white', font=answersFont)
            labelQ.pack(pady=0, padx=2)

            labelF = tk.Label(self, text="{}".format(feedback[i]), bg='white', font=answersFont)
            labelF.pack(pady=3, padx=0)
                



        button1 = tk.Button(self, text="Back to Results", font=standardFont,
                        command=lambda: controller.show_frame(PythonFormative1))
        button1.pack(pady=20)
        button2 = tk.Button(self, text="Home", font=standardFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack()
# Java
class JavaFormative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = tk.Label(self, text="Java: Formative Test Results", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont, bg='white')
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                        command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

# Web Development
class WebDevFormative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Web Development: Formative Test Results", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont, bg='white')
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                        command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

# Computational Systems
class CompSysFormative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Computational Systems: Formative Test Results", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont, bg='white')
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                        command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

# =============== SUMMATIVE RESULTS =============
class SummativeResultsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Summative Test Results",  font=headerFont, bg='white',)
        label.pack(pady=10, padx=10)

        moduleLabel = tk.Label(self, text="Choose Test Module:", fg="#807682", font=subHeaderFont, bg='white',)
        moduleLabel.pack(pady=10, padx=10)

        # need to use 'highlightbackground' instead of bg="" for mac
        module1Btn = tk.Button(self, text="Python", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(PythonSummative))
        module1Btn.pack(fill='x')

        module2Btn = tk.Button(self, text="Java", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(JavaSummative))
        module2Btn.pack(fill='x')

        module3Btn = tk.Button(self, text="Web Development", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(WebDevSummative))
        module3Btn.pack(fill='x')

        module4Btn = tk.Button(self, text="Computation Systems", bg="#dfbfcb", font=buttonFont,
                        command=lambda: controller.show_frame(CompSysSummative))
        module4Btn.pack(fill='x')


        button1 = tk.Button(self, text="View Formative Test Results", font=standardFont,
                        command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack(pady=20)
        button2 = tk.Button(self, text="Home", font=standardFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

#  Python
class PythonSummative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Python: Summative Test Results", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont, bg='white')
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

#  Java
class JavaSummative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        with open('Java Capital Cities.json', 'r') as file:
            testData = json.load(file)
  
        label = tk.Label(self, text="Java Summative Test Results Available:", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        buttonTest = tk.Button(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=buttonFont, bg="#C6DDF5",
                            command=lambda: controller.show_frame(JavaSummative1))
        buttonTest.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=standardFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=standardFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack()
# Java Summative Test Results for test 1
class JavaSummative1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userID = "103"

        with open ('studentAnswers.json', 'r') as f:
            data = json.load(f)

        # access just the answer list
            for i in data['testID']:
                if i['studentID'] == userID:
                    answers = i['Test']['answers']
                    break
                else:
                    print("Not found")


        #### CORRECT FILE PATH NEEDS TO BE SET ###
        with open('Java Capital Cities.json', 'r') as file:
            testData = json.load(file)


        # Create a list of correct answers from the json
        correctList = []
        for i in range(1,11):
            correctList.append(testData["QnA"][str(i)]["correctA"])


        labelTitle = tk.Label(self, text='Results for Test: {} - {}'.format(testData["testID"], testData["name"]), font=subHeaderFont, fg='#8A5A76', bg='white')
        labelTitle.pack(pady=2)


        mark = 0

        for i in range(10):
            if correctList[i][1] == answers[i]:
                mark += 1

                # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
                # labelQ.pack(pady=1, padx=2)

                labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tCorrect", bg='white', font=standardFont, anchor='w', width=100)
                labelA.pack(pady=1, padx=2)

                labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", bg='white', fg='#ebebeb')
                labelDash.pack()

            else:

                # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
                # labelQ.pack(pady=1, padx=2)

                labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tIncorrect", bg='white', font=standardFont, anchor='w', width=100)
                labelA.pack(padx=2)

                labelC = tk.Label(self, text="\t\t\t\t\t\t\t\tCorrect answer was: {}) {}".format(correctList[i][1], correctList[i][0]), fg="#57526B", bg='white', font=answersFont, anchor='w', width=100)
                labelC.pack()

                labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", bg='white', fg='#ebebeb')
                labelDash.pack()

        labelTotal = tk.Label(self, text="Total Mark: " + str(mark) + "/10", fg="#8A5A76", bg='white', font=standardFont)
        labelTotal.pack()

        print("Total Mark: " , mark,"/10")



        button1 = tk.Button(self, text="View Feedback", font='buttonFont',
                        command=lambda: controller.show_frame(JavaSummativeFeedback))
        button1.pack()
        button2 = tk.Button(self, text="Back", font='buttonFont',
                        command=lambda: controller.show_frame(JavaSummative))
        button2.pack(pady=5)

# Sumamtive Feedback for Java1
class JavaSummativeFeedback(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        with open('Java Capital Cities.json', 'r') as file:
            testData = json.load(file)

        label = tk.Label(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=headerFont, bg='white')
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Feedback for test", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)


        # Create a list of the test questions
        questionList = []
        for i in range(1,11):
            questionList.append(testData["QnA"][str(i)]["q"])


        # Create a list of the test feedback
        feedback = []
        for i in range(1,11):
            feedback.append(testData["QnA"][str(i)]["feedback"])



        for i in range(10):
            # if questionList[i] == feedback[i]:

            labelQ = tk.Label(self, text="Question " + str(i+1) + ") {}".format(questionList[i]), fg="#57526B", bg='white', font=answersFont)
            labelQ.pack(pady=0, padx=2)

            labelF = tk.Label(self, text="{}".format(feedback[i]), bg='white', font=answersFont)
            labelF.pack(pady=3, padx=0)
                



        button1 = tk.Button(self, text="Back to Results", font=standardFont,
                        command=lambda: controller.show_frame(JavaSummative1))
        button1.pack(pady=20)
        button2 = tk.Button(self, text="Home", font=standardFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack()

#  Web Development
class WebDevSummative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Web Development: Summative Test Results", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont, bg='white')
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

#  Computational System
class CompSysSummative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Computational Systems: Summative Test Results", font=subHeaderFont, bg='white')
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont, bg='white')
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                        command=lambda: controller.show_frame(SummativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                        command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)

app = Application()
app.title("Education App")
app.geometry("1200x800")
app.mainloop()