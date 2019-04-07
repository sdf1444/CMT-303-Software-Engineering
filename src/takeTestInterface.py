# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:53
# @Author  : Chaoran Wang
# @FileName: takeTestInterface.py
# @Software: PyCharm
from tkinter import *
import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from src_ClassTest import Test
import json
import os,sys
import random
with open ('studentAnswers.json') as f:
    data = json.load(f)


standardFont = ("Helvetica", 14)
buttonFont = ("Helvetica", 16)
headerFont = ("Helvetica", 30)
subHeaderFont = ("Helvetica", 20)
answersFont = ("Helvetica", 10)

class TestTakeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.is_save = False
        # The container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others.
        container = tk.Frame(self)
        container.pack(side="left", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.quiz = Test(True, 'testID', 'module')

        self.frames = {}
        for F in (StartPage, SummativeTestInterFace, FormativeTestInterface, TakeFormativeNomal, TakeFormativeFinal):
            # page_name = F.__name__
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        # self.geometry('1200x800')

    def show_frame(self, cont):
        # Show a frame for the given page name.
        frame = self.frames[cont]
        frame.tkraise()

    def open_file(self, path):
        # Open the file with the path.
        with open('path', 'w') as f:
            pass

class StartPage(tk.Frame):
    # First page of GUI.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Tests")
        # self.app1 = Application()
        # self.app1.title("Education App")
        # self.app1.geometry("1200x800")
        button1 = tk.Button(self, text="Take Formative Test", font=16, command=lambda: controller.show_frame(FormativeTestInterface))
        button1.place(x=550, y=200)#OpenFormativeTest

        button2 = tk.Button(self, text="Take Summative Test", font=16, command=lambda: controller.show_frame(SummativeTestInterFace))
        button2.place(x=550, y=400)

        button3 = tk.Button(self, text="View Result of Student", font=16,
                            command=self.start)
        button3.place(x=550, y=600)

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)

    def quit(self):
        # When logout clicked application quits.
        self.destroy()
    def start(self):
        self.app1 = Application()
        self.app1.title("Education App")
        self.app1.geometry("1200x800")
        self.app1.mainloop()

class FormativeTestInterface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Take Formative Test")

        logout = tk.Button(self, text="Normal Take", font=16, command=lambda: controller.show_frame(TakeFormativeNomal))
        logout.place(x=425, y=360)

        logout = tk.Button(self, text="Final Take", font=16, command=lambda: controller.show_frame(TakeFormativeFinal))
        logout.place(x=625, y=360)

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)
        logout = tk.Button(self, text="Back", font=16, command=lambda: controller.show_frame(StartPage))
        logout.place(x=25, y=760)

class TakeFormativeNomal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.m = StringVar()
        self.controller.title("Take Formative Test")
        self.test1 = tk.Label(self, text="Tests", font=14, fg="black")
        self.test1.place(x=1000, y=0)
        self.test2 = ttk.Combobox(self, width='60')
        test_list = []
        path = "./formative/Released"
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            test_list.append(file_path)
        self.test2['values'] = tuple(test_list)
        self.test2.place(x=750, y=40)

        select = tk.Button(self, text="Select", font=16, fg="black", command=lambda: self.OpenFile(self.test2.get()))
        select.place(x=830, y=0)

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)

        logout = tk.Button(self, text="Back", font=16, command=lambda: controller.show_frame(FormativeTestInterface))
        logout.place(x=25, y=760)


    def OpenFile(self, path):
        try:

            f = open(path, encoding='utf-8')
            file_data = json.load(f)
            #file_data is a json Object


            self.module1 = tk.Label(self, text="Module", font=14, fg="black")
            self.module1.place(x=0, y=1)
            self.module2 = tk.Label(self, text=file_data["module"], font=14, fg="black",bg="SlateGray")
            self.module2.place(x=90, y=5)
            self.testname = tk.Label(self, text="TestName", font=14, fg="black")
            self.testname.place(x=0, y=40)
            self.testname2 = tk.Label(self, text=file_data["name"], font=14, fg="black",bg="SlateGray")
            self.testname2.place(x=90, y=45)




            d = dict(file_data["QnA"])
            questionobject = []
            choicelist = []
            for item in d.items():
                questionobject.append(item)

            # Q1
            name1 = "Question" + questionobject[0][0]
            q1name = questionobject[0][1]["q"]
            q1chice = []
            q1chice.append(questionobject[0][1]["correctA"])
            for item in questionobject[0][1]["wrongAs"]:
                q1chice.append(item)
            showquest = sorted(q1chice, key=lambda k: k[1])
            self.question1 = tk.Label(self, text=name1, font=14, fg="black")
            self.question1.place(x=0, y=80)
            self.question1show = tk.Label(self, text=q1name, font=14, fg="black")
            self.question1show.place(x=120, y=80)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            choice1 = showquest[0][1].upper()+"."+showquest[0][0]
            choice2 = showquest[1][1].upper()+"."+showquest[1][0]
            choice3 = showquest[2][1].upper()+"."+showquest[2][0]
            choice4 = showquest[3][1].upper()+"."+showquest[3][0]
            self.question1Choise1 = tk.Label(self, text=choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=80)
            self.question1Choise2 = tk.Label(self, text=choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=80)
            self.question1Choise3 = tk.Label(self, text=choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=80)
            self.question1Choise4 = tk.Label(self, text=choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=80)

            # Q2
            name2 = "Question" + questionobject[1][0]
            q2name = questionobject[1][1]["q"]
            q2chice = []
            q2chice.append(questionobject[1][1]["correctA"])
            for item in questionobject[1][1]["wrongAs"]:
                q2chice.append(item)
            showquest2 = sorted(q2chice, key=lambda k: k[1])
            self.question2 = tk.Label(self, text=name2, font=14, fg="black")
            self.question2.place(x=0, y=130)
            self.question2show = tk.Label(self, text=q2name, font=14, fg="black")
            self.question2show.place(x=120, y=130)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q2choice1 = showquest2[0][1].upper() + "." + showquest2[0][0]
            q2choice2 = showquest2[1][1].upper() + "." + showquest2[1][0]
            q2choice3 = showquest2[2][1].upper() + "." + showquest2[2][0]
            q2choice4 = showquest2[3][1].upper() + "." + showquest2[3][0]
            self.question1Choise1 = tk.Label(self, text=q2choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=130)
            self.question1Choise2 = tk.Label(self, text=q2choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=130)
            self.question1Choise3 = tk.Label(self, text=q2choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=130)
            self.question1Choise4 = tk.Label(self, text=q2choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=130)

            # Q3
            name3 = "Question" + questionobject[2][0]
            q3name = questionobject[2][1]["q"]
            q3chice = []
            q3chice.append(questionobject[2][1]["correctA"])
            for item in questionobject[2][1]["wrongAs"]:
                q3chice.append(item)
            showquest3 = sorted(q3chice, key=lambda k: k[1])
            self.question3 = tk.Label(self, text=name3, font=14, fg="black")
            self.question3.place(x=0, y=160)
            self.question3show = tk.Label(self, text=q3name, font=14, fg="black")
            self.question3show.place(x=120, y=160)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q3choice1 = showquest3[0][1].upper() + "." + showquest3[0][0]
            q3choice2 = showquest3[1][1].upper() + "." + showquest3[1][0]
            q3choice3 = showquest3[2][1].upper() + "." + showquest3[2][0]
            q3choice4 = showquest3[3][1].upper() + "." + showquest3[3][0]
            self.question1Choise1 = tk.Label(self, text=q3choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=160)
            self.question1Choise2 = tk.Label(self, text=q3choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=160)
            self.question1Choise3 = tk.Label(self, text=q3choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=160)
            self.question1Choise4 = tk.Label(self, text=q3choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=160)

            # Q4
            name4 = "Question" + questionobject[3][0]
            q4name = questionobject[3][1]["q"]
            q4chice = []
            q4chice.append(questionobject[3][1]["correctA"])
            for item in questionobject[3][1]["wrongAs"]:
                q4chice.append(item)
            showquest4 = sorted(q4chice, key=lambda k: k[1])
            self.question4 = tk.Label(self, text=name4, font=14, fg="black")
            self.question4.place(x=0, y=190)
            self.question4show = tk.Label(self, text=q4name, font=14, fg="black")
            self.question4show.place(x=120, y=190)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q4choice1 = showquest4[0][1].upper() + "." + showquest4[0][0]
            q4choice2 = showquest4[1][1].upper() + "." + showquest4[1][0]
            q4choice3 = showquest4[2][1].upper() + "." + showquest4[2][0]
            q4choice4 = showquest4[3][1].upper() + "." + showquest4[3][0]
            self.question1Choise1 = tk.Label(self, text=q4choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=190)
            self.question1Choise2 = tk.Label(self, text=q4choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=190)
            self.question1Choise3 = tk.Label(self, text=q4choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=190)
            self.question1Choise4 = tk.Label(self, text=q4choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=190)

            # Q5
            name5 = "Question" + questionobject[4][0]
            q5name = questionobject[4][1]["q"]
            q5chice = []
            q5chice.append(questionobject[4][1]["correctA"])
            for item in questionobject[4][1]["wrongAs"]:
                q5chice.append(item)
            showquest5 = sorted(q5chice, key=lambda k: k[1])
            self.question5 = tk.Label(self, text=name5, font=14, fg="black")
            self.question5.place(x=0, y=220)
            self.question5show = tk.Label(self, text=q5name, font=14, fg="black")
            self.question5show.place(x=120, y=220)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q5choice1 = showquest5[0][1].upper() + "." + showquest5[0][0]
            q5choice2 = showquest5[1][1].upper() + "." + showquest5[1][0]
            q5choice3 = showquest5[2][1].upper() + "." + showquest5[2][0]
            q5choice4 = showquest5[3][1].upper() + "." + showquest5[3][0]
            self.question1Choise1 = tk.Label(self, text=q5choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=220)
            self.question1Choise2 = tk.Label(self, text=q5choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=220)
            self.question1Choise3 = tk.Label(self, text=q5choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=220)
            self.question1Choise4 = tk.Label(self, text=q5choice4, font=12, fg="black")
            self.question1Choise4.place(x=1030, y=220)

            # Q6
            name6 = "Question" + questionobject[5][0]
            q6name = questionobject[5][1]["q"]
            q6chice = []
            q6chice.append(questionobject[5][1]["correctA"])
            for item in questionobject[5][1]["wrongAs"]:
                q6chice.append(item)
            showquest6 = sorted(q6chice, key=lambda k: k[1])
            self.question6 = tk.Label(self, text=name6, font=14, fg="black")
            self.question6.place(x=0, y=250)
            self.question6show = tk.Label(self, text=q6name, font=14, fg="black")
            self.question6show.place(x=120, y=250)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q6choice1 = showquest6[0][1].upper() + "." + showquest6[0][0]
            q6choice2 = showquest6[1][1].upper() + "." + showquest6[1][0]
            q6choice3 = showquest6[2][1].upper() + "." + showquest6[2][0]
            q6choice4 = showquest6[3][1].upper() + "." + showquest6[3][0]
            self.question1Choise1 = tk.Label(self, text=q6choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=250)
            self.question1Choise2 = tk.Label(self, text=q6choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=250)
            self.question1Choise3 = tk.Label(self, text=q6choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=250)
            self.question1Choise4 = tk.Label(self, text=q6choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=250)

            # Q7
            name7 = "Question" + questionobject[6][0]
            q7name = questionobject[6][1]["q"]
            q7chice = []
            q7chice.append(questionobject[6][1]["correctA"])
            for item in questionobject[6][1]["wrongAs"]:
                q7chice.append(item)
            showquest7 = sorted(q7chice, key=lambda k: k[1])
            self.question7 = tk.Label(self, text=name7, font=14, fg="black")
            self.question7.place(x=0, y=280)
            self.question7show = tk.Label(self, text=q7name, font=14, fg="black")
            self.question7show.place(x=120, y=280)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q7choice1 = showquest6[0][1].upper() + "." + showquest7[0][0]
            q7choice2 = showquest6[1][1].upper() + "." + showquest7[1][0]
            q7choice3 = showquest6[2][1].upper() + "." + showquest7[2][0]
            q7choice4 = showquest6[3][1].upper() + "." + showquest7[3][0]
            self.question1Choise1 = tk.Label(self, text=q7choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=280)
            self.question1Choise2 = tk.Label(self, text=q7choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=280)
            self.question1Choise3 = tk.Label(self, text=q7choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=280)
            self.question1Choise4 = tk.Label(self, text=q7choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=280)

            # Q8
            name8 = "Question" + questionobject[7][0]
            q8name = questionobject[7][1]["q"]
            q8chice = []
            q8chice.append(questionobject[7][1]["correctA"])
            for item in questionobject[7][1]["wrongAs"]:
                q8chice.append(item)
            showquest8 = sorted(q8chice, key=lambda k: k[1])
            self.question8 = tk.Label(self, text=name8, font=14, fg="black")
            self.question8.place(x=0, y=310)
            self.question8show = tk.Label(self, text=q8name, font=14, fg="black")
            self.question8show.place(x=120, y=310)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q8choice1 = showquest6[0][1].upper() + "." + showquest8[0][0]
            q8choice2 = showquest6[1][1].upper() + "." + showquest8[1][0]
            q8choice3 = showquest6[2][1].upper() + "." + showquest8[2][0]
            q8choice4 = showquest6[3][1].upper() + "." + showquest8[3][0]
            self.question1Choise1 = tk.Label(self, text=q8choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=310)
            self.question1Choise2 = tk.Label(self, text=q8choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=310)
            self.question1Choise3 = tk.Label(self, text=q8choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=310)
            self.question1Choise4 = tk.Label(self, text=q8choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=310)

            #Q9
            name9 = "Question" + questionobject[8][0]
            q9name = questionobject[8][1]["q"]
            q9chice = []
            q9chice.append(questionobject[8][1]["correctA"])
            for item in questionobject[8][1]["wrongAs"]:
                q9chice.append(item)
            showquest9 = sorted(q9chice, key=lambda k: k[1])
            self.question9 = tk.Label(self, text=name9, font=14, fg="black")
            self.question9.place(x=0, y=340)
            self.question9show = tk.Label(self, text=q9name, font=14, fg="black")
            self.question9show.place(x=120, y=340)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q9choice1 = showquest6[0][1].upper() + "." + showquest9[0][0]
            q9choice2 = showquest6[1][1].upper() + "." + showquest9[1][0]
            q9choice3 = showquest6[2][1].upper() + "." + showquest9[2][0]
            q9choice4 = showquest6[3][1].upper() + "." + showquest9[3][0]
            self.question1Choise1 = tk.Label(self, text=q9choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=340)
            self.question1Choise2 = tk.Label(self, text=q9choice2, font=12, fg="black")
            self.question1Choise2.place(x=800, y=340)
            self.question1Choise3 = tk.Label(self, text=q9choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=340)
            self.question1Choise4 = tk.Label(self, text=q9choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=340)

            # Q10
            name10 = "Question" + questionobject[9][0]
            q10name = questionobject[9][1]["q"]
            q10chice = []
            q10chice.append(questionobject[9][1]["correctA"])
            for item in questionobject[9][1]["wrongAs"]:
                q10chice.append(item)
            showquest10 = sorted(q10chice, key=lambda k: k[1])
            self.question10 = tk.Label(self, text=name10, font=14, fg="black")
            self.question10.place(x=0, y=370)
            self.question10show = tk.Label(self, text=q10name, font=14, fg="black")
            self.question10show.place(x=120, y=370)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q10choice1 = showquest6[0][1].upper() + "." + showquest10[0][0]
            q10choice2 = showquest6[1][1].upper() + "." + showquest10[1][0]
            q10choice3 = showquest6[2][1].upper() + "." + showquest10[2][0]
            q10choice4 = showquest6[3][1].upper() + "." + showquest10[3][0]
            self.question1Choise1 = tk.Label(self, text=q10choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=370)
            self.question1Choise2 = tk.Label(self, text=q10choice2, font=12, fg="black")
            self.question1Choise2.place(x=800, y=370)
            self.question1Choise3 = tk.Label(self, text=q10choice3, font=12, fg="black")
            self.question1Choise3.place(x=940, y=370)
            self.question1Choise4 = tk.Label(self, text=q10choice4, font=12, fg="black")
            self.question1Choise4.place(x=1040, y=370)

            self.Guide = tk.Label(self, text="Enter Answers: (Eg: A,B,C,D)", font=14, fg="black")
            self.Guide.place(x=0, y=500)
            StudentAnswer = tk.Entry(self, textvariable=self.m, width=100)
            StudentAnswer.place(x=325, y=500)

            anwserlist = tk.Button(self, text="Save Test", font=16,
                                   command=lambda: self.Save(wrapper, StudentAnswer.get()))
            anwserlist.place(x=500, y=760)

            self.StudentID= "12"



            save = tk.Button(self, text="Save Anwser", font=16,
                             command=lambda: self.store(StudentAnswer.get()))
            save.place(x=500, y=525)


            wrapper = {
                "StudentID": self.StudentID,
                "name": file_data["name"],
                "testID": file_data["testID"],
                "module": file_data["module"],

            }


        except Exception as e:
            print(e)
            tk.messagebox.showinfo("", "Please select a test",)

    def store(self, StudentAnswer):
        finalanw = list(StudentAnswer)
        print(StudentAnswer)
        return finalanw

    def Save(self, wrapper,StudentAnswer):
        path = "./Student/formative/normal"
        final = self.store(StudentAnswer)
        saves = []
        print(final)
        for item in final:
            if str(item)!=",":
                saves.append(item)
        # finalanwser = final.remove(",")
        wrapper["anwsers"] = saves
        print(wrapper)
        filename = "%s/%s %s.json" % (path, wrapper["StudentID"], wrapper["testID"])
        with open(filename, "w") as outfile:
            json.dump(wrapper, outfile, indent=4)
        tk.messagebox.showinfo("", "Test has been Submitted")
        return

class TakeFormativeFinal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.m = StringVar()
        self.controller.title("Take Test - Final")
        self.test1 = tk.Label(self, text="Tests", font=14, fg="black")
        self.test1.place(x=1000, y=0)
        self.test2 = ttk.Combobox(self, width='60')
        test_list = []
        path = "./formative/Released"
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            test_list.append(file_path)
        self.test2['values'] = tuple(test_list)
        self.test2.place(x=750, y=40)

        self.feedback = tk.Button(self, text="Feedback", font=16, fg="black", command=lambda: self.Feedback(self.test2.get()))
        self.feedback.place(x=830, y=760)
        self.feedback['state'] = 'active'
        pathcheck = "./Student/formative/lastAttempt"
        for name in os.listdir(pathcheck):
            file_path = os.path.join(pathcheck, name)
            if file_path != "":
                self.feedback['state'] = 'normal'

        select = tk.Button(self, text="Select", font=16, fg="black", command=lambda: self.OpenFile(self.test2.get()))
        select.place(x=830, y=0)

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)

        logout = tk.Button(self, text="Back", font=16, command=lambda: controller.show_frame(FormativeTestInterface))
        logout.place(x=25, y=760)

    def Feedback(self, path):
      try:
          f = open(path, encoding='utf-8')
          file_data = json.load(f)
          d = dict(file_data["QnA"])
          questionobject = []
          for item in d.items():
             questionobject.append(item)

          c1 = questionobject[0][1]["correctA"]
          c2 = questionobject[1][1]["correctA"]
          c3 = questionobject[2][1]["correctA"]
          c4 = questionobject[3][1]["correctA"]
          c5 = questionobject[4][1]["correctA"]
          c6 = questionobject[5][1]["correctA"]
          c7 = questionobject[6][1]["correctA"]
          c8 = questionobject[7][1]["correctA"]
          c9 = questionobject[8][1]["correctA"]
          c10 = questionobject[9][1]["correctA"]
          self.module1 = tk.Label(self, text=c1, font=14, fg="black")
          self.module1.place(x=0, y=10)
          self.module2 = tk.Label(self, text=c2, font=14, fg="black")
          self.module2.place(x=0, y=30)
          self.module3 = tk.Label(self, text=c3, font=14, fg="black")
          self.module3.place(x=0, y=50)
          self.module4 = tk.Label(self, text=c4, font=14, fg="black")
          self.module4.place(x=0, y=70)
          self.module5 = tk.Label(self, text=c5, font=14, fg="black")
          self.module5.place(x=0, y=90)
          self.module6 = tk.Label(self, text=c6, font=14, fg="black")
          self.module6.place(x=0, y=110)
          self.module7 = tk.Label(self, text=c7, font=14, fg="black")
          self.module7.place(x=0, y=130)
          self.module8 = tk.Label(self, text=c8, font=14, fg="black")
          self.module8.place(x=0, y=150)
          self.module9 = tk.Label(self, text=c9, font=14, fg="black")
          self.module9.place(x=0, y=170)
          self.module10 = tk.Label(self, text=c10, font=14, fg="black")
          self.module10.place(x=0, y=190)







      except Exception as e:
          print(e)
          tk.messagebox.showinfo("", "Please select a test", )


    def OpenFile(self, path):
        try:

            f = open(path, encoding='utf-8')
            file_data = json.load(f)
            #file_data is a json Object


            self.module1 = tk.Label(self, text="Module", font=14, fg="black")
            self.module1.place(x=0, y=1)
            self.module2 = tk.Label(self, text=file_data["module"], font=14, fg="black",bg="SlateGray")
            self.module2.place(x=90, y=5)
            self.testname = tk.Label(self, text="TestName", font=14, fg="black")
            self.testname.place(x=0, y=40)
            self.testname2 = tk.Label(self, text=file_data["name"], font=14, fg="black",bg="SlateGray")
            self.testname2.place(x=90, y=45)




            d = dict(file_data["QnA"])
            questionobject = []
            choicelist = []
            for item in d.items():
                questionobject.append(item)

            # Q1
            name1 = "Question" + questionobject[0][0]
            q1name = questionobject[0][1]["q"]
            q1chice = []
            q1chice.append(questionobject[0][1]["correctA"])
            for item in questionobject[0][1]["wrongAs"]:
                q1chice.append(item)
            showquest = sorted(q1chice, key=lambda k: k[1])
            self.question1 = tk.Label(self, text=name1, font=14, fg="black")
            self.question1.place(x=0, y=80)
            self.question1show = tk.Label(self, text=q1name, font=14, fg="black")
            self.question1show.place(x=120, y=80)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            choice1 = showquest[0][1].upper()+"."+showquest[0][0]
            choice2 = showquest[1][1].upper()+"."+showquest[1][0]
            choice3 = showquest[2][1].upper()+"."+showquest[2][0]
            choice4 = showquest[3][1].upper()+"."+showquest[3][0]
            self.question1Choise1 = tk.Label(self, text=choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=80)
            self.question1Choise2 = tk.Label(self, text=choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=80)
            self.question1Choise3 = tk.Label(self, text=choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=80)
            self.question1Choise4 = tk.Label(self, text=choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=80)

            # Q2
            name2 = "Question" + questionobject[1][0]
            q2name = questionobject[1][1]["q"]
            q2chice = []
            q2chice.append(questionobject[1][1]["correctA"])
            for item in questionobject[1][1]["wrongAs"]:
                q2chice.append(item)
            showquest2 = sorted(q2chice, key=lambda k: k[1])
            self.question2 = tk.Label(self, text=name2, font=14, fg="black")
            self.question2.place(x=0, y=130)
            self.question2show = tk.Label(self, text=q2name, font=14, fg="black")
            self.question2show.place(x=120, y=130)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q2choice1 = showquest2[0][1].upper() + "." + showquest2[0][0]
            q2choice2 = showquest2[1][1].upper() + "." + showquest2[1][0]
            q2choice3 = showquest2[2][1].upper() + "." + showquest2[2][0]
            q2choice4 = showquest2[3][1].upper() + "." + showquest2[3][0]
            self.question1Choise1 = tk.Label(self, text=q2choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=130)
            self.question1Choise2 = tk.Label(self, text=q2choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=130)
            self.question1Choise3 = tk.Label(self, text=q2choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=130)
            self.question1Choise4 = tk.Label(self, text=q2choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=130)

            # Q3
            name3 = "Question" + questionobject[2][0]
            q3name = questionobject[2][1]["q"]
            q3chice = []
            q3chice.append(questionobject[2][1]["correctA"])
            for item in questionobject[2][1]["wrongAs"]:
                q3chice.append(item)
            showquest3 = sorted(q3chice, key=lambda k: k[1])
            self.question3 = tk.Label(self, text=name3, font=14, fg="black")
            self.question3.place(x=0, y=160)
            self.question3show = tk.Label(self, text=q3name, font=14, fg="black")
            self.question3show.place(x=120, y=160)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q3choice1 = showquest3[0][1].upper() + "." + showquest3[0][0]
            q3choice2 = showquest3[1][1].upper() + "." + showquest3[1][0]
            q3choice3 = showquest3[2][1].upper() + "." + showquest3[2][0]
            q3choice4 = showquest3[3][1].upper() + "." + showquest3[3][0]
            self.question1Choise1 = tk.Label(self, text=q3choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=160)
            self.question1Choise2 = tk.Label(self, text=q3choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=160)
            self.question1Choise3 = tk.Label(self, text=q3choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=160)
            self.question1Choise4 = tk.Label(self, text=q3choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=160)

            # Q4
            name4 = "Question" + questionobject[3][0]
            q4name = questionobject[3][1]["q"]
            q4chice = []
            q4chice.append(questionobject[3][1]["correctA"])
            for item in questionobject[3][1]["wrongAs"]:
                q4chice.append(item)
            showquest4 = sorted(q4chice, key=lambda k: k[1])
            self.question4 = tk.Label(self, text=name4, font=14, fg="black")
            self.question4.place(x=0, y=190)
            self.question4show = tk.Label(self, text=q4name, font=14, fg="black")
            self.question4show.place(x=120, y=190)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q4choice1 = showquest4[0][1].upper() + "." + showquest4[0][0]
            q4choice2 = showquest4[1][1].upper() + "." + showquest4[1][0]
            q4choice3 = showquest4[2][1].upper() + "." + showquest4[2][0]
            q4choice4 = showquest4[3][1].upper() + "." + showquest4[3][0]
            self.question1Choise1 = tk.Label(self, text=q4choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=190)
            self.question1Choise2 = tk.Label(self, text=q4choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=190)
            self.question1Choise3 = tk.Label(self, text=q4choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=190)
            self.question1Choise4 = tk.Label(self, text=q4choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=190)

            # Q5
            name5 = "Question" + questionobject[4][0]
            q5name = questionobject[4][1]["q"]
            q5chice = []
            q5chice.append(questionobject[4][1]["correctA"])
            for item in questionobject[4][1]["wrongAs"]:
                q5chice.append(item)
            showquest5 = sorted(q5chice, key=lambda k: k[1])
            self.question5 = tk.Label(self, text=name5, font=14, fg="black")
            self.question5.place(x=0, y=220)
            self.question5show = tk.Label(self, text=q5name, font=14, fg="black")
            self.question5show.place(x=120, y=220)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q5choice1 = showquest5[0][1].upper() + "." + showquest5[0][0]
            q5choice2 = showquest5[1][1].upper() + "." + showquest5[1][0]
            q5choice3 = showquest5[2][1].upper() + "." + showquest5[2][0]
            q5choice4 = showquest5[3][1].upper() + "." + showquest5[3][0]
            self.question1Choise1 = tk.Label(self, text=q5choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=220)
            self.question1Choise2 = tk.Label(self, text=q5choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=220)
            self.question1Choise3 = tk.Label(self, text=q5choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=220)
            self.question1Choise4 = tk.Label(self, text=q5choice4, font=12, fg="black")
            self.question1Choise4.place(x=1030, y=220)

            # Q6
            name6 = "Question" + questionobject[5][0]
            q6name = questionobject[5][1]["q"]
            q6chice = []
            q6chice.append(questionobject[5][1]["correctA"])
            for item in questionobject[5][1]["wrongAs"]:
                q6chice.append(item)
            showquest6 = sorted(q6chice, key=lambda k: k[1])
            self.question6 = tk.Label(self, text=name6, font=14, fg="black")
            self.question6.place(x=0, y=250)
            self.question6show = tk.Label(self, text=q6name, font=14, fg="black")
            self.question6show.place(x=120, y=250)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q6choice1 = showquest6[0][1].upper() + "." + showquest6[0][0]
            q6choice2 = showquest6[1][1].upper() + "." + showquest6[1][0]
            q6choice3 = showquest6[2][1].upper() + "." + showquest6[2][0]
            q6choice4 = showquest6[3][1].upper() + "." + showquest6[3][0]
            self.question1Choise1 = tk.Label(self, text=q6choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=250)
            self.question1Choise2 = tk.Label(self, text=q6choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=250)
            self.question1Choise3 = tk.Label(self, text=q6choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=250)
            self.question1Choise4 = tk.Label(self, text=q6choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=250)

            # Q7
            name7 = "Question" + questionobject[6][0]
            q7name = questionobject[6][1]["q"]
            q7chice = []
            q7chice.append(questionobject[6][1]["correctA"])
            for item in questionobject[6][1]["wrongAs"]:
                q7chice.append(item)
            showquest7 = sorted(q7chice, key=lambda k: k[1])
            self.question7 = tk.Label(self, text=name7, font=14, fg="black")
            self.question7.place(x=0, y=280)
            self.question7show = tk.Label(self, text=q7name, font=14, fg="black")
            self.question7show.place(x=120, y=280)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q7choice1 = showquest6[0][1].upper() + "." + showquest7[0][0]
            q7choice2 = showquest6[1][1].upper() + "." + showquest7[1][0]
            q7choice3 = showquest6[2][1].upper() + "." + showquest7[2][0]
            q7choice4 = showquest6[3][1].upper() + "." + showquest7[3][0]
            self.question1Choise1 = tk.Label(self, text=q7choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=280)
            self.question1Choise2 = tk.Label(self, text=q7choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=280)
            self.question1Choise3 = tk.Label(self, text=q7choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=280)
            self.question1Choise4 = tk.Label(self, text=q7choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=280)

            # Q8
            name8 = "Question" + questionobject[7][0]
            q8name = questionobject[7][1]["q"]
            q8chice = []
            q8chice.append(questionobject[7][1]["correctA"])
            for item in questionobject[7][1]["wrongAs"]:
                q8chice.append(item)
            showquest8 = sorted(q8chice, key=lambda k: k[1])
            self.question8 = tk.Label(self, text=name8, font=14, fg="black")
            self.question8.place(x=0, y=310)
            self.question8show = tk.Label(self, text=q8name, font=14, fg="black")
            self.question8show.place(x=120, y=310)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q8choice1 = showquest6[0][1].upper() + "." + showquest8[0][0]
            q8choice2 = showquest6[1][1].upper() + "." + showquest8[1][0]
            q8choice3 = showquest6[2][1].upper() + "." + showquest8[2][0]
            q8choice4 = showquest6[3][1].upper() + "." + showquest8[3][0]
            self.question1Choise1 = tk.Label(self, text=q8choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=310)
            self.question1Choise2 = tk.Label(self, text=q8choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=310)
            self.question1Choise3 = tk.Label(self, text=q8choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=310)
            self.question1Choise4 = tk.Label(self, text=q8choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=310)

            #Q9
            name9 = "Question" + questionobject[8][0]
            q9name = questionobject[8][1]["q"]
            q9chice = []
            q9chice.append(questionobject[8][1]["correctA"])
            for item in questionobject[8][1]["wrongAs"]:
                q9chice.append(item)
            showquest9 = sorted(q9chice, key=lambda k: k[1])
            self.question9 = tk.Label(self, text=name9, font=14, fg="black")
            self.question9.place(x=0, y=340)
            self.question9show = tk.Label(self, text=q9name, font=14, fg="black")
            self.question9show.place(x=120, y=340)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q9choice1 = showquest6[0][1].upper() + "." + showquest9[0][0]
            q9choice2 = showquest6[1][1].upper() + "." + showquest9[1][0]
            q9choice3 = showquest6[2][1].upper() + "." + showquest9[2][0]
            q9choice4 = showquest6[3][1].upper() + "." + showquest9[3][0]
            self.question1Choise1 = tk.Label(self, text=q9choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=340)
            self.question1Choise2 = tk.Label(self, text=q9choice2, font=12, fg="black")
            self.question1Choise2.place(x=800, y=340)
            self.question1Choise3 = tk.Label(self, text=q9choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=340)
            self.question1Choise4 = tk.Label(self, text=q9choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=340)

            # Q10
            name10 = "Question" + questionobject[9][0]
            q10name = questionobject[9][1]["q"]
            q10chice = []
            q10chice.append(questionobject[9][1]["correctA"])
            for item in questionobject[9][1]["wrongAs"]:
                q10chice.append(item)
            showquest10 = sorted(q10chice, key=lambda k: k[1])
            self.question10 = tk.Label(self, text=name10, font=14, fg="black")
            self.question10.place(x=0, y=370)
            self.question10show = tk.Label(self, text=q10name, font=14, fg="black")
            self.question10show.place(x=120, y=370)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q10choice1 = showquest6[0][1].upper() + "." + showquest10[0][0]
            q10choice2 = showquest6[1][1].upper() + "." + showquest10[1][0]
            q10choice3 = showquest6[2][1].upper() + "." + showquest10[2][0]
            q10choice4 = showquest6[3][1].upper() + "." + showquest10[3][0]
            self.question1Choise1 = tk.Label(self, text=q10choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=370)
            self.question1Choise2 = tk.Label(self, text=q10choice2, font=12, fg="black")
            self.question1Choise2.place(x=800, y=370)
            self.question1Choise3 = tk.Label(self, text=q10choice3, font=12, fg="black")
            self.question1Choise3.place(x=940, y=370)
            self.question1Choise4 = tk.Label(self, text=q10choice4, font=12, fg="black")
            self.question1Choise4.place(x=1040, y=370)

            self.Guide = tk.Label(self, text="Enter Answers: (Eg: A,B,C,D)", font=14, fg="black")
            self.Guide.place(x=0, y=500)
            StudentAnswer = tk.Entry(self, textvariable=self.m, width=100)
            StudentAnswer.place(x=325, y=500)

            anwserlist = tk.Button(self, text="Save Test", font=16,
                                   command=lambda: self.Save(wrapper, StudentAnswer.get()))
            anwserlist.place(x=500, y=760)

            self.StudentID= "12"



            save = tk.Button(self, text="Save Anwser", font=16,
                             command=lambda: self.store(StudentAnswer.get()))
            save.place(x=500, y=525)


            wrapper = {
                "StudentID": self.StudentID,
                "name": file_data["name"],
                "testID": file_data["testID"],
                "module": file_data["module"],

            }


        except Exception as e:
            print(e)
            tk.messagebox.showinfo("", "Please select a test",)

    def store(self, StudentAnswer):
        finalanw = list(StudentAnswer)
        print(StudentAnswer)
        return finalanw

    def Save(self, wrapper,StudentAnswer):
        path = "./Student/formative/lastAttempt"
        final = self.store(StudentAnswer)
        saves = []
        print(final)
        for item in final:
            if str(item)!=",":
                saves.append(item)
        # finalanwser = final.remove(",")
        wrapper["anwsers"] = saves
        print(wrapper)
        filename = "%s/%s %s.json" % (path, wrapper["StudentID"], wrapper["testID"])
        with open(filename, "w") as outfile:
            json.dump(wrapper, outfile, indent=4)
        tk.messagebox.showinfo("", "Test has been Submitted")
        return

class SummativeTestInterFace(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.m = StringVar()
        self.controller.title("Take Summative Test")
        self.test1 = tk.Label(self, text="Tests", font=14, fg="black")
        self.test1.place(x=1000, y=0)
        self.test2 = ttk.Combobox(self, width='60')
        test_list = []
        path = "./summative/Released"
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            test_list.append(file_path)
        self.test2['values'] = tuple(test_list)
        self.test2.place(x=750, y=40)

        self.select = tk.Button(self, text="Select", font=16, fg="black", command=lambda: self.OpenFile(self.test2.get()))
        self.select.place(x=830, y=0)
        self.select['state'] = 'normal'
        pathcheck = "./Student/summative"
        for name in os.listdir(pathcheck):
            file_path = os.path.join(pathcheck, name)
            if file_path != "":
                self.select['state'] = 'active'

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)

        logout = tk.Button(self, text="Back", font=16, command=lambda: controller.show_frame(StartPage))
        logout.place(x=25, y=760)


    def OpenFile(self, path):
        try:

            f = open(path, encoding='utf-8')
            file_data = json.load(f)
            #file_data is a json Object


            self.module1 = tk.Label(self, text="Module", font=14, fg="black")
            self.module1.place(x=0, y=1)
            self.module2 = tk.Label(self, text=file_data["module"], font=14, fg="black",bg="SlateGray")
            self.module2.place(x=90, y=5)

            self.time1 = tk.Label(self, text="StartTime", font=14, fg="black")
            self.time1.place(x=300, y=8)
            self.time2 = tk.Label(self, text=file_data["Start date"], font=14, fg="black", bg="SlateGray")
            self.time2.place(x=400, y=10)

            self.testname = tk.Label(self, text="TestName", font=14, fg="black")
            self.testname.place(x=0, y=40)
            self.testname2 = tk.Label(self, text=file_data["name"], font=14, fg="black",bg="SlateGray")
            self.testname2.place(x=90, y=45)

            self.time3 = tk.Label(self, text="EndTime", font=14, fg="black")
            self.time3.place(x=300, y=42)
            self.time4 = tk.Label(self, text=file_data["End date"], font=14, fg="black", bg="SlateGray")
            self.time4.place(x=400, y=50)




            d = dict(file_data["QnA"])
            questionobject = []
            choicelist = []
            for item in d.items():
                questionobject.append(item)

            # Q1
            name1 = "Question" + questionobject[0][0]
            q1name = questionobject[0][1]["q"]
            q1chice = []
            q1chice.append(questionobject[0][1]["correctA"])
            for item in questionobject[0][1]["wrongAs"]:
                q1chice.append(item)
            showquest = sorted(q1chice, key=lambda k: k[1])
            self.question1 = tk.Label(self, text=name1, font=14, fg="black")
            self.question1.place(x=0, y=80)
            self.question1show = tk.Label(self, text=q1name, font=14, fg="black")
            self.question1show.place(x=120, y=80)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            choice1 = showquest[0][1].upper()+"."+showquest[0][0]
            choice2 = showquest[1][1].upper()+"."+showquest[1][0]
            choice3 = showquest[2][1].upper()+"."+showquest[2][0]
            choice4 = showquest[3][1].upper()+"."+showquest[3][0]
            self.question1Choise1 = tk.Label(self, text=choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=80)
            self.question1Choise2 = tk.Label(self, text=choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=80)
            self.question1Choise3 = tk.Label(self, text=choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=80)
            self.question1Choise4 = tk.Label(self, text=choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=80)

            # Q2
            name2 = "Question" + questionobject[1][0]
            q2name = questionobject[1][1]["q"]
            q2chice = []
            q2chice.append(questionobject[1][1]["correctA"])
            for item in questionobject[1][1]["wrongAs"]:
                q2chice.append(item)
            showquest2 = sorted(q2chice, key=lambda k: k[1])
            self.question2 = tk.Label(self, text=name2, font=14, fg="black")
            self.question2.place(x=0, y=130)
            self.question2show = tk.Label(self, text=q2name, font=14, fg="black")
            self.question2show.place(x=120, y=130)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q2choice1 = showquest2[0][1].upper() + "." + showquest2[0][0]
            q2choice2 = showquest2[1][1].upper() + "." + showquest2[1][0]
            q2choice3 = showquest2[2][1].upper() + "." + showquest2[2][0]
            q2choice4 = showquest2[3][1].upper() + "." + showquest2[3][0]
            self.question1Choise1 = tk.Label(self, text=q2choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=130)
            self.question1Choise2 = tk.Label(self, text=q2choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=130)
            self.question1Choise3 = tk.Label(self, text=q2choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=130)
            self.question1Choise4 = tk.Label(self, text=q2choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=130)

            # Q3
            name3 = "Question" + questionobject[2][0]
            q3name = questionobject[2][1]["q"]
            q3chice = []
            q3chice.append(questionobject[2][1]["correctA"])
            for item in questionobject[2][1]["wrongAs"]:
                q3chice.append(item)
            showquest3 = sorted(q3chice, key=lambda k: k[1])
            self.question3 = tk.Label(self, text=name3, font=14, fg="black")
            self.question3.place(x=0, y=160)
            self.question3show = tk.Label(self, text=q3name, font=14, fg="black")
            self.question3show.place(x=120, y=160)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q3choice1 = showquest3[0][1].upper() + "." + showquest3[0][0]
            q3choice2 = showquest3[1][1].upper() + "." + showquest3[1][0]
            q3choice3 = showquest3[2][1].upper() + "." + showquest3[2][0]
            q3choice4 = showquest3[3][1].upper() + "." + showquest3[3][0]
            self.question1Choise1 = tk.Label(self, text=q3choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=160)
            self.question1Choise2 = tk.Label(self, text=q3choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=160)
            self.question1Choise3 = tk.Label(self, text=q3choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=160)
            self.question1Choise4 = tk.Label(self, text=q3choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=160)

            # Q4
            name4 = "Question" + questionobject[3][0]
            q4name = questionobject[3][1]["q"]
            q4chice = []
            q4chice.append(questionobject[3][1]["correctA"])
            for item in questionobject[3][1]["wrongAs"]:
                q4chice.append(item)
            showquest4 = sorted(q4chice, key=lambda k: k[1])
            self.question4 = tk.Label(self, text=name4, font=14, fg="black")
            self.question4.place(x=0, y=190)
            self.question4show = tk.Label(self, text=q4name, font=14, fg="black")
            self.question4show.place(x=120, y=190)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q4choice1 = showquest4[0][1].upper() + "." + showquest4[0][0]
            q4choice2 = showquest4[1][1].upper() + "." + showquest4[1][0]
            q4choice3 = showquest4[2][1].upper() + "." + showquest4[2][0]
            q4choice4 = showquest4[3][1].upper() + "." + showquest4[3][0]
            self.question1Choise1 = tk.Label(self, text=q4choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=190)
            self.question1Choise2 = tk.Label(self, text=q4choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=190)
            self.question1Choise3 = tk.Label(self, text=q4choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=190)
            self.question1Choise4 = tk.Label(self, text=q4choice4, font=12, fg="black")
            self.question1Choise4.place(x=1020, y=190)

            # Q5
            name5 = "Question" + questionobject[4][0]
            q5name = questionobject[4][1]["q"]
            q5chice = []
            q5chice.append(questionobject[4][1]["correctA"])
            for item in questionobject[4][1]["wrongAs"]:
                q5chice.append(item)
            showquest5 = sorted(q5chice, key=lambda k: k[1])
            self.question5 = tk.Label(self, text=name5, font=14, fg="black")
            self.question5.place(x=0, y=220)
            self.question5show = tk.Label(self, text=q5name, font=14, fg="black")
            self.question5show.place(x=120, y=220)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q5choice1 = showquest5[0][1].upper() + "." + showquest5[0][0]
            q5choice2 = showquest5[1][1].upper() + "." + showquest5[1][0]
            q5choice3 = showquest5[2][1].upper() + "." + showquest5[2][0]
            q5choice4 = showquest5[3][1].upper() + "." + showquest5[3][0]
            self.question1Choise1 = tk.Label(self, text=q5choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=220)
            self.question1Choise2 = tk.Label(self, text=q5choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=220)
            self.question1Choise3 = tk.Label(self, text=q5choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=220)
            self.question1Choise4 = tk.Label(self, text=q5choice4, font=12, fg="black")
            self.question1Choise4.place(x=1030, y=220)

            # Q6
            name6 = "Question" + questionobject[5][0]
            q6name = questionobject[5][1]["q"]
            q6chice = []
            q6chice.append(questionobject[5][1]["correctA"])
            for item in questionobject[5][1]["wrongAs"]:
                q6chice.append(item)
            showquest6 = sorted(q6chice, key=lambda k: k[1])
            self.question6 = tk.Label(self, text=name6, font=14, fg="black")
            self.question6.place(x=0, y=250)
            self.question6show = tk.Label(self, text=q6name, font=14, fg="black")
            self.question6show.place(x=120, y=250)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q6choice1 = showquest6[0][1].upper() + "." + showquest6[0][0]
            q6choice2 = showquest6[1][1].upper() + "." + showquest6[1][0]
            q6choice3 = showquest6[2][1].upper() + "." + showquest6[2][0]
            q6choice4 = showquest6[3][1].upper() + "." + showquest6[3][0]
            self.question1Choise1 = tk.Label(self, text=q6choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=250)
            self.question1Choise2 = tk.Label(self, text=q6choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=250)
            self.question1Choise3 = tk.Label(self, text=q6choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=250)
            self.question1Choise4 = tk.Label(self, text=q6choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=250)

            # Q7
            name7 = "Question" + questionobject[6][0]
            q7name = questionobject[6][1]["q"]
            q7chice = []
            q7chice.append(questionobject[6][1]["correctA"])
            for item in questionobject[6][1]["wrongAs"]:
                q7chice.append(item)
            showquest7 = sorted(q7chice, key=lambda k: k[1])
            self.question7 = tk.Label(self, text=name7, font=14, fg="black")
            self.question7.place(x=0, y=280)
            self.question7show = tk.Label(self, text=q7name, font=14, fg="black")
            self.question7show.place(x=120, y=280)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q7choice1 = showquest6[0][1].upper() + "." + showquest7[0][0]
            q7choice2 = showquest6[1][1].upper() + "." + showquest7[1][0]
            q7choice3 = showquest6[2][1].upper() + "." + showquest7[2][0]
            q7choice4 = showquest6[3][1].upper() + "." + showquest7[3][0]
            self.question1Choise1 = tk.Label(self, text=q7choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=280)
            self.question1Choise2 = tk.Label(self, text=q7choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=280)
            self.question1Choise3 = tk.Label(self, text=q7choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=280)
            self.question1Choise4 = tk.Label(self, text=q7choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=280)

            # Q8
            name8 = "Question" + questionobject[7][0]
            q8name = questionobject[7][1]["q"]
            q8chice = []
            q8chice.append(questionobject[7][1]["correctA"])
            for item in questionobject[7][1]["wrongAs"]:
                q8chice.append(item)
            showquest8 = sorted(q8chice, key=lambda k: k[1])
            self.question8 = tk.Label(self, text=name8, font=14, fg="black")
            self.question8.place(x=0, y=310)
            self.question8show = tk.Label(self, text=q8name, font=14, fg="black")
            self.question8show.place(x=120, y=310)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q8choice1 = showquest6[0][1].upper() + "." + showquest8[0][0]
            q8choice2 = showquest6[1][1].upper() + "." + showquest8[1][0]
            q8choice3 = showquest6[2][1].upper() + "." + showquest8[2][0]
            q8choice4 = showquest6[3][1].upper() + "." + showquest8[3][0]
            self.question1Choise1 = tk.Label(self, text=q8choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=310)
            self.question1Choise2 = tk.Label(self, text=q8choice2, font=12, fg="black")
            self.question1Choise2.place(x=780, y=310)
            self.question1Choise3 = tk.Label(self, text=q8choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=310)
            self.question1Choise4 = tk.Label(self, text=q8choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=310)

            #Q9
            name9 = "Question" + questionobject[8][0]
            q9name = questionobject[8][1]["q"]
            q9chice = []
            q9chice.append(questionobject[8][1]["correctA"])
            for item in questionobject[8][1]["wrongAs"]:
                q9chice.append(item)
            showquest9 = sorted(q9chice, key=lambda k: k[1])
            self.question9 = tk.Label(self, text=name9, font=14, fg="black")
            self.question9.place(x=0, y=340)
            self.question9show = tk.Label(self, text=q9name, font=14, fg="black")
            self.question9show.place(x=120, y=340)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q9choice1 = showquest6[0][1].upper() + "." + showquest9[0][0]
            q9choice2 = showquest6[1][1].upper() + "." + showquest9[1][0]
            q9choice3 = showquest6[2][1].upper() + "." + showquest9[2][0]
            q9choice4 = showquest6[3][1].upper() + "." + showquest9[3][0]
            self.question1Choise1 = tk.Label(self, text=q9choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=340)
            self.question1Choise2 = tk.Label(self, text=q9choice2, font=12, fg="black")
            self.question1Choise2.place(x=800, y=340)
            self.question1Choise3 = tk.Label(self, text=q9choice3, font=12, fg="black")
            self.question1Choise3.place(x=900, y=340)
            self.question1Choise4 = tk.Label(self, text=q9choice4, font=12, fg="black")
            self.question1Choise4.place(x=1000, y=340)

            # Q10
            name10 = "Question" + questionobject[9][0]
            q10name = questionobject[9][1]["q"]
            q10chice = []
            q10chice.append(questionobject[9][1]["correctA"])
            for item in questionobject[9][1]["wrongAs"]:
                q10chice.append(item)
            showquest10 = sorted(q10chice, key=lambda k: k[1])
            self.question10 = tk.Label(self, text=name10, font=14, fg="black")
            self.question10.place(x=0, y=370)
            self.question10show = tk.Label(self, text=q10name, font=14, fg="black")
            self.question10show.place(x=120, y=370)
            # self.question1Choise = ttk.Combobox(self, textvariable=self.m, width="20")
            # self.question1Choise['values'] = (showquest)
            # self.question1Choise.place(x=800, y=80)
            q10choice1 = showquest6[0][1].upper() + "." + showquest10[0][0]
            q10choice2 = showquest6[1][1].upper() + "." + showquest10[1][0]
            q10choice3 = showquest6[2][1].upper() + "." + showquest10[2][0]
            q10choice4 = showquest6[3][1].upper() + "." + showquest10[3][0]
            self.question1Choise1 = tk.Label(self, text=q10choice1, font=12, fg="black")
            self.question1Choise1.place(x=660, y=370)
            self.question1Choise2 = tk.Label(self, text=q10choice2, font=12, fg="black")
            self.question1Choise2.place(x=800, y=370)
            self.question1Choise3 = tk.Label(self, text=q10choice3, font=12, fg="black")
            self.question1Choise3.place(x=940, y=370)
            self.question1Choise4 = tk.Label(self, text=q10choice4, font=12, fg="black")
            self.question1Choise4.place(x=1040, y=370)

            self.Guide = tk.Label(self, text="Enter Answers: (Eg: A,B,C,D)", font=14, fg="black")
            self.Guide.place(x=0, y=500)
            StudentAnswer = tk.Entry(self, textvariable=self.m, width=100)
            StudentAnswer.place(x=325, y=500)

            anwserlist = tk.Button(self, text="Save Test", font=16,
                                   command=lambda: self.Save(wrapper, StudentAnswer.get()))
            anwserlist.place(x=500, y=760)

            self.StudentID= "12"



            save = tk.Button(self, text="Save Anwser", font=16,
                             command=lambda: self.store(StudentAnswer.get()))
            save.place(x=500, y=525)


            wrapper = {
                "StudentID": self.StudentID,
                "name": file_data["name"],
                "testID": file_data["testID"],
                "module": file_data["module"],

            }


        except Exception as e:
            print(e)
            tk.messagebox.showinfo("", "Please select a test",)

    def store(self, StudentAnswer):
        finalanw = list(StudentAnswer)
        print(StudentAnswer)
        return finalanw

    def Save(self, wrapper,StudentAnswer):
        path = "./Student/summative"
        final = self.store(StudentAnswer)
        saves = []
        print(final)
        for item in final:
            if str(item)!=",":
                saves.append(item)
        # finalanwser = final.remove(",")
        wrapper["anwsers"] = saves
        import datetime
        end_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%H:%M %d-%m-%Y")
        wrapper["finish_time"] = end_time
        print(wrapper)

        filename = "%s/%s %s.json" % (path, wrapper["StudentID"], wrapper["testID"])
        with open(filename, "w") as outfile:
            json.dump(wrapper, outfile, indent=4)
        tk.messagebox.showinfo("", "Test has been Submitted")
        return



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
        for F in (ORPage, FormativeResultsPage, SummativeResultsPage, PythonFormative, JavaFormative, WebDevFormative,
                  CompSysFormative, PythonFormative1, PythonFormativeFeedback,
                  PythonSummative, JavaSummative, WebDevSummative, CompSysSummative, JavaSummative1,
                  JavaSummativeFeedback):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ORPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ORPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font=headerFont)
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
        label = tk.Label(self, text="Formative Test Results", font=headerFont)
        label.pack(pady=10, padx=10)

        moduleLabel = tk.Label(self, text="Choose Test Module:", fg="#807682", font=subHeaderFont)
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

        label = tk.Label(self, text="Python Formative Test Results Available:", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        buttonTest = tk.Button(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=buttonFont,
                               bg="#C6DDF5",
                               command=lambda: controller.show_frame(PythonFormative1))
        buttonTest.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=standardFont,
                            command=lambda: controller.show_frame(FormativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=standardFont,
                            command=lambda: controller.show_frame(ORPage))
        button2.pack()


# Python Formative Test Results for test 1
class PythonFormative1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userID = '102'

        with open('studentAnswers.json', 'r') as f:
            data = json.load(f)

            # access just the answer list
            for i in data['testID']:
                if i['studentID'] == userID:
                    answers = i['Test']['answers']
                    break
                else:
                    print("Not found")

        #### CORRECT FILE PATH NEEDS TO BE SET ###
        with open('Python General Knowledge.json', 'r') as file:
            testData = json.load(file)

        # Create a list of correct answers from the json
        correctList = []
        for i in range(1, 11):
            correctList.append(testData["QnA"][str(i)]["correctA"])

        labelTitle = tk.Label(self, text='Results for Test: {} - {}'.format(testData["testID"], testData["name"]), font=subHeaderFont, fg='#8A5A76')
        labelTitle.pack(pady=2)


        mark = 0


        for i in range(10):
            if correctList[i][1] == answers[i]:
                mark += 1

                # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
                # labelQ.pack(pady=1, padx=2)

                labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tCorrect", font=standardFont, anchor='w', width=100)
                labelA.pack(pady=1, padx=2)

                labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", fg='#ebebeb')
                labelDash.pack()

            else:

                # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
                # labelQ.pack(pady=1, padx=2)

                labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tIncorrect", font=standardFont, anchor='w', width=100)
                labelA.pack(padx=2)

                labelC = tk.Label(self, text="\t\t\t\t\t\t\t\tCorrect answer was: {}) {}".format(correctList[i][1], correctList[i][0]), fg="#57526B", font=answersFont, anchor='w', width=100)
                labelC.pack()

                labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", fg='#ebebeb')
                labelDash.pack()



        labelTotal = tk.Label(self, text="Total Mark: " + str(mark) + "/10", fg="#8A5A76", font=standardFont)
        labelTotal.pack()

        print("Total Mark: " , mark,"/10")



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

        label = tk.Label(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=headerFont)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Feedback for test", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        # Create a list of the test questions
        questionList = []
        for i in range(1, 11):
            questionList.append(testData["QnA"][str(i)]["q"])

        # Create a list of the test feedback
        feedback = []
        for i in range(1, 11):
            feedback.append(testData["QnA"][str(i)]["feedback"])

        for i in range(10):
            # if questionList[i] == feedback[i]:

            labelQ = tk.Label(self, text="Question " + str(i + 1) + ") {}".format(questionList[i]), fg="#57526B", font=answersFont)
            labelQ.pack(pady=0, padx=2)

            labelF = tk.Label(self, text="{}".format(feedback[i]), font=answersFont)
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

        label = tk.Label(self, text="Java: Formative Test Results", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont)
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

        label = tk.Label(self, text="Web Development: Formative Test Results", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont)
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

        label = tk.Label(self, text="Computational Systems: Formative Test Results", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont)
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
        label = tk.Label(self, text="Sumamtive Test Results", font=headerFont)
        label.pack(pady=10, padx=10)

        moduleLabel = tk.Label(self, text="Choose Test Module:", fg="#807682", font=subHeaderFont)
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

        label = tk.Label(self, text="Python: Summative Test Results", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont)
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

        label = tk.Label(self, text="Java Summative Test Results Available:", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        buttonTest = tk.Button(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=buttonFont,
                               bg="#C6DDF5",
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

        with open('studentAnswers.json', 'r') as f:
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
        for i in range(1, 11):
            correctList.append(testData["QnA"][str(i)]["correctA"])

        labelTitle = tk.Label(self, text='Results for Test: {} - {}'.format(testData["testID"], testData["name"]), font=subHeaderFont, fg='#8A5A76')
        labelTitle.pack(pady=2)


        mark = 0

        for i in range(10):
            if correctList[i][1] == answers[i]:
                mark += 1

                # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
                # labelQ.pack(pady=1, padx=2)

                labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tCorrect", font=standardFont, anchor='w', width=100)
                labelA.pack(pady=1, padx=2)

                labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", fg='#ebebeb')
                labelDash.pack()

            else:

                # labelQ = tk.Label(self, text="Question " + str(i+1), fg="#57526B", bg='white', font=standardFont)
                # labelQ.pack(pady=1, padx=2)

                labelA = tk.Label(self, text="Question " + str(i+1) + ") Your answer: " + answers[i] + "\t\t\t\t\t\tIncorrect", font=standardFont, anchor='w', width=100)
                labelA.pack(padx=2)

                labelC = tk.Label(self, text="\t\t\t\t\t\t\t\tCorrect answer was: {}) {}".format(correctList[i][1], correctList[i][0]), fg="#57526B", font=answersFont, anchor='w', width=100)
                labelC.pack()

                labelDash = tk.Label(self, text="_________________________________________________________________________________________________________", fg='#ebebeb')
                labelDash.pack()

        labelTotal = tk.Label(self, text="Total Mark: " + str(mark) + "/10", fg="#8A5A76", font=standardFont)
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

        label = tk.Label(self, text="Test {}: {}".format(testData["testID"], testData["name"]), font=headerFont)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Feedback for test", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        # Create a list of the test questions
        questionList = []
        for i in range(1, 11):
            questionList.append(testData["QnA"][str(i)]["q"])

        # Create a list of the test feedback
        feedback = []
        for i in range(1, 11):
            feedback.append(testData["QnA"][str(i)]["feedback"])

        for i in range(10):
            # if questionList[i] == feedback[i]:

            labelQ = tk.Label(self, text="Question " + str(i + 1) + ") {}".format(questionList[i]), fg="#57526B", font=answersFont)
            labelQ.pack(pady=0, padx=2)

            labelF = tk.Label(self, text="{}".format(feedback[i]), font=answersFont)
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

        label = tk.Label(self, text="Web Development: Summative Test Results", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont)
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

        label = tk.Label(self, text="Computational Systems: Summative Test Results", font=subHeaderFont)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="There are currently no test results available.", font=standardFont)
        label.pack(pady=40, padx=10)

        button1 = tk.Button(self, text="Back", font=buttonFont,
                            command=lambda: controller.show_frame(SummativeResultsPage))
        button1.pack()
        button2 = tk.Button(self, text="Home", font=buttonFont,
                            command=lambda: controller.show_frame(ORPage))
        button2.pack(pady=10)


if __name__ == "__main__":
    app = TestTakeApp()
    app.mainloop()