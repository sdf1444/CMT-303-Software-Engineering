from tkinter import *
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from src_ClassTest import Test
import json
import os, sys
import random
from takeTestInterface import TestTakeApp
from core.engine import load_modules, load_test_ids, make_plot
import matplotlib as plt
import tkinter as tk

QUIZES_DATA = "data/quizes.json"
headingfont = ('Helvetica ', 50)
labelfont = ('Helvetica ', 16)

class addQuestion(Test):
    pass
class TestCreaterApp(tk.Tk):

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
        for F in (LoginPage, StudentLogin, StaffLogin, Register, StartPage, TestPage, ManageTest, FormativeTest, SummativeTest, OpenFormativeTest, OpenSummativeTest):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Pput all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")
        self.geometry('1200x800')

    def show_frame(self, page_name):
        # Show a frame for the given page name.
        frame = self.frames[page_name]
        frame.tkraise()

    def open_file(self, path):
        # Open the file with the path.
        with open('path', 'w') as f:
            pass

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        heading = tk.Label(self, text="Home", font=headingfont)
        # heading.config(self,height=3, width=20, font=headingfont)
        heading.place(x=500, y=0)
        login = tk.Button(self, text="Login for Student", font=labelfont, command=lambda: controller.show_frame("StudentLogin"))
        login.place(x=500, y=100)
        login2 = tk.Button(self, text="Login for Staff", font=labelfont, command=lambda: controller.show_frame("StaffLogin"))
        login2.place(x=500, y=300)
        register = tk.Button(self,text="Register", font=labelfont, command=lambda: controller.show_frame("Register"))
        register.place(x=520, y=510)

class StudentLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heading = tk.Label(self, text="Login",font=headingfont)
        self.Username = tk.Label(self, text="Username",font=labelfont)
        self.Password = tk.Label(self, text="Password",font=labelfont)
        self.uname = tk.Entry(self)
        self.pw = tk.Entry(self,show="*")
        self.status = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", font=labelfont, command=self.login)
        self.reset = tk.Button(self, text="Reset", font=labelfont, command=self.clear)

        self.heading.place(x=500, y=100)
        self.Username.place(x=400, y=200)
        self.Password.place(x=400, y=240)
        self.uname.place(x=500, y=200, height=40, width=400)
        self.pw.place(x=500, y=240, height=40, width=400)
        self.submit.place(x=400, y=300)
        self.reset.place(x=900, y=300)
    def clear(self):
        self.uname.delete(0, END)
        self.pw.delete(0, END)

    def login(self):
        if (self.uname.get() == "" or self.pw.get() == ""):
            messagebox.showwarning("Error!","Username or Password or Status cannot be empty!",parent=self)
        else:
            u = self.uname.get()
            p = self.pw.get()
            try:
                with open("./User/Student/155420906671.json", "rb") as fp:
                    while True:
                        try:
                            s = json.load(fp)
                            # b = pickle.load(fp)
                            if(s['UserName'] == u):
                                if(s['Password'] == p):
                                    messagebox.showinfo("Success!","Hello " + str(u) + "! Welcome to Interface!",parent=self)
                                    app = TestTakeApp()
                                    app.geometry('1200x800')
                                    app.mainloop()

                                    break
                                else:
                                    messagebox.showinfo("Error","Password is wrong")

                            else:
                                messagebox.showinfo("Error","Username is wrong")
                        except Exception as e:
                            print(e)
                            # messagebox.showwarning("Failed!","Sorry. User not found!",parent=self)
                            break
                self.clear()
            except:
                messagebox.showwarning("Database Empty!","No users were found. Please Register.",parent=self)

                self.destroy()

class StaffLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heading = tk.Label(self, text="Login", font=headingfont)
        self.Username = tk.Label(self, text="Username", font=labelfont)
        self.Password = tk.Label(self, text="Password", font=labelfont)
        self.uname = tk.Entry(self)
        self.pw = tk.Entry(self,show="*")
        self.status = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", font=labelfont, command=self.login)
        self.reset = tk.Button(self, text="Reset", font=labelfont, command=self.clear)

        self.heading.place(x=500, y=100)
        self.Username.place(x=400, y=200)
        self.Password.place(x=400, y=240)
        self.uname.place(x=500, y=200, height=40, width=400)
        self.pw.place(x=500, y=240, height=40, width=400)
        self.submit.place(x=400, y=300)
        self.reset.place(x=900, y=300)
    def clear(self):
        self.uname.delete(0, END)
        self.pw.delete(0, END)

    def login(self):
        if (self.uname.get() == "" or self.pw.get() == ""):
            messagebox.showwarning("Error!","Username or Passwod or Status cannot be empty!",parent=self)
        else:
            u = self.uname.get()
            p = self.pw.get()
            try:
                test_list = []
                path = "./User/Staff"
                with open("./User/Staff/155421142187.json", "rb") as fp:
                    print("heh")
                    while True:
                        try:
                            s = json.load(fp)
                            # b = pickle.load(fp)
                            if(s['UserName'] == u):
                                if(s['Password'] == p):
                                    messagebox.showinfo("Success!","Hello " + str(u) + "! Welcome to Interface!",parent=self)
                                    self.controller.show_frame("StartPage")
                                else:
                                    messagebox.showinfo("Error","Password is wrong")

                            else:
                                messagebox.showinfo("Error","Username is wrong")

                        except Exception as e:
                            print(e)
                            # messagebox.showwarning("Failed!","Sorry. User not found!",parent=self)
                            break
                self.clear()
            except:
                messagebox.showwarning("Database Empty!","No users were found. Please Register.",parent=self)

                self.destroy()

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heading = tk.Label(self, text="Register", font=headingfont)
        self.Username = tk.Label(self, text="Username",font=labelfont)
        self.Password = tk.Label(self, text="Password",font=labelfont)
        self.Status = tk.Label(self, text = "Status",font=labelfont)
        self.uname = tk.Entry(self)
        self.pw = tk.Entry(self,show="*")
        self.status = tk.Entry(self)
        from time import time
        self.id = str(int(time()*100))
        self.submit = tk.Button(self, text="Submit", font=labelfont, command=self.insert)
        self.reset = tk.Button(self, text="Reset", font=labelfont, command=self.clear)

        self.heading.place(x=500, y=100)
        self.Username.place(x=400, y=200)
        self.Password.place(x=400, y=240)
        self.Status.place(x=400, y=280)
        self.uname.place(x=500, y=200, height=40, width=400)
        self.pw.place(x=500, y=240, height=40, width=400)
        self.status.place(x=500, y=280, height=40, width=400)
        self.submit.place(x=400, y=350)
        self.reset.place(x=900, y=350)

    def clear(self):
        self.uname.delete(0, END)
        self.pw.delete(0, END)

    def user_wrapper(self):
        """Main wrapper functions.  Converts the class into a dictionary
        :return wrapper: Dict of class Test instance"""
        wrapper = {'UserID': self.id,
                   'UserName':  self.uname.get(),
                   'Password':self.pw.get(),
                   'Status':self.status.get()}
        return wrapper

    def insert(self):
        #f = open('file.txt','a')
        if (
            self.uname.get() == "" or
            self.pw.get() == ""
           ):
            messagebox.showwarning("Empty Input!","Please fill all the details.",parent=self)
        if(
                self.status.get() not in ["Student","Staff"]
        ):
            messagebox.showwarning("Empty Input!", "Please ensure Status with Student or Staff.", parent=self)

        else:
                if (self.status.get()== "Student"):
                   path = "./User/Student"
                   saveUser = self.user_wrapper()
                   filename = "%s/%s.json" % (path, self.id)
                   with open(filename, "w") as outfile:
                      json.dump(saveUser, outfile, indent=4)
                      messagebox.showinfo("Account created.","Please login using new credentials. :)",parent=self)
                   self.root.destroy()

                if (self.status.get()== "Staff"):
                   path = "./User/Staff"
                   saveUser = self.user_wrapper()
                   filename = "%s/%s.json" % (path, self.id)
                   with open(filename, "w") as outfile:
                      json.dump(saveUser, outfile, indent=4)
                      messagebox.showinfo("Account created.","Please login using new credentials. :)",parent=self)
                   self.destroy()

class StartPage(tk.Frame):
    # First page of GUI.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Create Test", font=16, command=lambda: controller.show_frame("TestPage"))
        button1.place(x=550, y=200)

        button2 = tk.Button(self, text="Manage Test", font=16, command=lambda: controller.show_frame("ManageTest"))
        button2.place(x=550, y=400)

        button3 = tk.Button(self, text="View Test Results", font=16, command=self.staff)
        button3.place(x=550, y=600)

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)

    def quit(self):
        # When logout clicked application quits.
        self.destroy()
    def staff(self):
        # self.root = tk.Tk()
        # self.root.title("Modules")
        # self.root.geometry('{}x{}'.format(1200, 800))
        # self.root.resizable(width=True, height=True)
        self.app1 = ModulesChooser()
        self.app.geometry('1200x800')

        self.app1.mainloop()

class TestPage(tk.Frame):
    # Page to choose formative or summative test.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.controller.title("Create Test2")
        button1 = tk.Button(self, text="Formative Test", font=16,
                            command=lambda: controller.show_frame("FormativeTest"))
        button1.place(x=550, y=200)

        button2 = tk.Button(self, text="Summative Test", font=16,
                            command=lambda: controller.show_frame("SummativeTest"))
        button2.place(x=550, y=400)

        button3 = tk.Button(self, text="Back", font=16, command=lambda: controller.show_frame("StartPage"))
        button3.place(x=0, y=760)

        logout = tk.Button(self, text="Logout", font=16, command=quit)
        logout.place(x=1125, y=760)

    def quit(self):
        # When logout clicked application quits.
        self.destroy()

class Test2(tk.Frame):
    # Form for formative or summative test.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.is_save = False
        self.controller = controller
        self.t = StringVar()
        self.m = StringVar()
        self.b = StringVar()
        self.q = StringVar()
        self.c = StringVar()
        self.w_1 = StringVar()
        self.w_2 = StringVar()
        self.w_3 = StringVar()
        self.sd = StringVar()
        self.ed = StringVar()
        self.module1 = tk.Label(self, text="Module", font=14, fg="black")
        self.module1.place(x=0, y=1)
        self.module2 = ttk.Combobox(self, textvariable=self.m)
        self.module2['values'] = ("Python", "Java", "Web development", "Computational Systems")
        self.module2.place(x=125, y=5)
        self.test_number = 1
        self.testname = tk.StringVar(value="Test Name")
        self.testname1 = tk.Label(self, font=14, fg="black", textvariable=self.testname)
        self.testname1.place(x=0, y=60)
        self.testname2 = tk.Entry(self, textvariable=self.t)
        self.testname2.place(x=125, y=65)

        self.question_number = 1
        self.current_question_number = 1
        self.question_number_text = tk.StringVar(value="Question #" + str(self.question_number))
        self.question1 = tk.Label(self, font=14, fg="black",textvariable=self.question_number_text)
        self.question1.place(x=0, y=120)
        self.question2 = tk.Entry(self, textvariable=self.q)
        self.question2.place(x=125, y=126)

        self.correct = tk.Label(self, text="Correct", font=14, fg="black")
        self.correct.place(x=0, y=180)
        self.correct1 = tk.Entry(self, textvariable=self.c)
        self.correct1.place(x=125, y=188)
        self.incorrect1 = tk.Label(self, text="Incorrect", font=14, fg="black")
        self.incorrect1.place(x=0, y=240)
        self.incorrect4 = tk.Entry(self, textvariable=self.w_1)
        self.incorrect4.place(x=125, y=246)
        self.incorrect2 = tk.Label(self, text="Incorrect", font=14, fg="black")
        self.incorrect2.place(x=0, y=300)
        self.incorrect5 = tk.Entry(self, textvariable=self.w_2)
        self.incorrect5.place(x=125, y=306)
        self.incorrect3 = tk.Label(self, text="Incorrect", font=14, fg="black")
        self.incorrect3.place(x=0, y=360)
        self.incorrect6 = tk.Entry(self, textvariable=self.w_3)
        self.incorrect6.place(x=125, y=366)

        self.answers = []
        self.answers.append(self.correct1)
        self.answers.append(self.incorrect4)
        self.answers.append(self.incorrect5)
        self.answers.append(self.incorrect6)

        self.mark = tk.Label(self, text="Mark", font=14, fg="black")
        self.mark.place(x=0, y=420)
        e = StringVar()
        self.mark1 = tk.Entry(self, textvariable=e)
        e.set(1)
        self.mark1.place(x=125, y=426)

        self.feedback = tk.Label(self, text="Feedback", font=14, fg="black")
        self.feedback.place(x=0, y=480)
        self.feedback1 = tk.Entry(self, textvariable=self.b)
        self.feedback1.place(x=125, y=486)

        self.add = tk.Button(self, text="Save Question(must click after each question is created)", font=16, fg="black",
                             command=self.save_question)
        self.add.place(x=250, y=690)

        self.add = tk.Button(self, text="Add another question", font=16, fg="black", command=self.add_question)
        self.add.place(x=300, y=0)

        self.previous = tk.Button(self, text="previous", font=16, fg="black", command=self.show_previuos)
        self.previous.place(x=0, y=690)

        self.next = tk.Button(self, text="next", font=16, fg="black", command=self.show_next)
        self.next.place(x=150, y=690)

        # self.edit = tk.Button(self, text="Edit Question", command=self.edit)
        # self.edit.place(x=470, y=2)

        self.delete = tk.Button(self, text="Delete Question", font=16, fg="black", command=self.delete)
        self.delete.place(x=300, y=55)

        self.release = tk.Button(self, text="Release test", font=16, fg="black", command=self.release)
        self.release.place(x=0, y=755)

        self.save = tk.Button(self, text="Save test", font=16, fg="black", command=self.save)
        self.save.place(x=200, y=755)

        self.back = tk.Button(self, text="Back", font=16, fg="black", command=self.back)
        self.back.place(x=400, y=755)

        self.loggout = tk.Button(self, text="Logout", font=16, fg="black", command=quit)
        self.loggout.place(x=600, y=755)

        self.quiz = None
        self.attempts1 = None
        self.unlimitedattempts = None
        self.previous['state'] = 'disabled'
        self.next['state'] = 'disabled'

    # def answer(self, y):
    #     self.answers.append(tk.Entry(self, textvariable=self.a))
    #     self.answers[-1].place(x=70, y=y)

    def save_question(self):
        # Save needs to be clicked after each question created.
        # print("Question",self.question2.get(),"answer: ",self.answers[0].get())
        if self.question_number == len(self.quiz.Questions) + 1:
            self.is_save = True
        else:
            self.is_save = False
        ansOptions = []
        for i in range(len(self.answers)):
            ansOptions.append(self.answers[i].get())
        print(self.is_save, 'before, before')
        self.quiz.addQuestion(self.is_save, self.question_number, self.question2.get(), ansOptions[0], ansOptions[1],
                              ansOptions[2], ansOptions[3],
                              mark=self.mark1.get(), feedback=self.feedback1.get())
        tk.messagebox.showinfo("", "Question saved")
        # self.is_save = True

        print("=" * 30)
        print(self.quiz.Questions)

    def get_is_save(self):
        return self.is_save

    def get_current_question_number(self):
        return self.current_question_number

    def add_question(self):
        # Add another question button
        question_numbers = list(self.quiz.Questions.keys())

        if len(question_numbers) == 0:
            self.question_number = 1
        else:
            self.question_number = question_numbers[len(question_numbers) - 1] + 1
        self.current_question_number = self.question_number
        self.question_number_text.set("Question #" + str(self.question_number))
        self.question2.delete(0, END)
        self.answers[0].delete(0, END)
        self.answers[1].delete(0, END)
        self.answers[2].delete(0, END)
        self.answers[3].delete(0, END)
        self.is_save = True
        self.next['state'] = 'disabled'
        self.previous['state'] = 'normal'
        self.feedback1.delete(0, END)
        # self.enable_disable_button()
        tk.messagebox.showinfo("", "Another question added")

    def quit(self):
        # When logout clicked application quits.
        self.destroy()

    def enable_disable_button(self):
        # When question is 1 previous button disabled.
        question_numbers = list(self.quiz.Questions.keys())
        if len(self.quiz.Questions) == 0 or self.question_number == question_numbers[0]:
            self.previous['state'] = 'disabled'
        else:
            # When not question  1 previous button is active.
            self.previous['state'] = 'normal'

        if len(self.quiz.Questions) == 0 or self.question_number == question_numbers[len(question_numbers) - 1]:
            self.next['state'] = 'disabled'
        else:
            self.next['state'] = 'normal'

    def fill_question(self, ques, c_answer, w_answer, mk, fedk):
        # Fill form when previous and next button clicked to show other questions.
        self.question2.delete(0, END)
        self.question2.insert(0, ques)
        self.answers[0].delete(0, END)
        correct = c_answer
        wrong = w_answer
        mark = mk
        feedback = fedk
        self.answers[0].insert(0, correct)
        self.answers[1].delete(0, END)
        self.answers[1].insert(0, wrong[0][0])
        self.answers[2].delete(0, END)
        self.answers[2].insert(0, wrong[1][0])
        self.answers[3].delete(0, END)
        self.answers[3].insert(0, wrong[2][0])
        self.mark1.delete(0, END)
        self.mark1.insert(0, mark)
        self.feedback1.delete(0, END)
        self.feedback1.insert(0, feedback)

    def show_previuos(self):
        # What happens when previous button is clicked.
        print(self.question_number)
        print(list(self.quiz.Questions.keys()))
        print(self.question_number in list(self.quiz.Questions.keys()))
        question_numbers = list(self.quiz.Questions.keys())

        if len(self.quiz.Questions) > 1 and question_numbers[0] != self.question_number:
            self.question_number = question_numbers[question_numbers.index(self.question_number) - 1]
            # print(self.quiz.Questions[self.question_number - 1]['correctA'][0])
            # print("prev Q no:",self.question_number)
            self.fill_question(self.quiz.Questions[self.question_number]['q'],
                               self.quiz.Questions[self.question_number]['correctA'][0],
                               self.quiz.Questions[self.question_number]['wrongAs'],
                               self.quiz.Questions[self.question_number]['mark'],
                               self.quiz.Questions[self.question_number]['feedback'])

            self.question_number_text.set("Question #" + str(self.question_number))
            self.enable_disable_button()
            self.is_save = False
            # self.current_question_number = self.current_question_number - 1

    def delete(self):
        question_numbers = list(self.quiz.Questions.keys())

        if len(question_numbers) == 2:
            self.previous['state'] = 'disabled'
            self.next['state'] = 'disabled'

        if self.question_number == question_numbers[0]:

            if len(question_numbers) == 1:
                self.quiz.Questions.pop(self.question_number, None)
                self.question_number = 1
                self.question_number_text.set("Question #" + str(1))
                self.question2.delete(0, END)
                self.answers[0].delete(0, END)
                self.answers[1].delete(0, END)
                self.answers[2].delete(0, END)
                self.answers[3].delete(0, END)
                self.is_save = True
                self.feedback1.delete(0, END)
                self.previous['state'] = 'disabled'
            else:
                question_numbers.pop()
                self.question_number = question_numbers[0]
                for m in range(len(self.quiz.Questions) - 1):
                    self.quiz.Questions[m + 1] = self.quiz.Questions[m + 2]
                self.quiz.Questions.pop(len(self.quiz.Questions))
                self.fill_question(self.quiz.Questions[self.question_number]["q"],
                                   self.quiz.Questions[self.question_number]["correctA"][0],
                                   self.quiz.Questions[self.question_number]["wrongAs"],
                                   self.quiz.Questions[self.question_number]["mark"],
                                   self.quiz.Questions[self.question_number]["feedback"])
                self.question_number_text.set("Question #" + str(1))
                self.is_save = False

        elif self.question_number == question_numbers[-1] and len(question_numbers) > 1:
            question_numbers.pop(-1)
            self.question_number = question_numbers[-1]
            self.quiz.Questions.pop(self.question_number + 1)
            self.fill_question(self.quiz.Questions[self.question_number]["q"],
                               self.quiz.Questions[self.question_number]["correctA"][0],
                               self.quiz.Questions[self.question_number]["wrongAs"],
                               self.quiz.Questions[self.question_number]["mark"],
                               self.quiz.Questions[self.question_number]["feedback"])
            self.question_number_text.set("Question #" + str(self.question_number))
            self.is_save = False

        else:
            question_numbers.pop(-1)
            for m in range(len(self.quiz.Questions) - 2):
                self.quiz.Questions[self.question_number + m] = self.quiz.Questions[self.question_number + m + 1]
            self.quiz.Questions.pop(len(question_numbers) + 1)
            self.question_number -= 1
            self.fill_question(self.quiz.Questions[self.question_number]["q"],
                               self.quiz.Questions[self.question_number]["correctA"][0],
                               self.quiz.Questions[self.question_number]["wrongAs"],
                               self.quiz.Questions[self.question_number]["mark"],
                               self.quiz.Questions[self.question_number]["feedback"])
            self.question_number_text.set("Question #" + str(self.question_number))
            self.is_save = False
            if self.question_number == 1:
                self.previous['state'] = 'disabled'

        tk.messagebox.showinfo("", "Question deleted")

    def show_next(self):
        # What happens when next button is clicked.
        question_numbers = list(self.quiz.Questions.keys())
        print(question_numbers)
        if self.question_number == question_numbers[len(question_numbers) - 1]:
            # print(" last Q no:",self.question_number)
            self.question2.delete(0, END)
            self.answers[0].delete(0, END)
            self.answers[1].delete(0, END)
            self.answers[2].delete(0, END)
            self.answers[3].delete(0, END)
            self.enable_disable_button()
            self.mark1.delete(0, END)
            self.feedback1.delete(0, END)
            self.is_save = False
            self.question_number = self.question_number + 1
            self.question_number_text.set("Question #" + str(self.question_number))

        if self.question_number < question_numbers[len(question_numbers) - 1]:
            # print("next Q no:",self.question_number)
            self.question_number = question_numbers[question_numbers.index(self.question_number) + 1]
            self.fill_question(self.quiz.Questions[self.question_number]['q'],
                               self.quiz.Questions[self.question_number]['correctA'][0],
                               self.quiz.Questions[self.question_number]['wrongAs'],
                               self.quiz.Questions[self.question_number]['mark'],
                               self.quiz.Questions[self.question_number]['feedback'])
            self.enable_disable_button()
            self.is_save = False
            self.question_number_text.set("Question #" + str(self.question_number))

    def managetest_save_question(self, file_data):
        print(file_data)
        ansOptions = []
        for i in range(len(self.answers)):
            ansOptions.append(self.answers[i].get())

        if self.question_number == len(file_data["QnA"]) + 1:
            newquestion = True
        else:
            newquestion = False

        if newquestion:
            options = ["a", "b", "c", "d"]
            r = random.randint(0, 3)
            if r == 0: letter = "a"
            if r == 1: letter = "b"
            if r == 2: letter = "c"
            if r == 3: letter = "d"
            wrong = (ansOptions[1], ansOptions[2], ansOptions[3])
            wrong_shuffle = random.sample(wrong, len(wrong))
            options.remove(letter)
            wrong_letters = list(zip(wrong_shuffle, options))

            file_data["QnA"][str(self.question_number)] = {"q": self.question2.get(),
                                                           "correctA": [ansOptions[0], letter],
                                                           "wrongAs": wrong_letters, "mark": self.mark1.get(),
                                                           "feedback": self.feedback1.get()}

        else:
            file_data["QnA"][str(self.question_number)]["q"] = self.question2.get()
            file_data["QnA"][str(self.question_number)]["correctA"][0] = ansOptions[0]
            file_data["QnA"][str(self.question_number)]["wrongAs"][0][0] = ansOptions[1]
            file_data["QnA"][str(self.question_number)]["wrongAs"][1][0] = ansOptions[2]
            file_data["QnA"][str(self.question_number)]["wrongAs"][2][0] = ansOptions[3]
            file_data["QnA"][str(self.question_number)]["mark"] = self.mark1.get()
            file_data["QnA"][str(self.question_number)]["feedback"] = self.feedback1.get()

        for m in range(len(file_data["QnA"])):
            ansOptions = []
            ansOptions.append(file_data["QnA"][str(m + 1)]["correctA"][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][0][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][1][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][2][0])
            self.quiz.addQuestion(False, m + 1, file_data["QnA"][str(m + 1)]["q"],
                                  file_data["QnA"][str(m + 1)]["correctA"][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][0][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][1][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][2][0],
                                  mark=file_data["QnA"][str(m + 1)]["mark"],
                                  feedback=file_data["QnA"][str(m + 1)]["feedback"])

        print(file_data)
        tk.messagebox.showinfo("", "Question saved")

    def managetest_add_question(self, file_data):
        # Add another question button
        question_numbers = []
        for i in file_data["QnA"].keys():
            question_numbers.append(int(i))

        if len(question_numbers) == 0:
            self.question_number = 1
        else:
            self.question_number = question_numbers[len(question_numbers) - 1] + 1

        self.current_question_number = self.question_number
        self.question_number_text.set("Question #" + str(self.question_number))
        self.question2.delete(0, END)
        self.answers[0].delete(0, END)
        self.answers[1].delete(0, END)
        self.answers[2].delete(0, END)
        self.answers[3].delete(0, END)
        self.is_save = True
        self.feedback1.delete(0, END)
        self.next['state'] = 'disabled'
        self.previous['state'] = 'normal'
        tk.messagebox.showinfo("", "Another question added")

    def managetest_show_previuos(self, path):
        # What happens when previous button is clicked.
        self.next['state'] = 'normal'
        self.add['state'] = 'disabled'
        self.question_number = self.question_number - 1
        self.question_number_text.set("Question #" + str(self.question_number))
        self.fill_question(path["QnA"][str(self.question_number)]["q"],
                           path["QnA"][str(self.question_number)]["correctA"][0],
                           path["QnA"][str(self.question_number)]["wrongAs"],
                           path["QnA"][str(self.question_number)]["mark"],
                           path["QnA"][str(self.question_number)]["feedback"])
        try:
            path["QnA"][str(self.question_number - 1)]

        except Exception as e:
            self.previous['state'] = 'disabled'

        try:
            path["QnA"][str(self.question_number + 1)]


        except Exception as e:
            self.next['state'] = 'disabled'
            self.add['state'] = 'normal'

    def managetest_show_next(self, path):
        self.previous['state'] = 'normal'
        # What happens when next button is clicked.
        self.question_number = self.question_number + 1
        self.question_number_text.set("Question #" + str(self.question_number))

        self.fill_question(path["QnA"][str(self.question_number)]["q"],
                           path["QnA"][str(self.question_number)]["correctA"][0],
                           path["QnA"][str(self.question_number)]["wrongAs"],
                           path["QnA"][str(self.question_number)]["mark"],
                           path["QnA"][str(self.question_number)]["feedback"])

        try:
            path["QnA"][str(self.question_number + 1)]

        except Exception as e:
            self.next['state'] = 'disabled'
            self.add['state'] = 'normal'

    def managetest_delete(self, file_data):
        question_numbers = []
        for i in file_data["QnA"].keys():
            question_numbers.append(int(i))

        if len(question_numbers) == 2:
            self.previous['state'] = 'disabled'
            self.next['state'] = 'disabled'

        if self.question_number == question_numbers[0]:

            if len(question_numbers) == 1:
                file_data["QnA"].pop(str(self.question_number), None)
                self.question_number = 1
                self.question_number_text.set("Question #" + str(1))
                self.question2.delete(0, END)
                self.answers[0].delete(0, END)
                self.answers[1].delete(0, END)
                self.answers[2].delete(0, END)
                self.answers[3].delete(0, END)
                self.is_save = True
                self.feedback1.delete(0, END)
                self.previous['state'] = 'disabled'
            else:
                question_numbers.pop()
                self.question_number = question_numbers[0]
                for m in range(len(file_data["QnA"]) - 1):
                    file_data["QnA"][str(m + 1)] = file_data["QnA"][str(m + 2)]
                file_data["QnA"].pop(str(len(file_data["QnA"])))
                self.fill_question(file_data["QnA"][str(self.question_number)]["q"],
                                   file_data["QnA"][str(self.question_number)]["correctA"][0],
                                   file_data["QnA"][str(self.question_number)]["wrongAs"],
                                   file_data["QnA"][str(self.question_number)]["mark"],
                                   file_data["QnA"][str(self.question_number)]["feedback"])
                self.question_number_text.set("Question #" + str(1))
                self.is_save = False

        elif self.question_number == question_numbers[-1] and len(question_numbers) > 1:
            question_numbers.pop(-1)
            self.question_number = question_numbers[-1]
            file_data["QnA"].pop(str(self.question_number + 1))
            self.fill_question(file_data["QnA"][str(self.question_number)]["q"],
                               file_data["QnA"][str(self.question_number)]["correctA"][0],
                               file_data["QnA"][str(self.question_number)]["wrongAs"],
                               file_data["QnA"][str(self.question_number)]["mark"],
                               file_data["QnA"][str(self.question_number)]["feedback"])
            self.question_number_text.set("Question #" + str(self.question_number))
            self.is_save = False

        else:
            question_numbers.pop(-1)
            for m in range(len(file_data["QnA"]) - 2):
                file_data["QnA"][str(self.question_number + m)] = file_data["QnA"][str(self.question_number + m + 1)]
            file_data["QnA"].pop(str(len(question_numbers) + 1))
            self.question_number -= 1
            self.fill_question(file_data["QnA"][str(self.question_number)]["q"],
                               file_data["QnA"][str(self.question_number)]["correctA"][0],
                               file_data["QnA"][str(self.question_number)]["wrongAs"],
                               file_data["QnA"][str(self.question_number)]["mark"],
                               file_data["QnA"][str(self.question_number)]["feedback"])
            self.question_number_text.set("Question #" + str(self.question_number))
            self.is_save = False
            if self.question_number == 1:
                self.previous['state'] = 'disabled'

        tk.messagebox.showinfo("", "Question deleted")

class FormativeTest(Test2):

    def __init__(self, parent, controller):
        Test2.__init__(self, parent, controller)
        self.quiz = Test('name', self.test_number, 'module')

    def release(self):
        # Release button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = None
        self.quiz.enddate = None
        self.quiz.save_json("formative/Released")
        tk.messagebox.showinfo("", "Test Released")

    def save(self):
        # Save button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = None
        self.quiz.enddate = None
        self.quiz.save_json("formative/Unreleased")
        tk.messagebox.showinfo("", "Test Saved")

    def back(self):
        # Back button.
        self.attempts1 = None
        self.unlimitedattempts = None
        self.quiz.Questions = {}
        self.controller.show_frame("TestPage")
        self.question_number = 1
        self.question_number_text.set("Question #" + str(self.question_number))
        self.module2.delete(0, tk.END)
        self.testname2.delete(0, tk.END)
        self.question2.delete(0, tk.END)
        self.correct1.delete(0, tk.END)
        self.incorrect4.delete(0, tk.END)
        self.incorrect5.delete(0, tk.END)
        self.incorrect6.delete(0, tk.END)
        self.feedback1.delete(0, tk.END)

class SummativeTest(Test2):

    def __init__(self, parent, controller):
        Test2.__init__(self, parent, controller)
        self.startdate = tk.Label(self, text="Start Date", font=14, fg="black")
        self.startdate.place(x=0, y=540)
        self.startdate1 = tk.Entry(self)
        self.startdate1.place(x=125, y=545)
        self.enddate = tk.Label(self, text="End Date", font=14, fg="black")
        self.enddate.place(x=0, y=600)
        self.enddate1 = tk.Entry(self)
        self.enddate1.place(x=125, y=605)
        self.quiz = Test('', self.test_number, '')

    def release(self):
        # Release button for summative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = self.startdate1.get()
        self.quiz.enddate = self.enddate1.get()
        self.quiz.save_json("summative/Released")
        tk.messagebox.showinfo("", "Test Released")

    def save(self):
        # Save button for summative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = self.startdate1.get()
        self.quiz.enddate = self.enddate1.get()
        self.quiz.save_json("summative/Unreleased")
        tk.messagebox.showinfo("", "Test Saved")

    def back(self):
        # Back button.
        self.attempts1 = None
        self.unlimitedattempts = None
        self.quiz.Questions = {}
        self.controller.show_frame("TestPage")
        self.question_number = 1
        self.question_number_text.set("Question #" + str(self.question_number))
        self.module2.delete(0, tk.END)
        self.testname2.delete(0, tk.END)
        self.question2.delete(0, tk.END)
        self.correct1.delete(0, tk.END)
        self.incorrect4.delete(0, tk.END)
        self.incorrect5.delete(0, tk.END)
        self.incorrect6.delete(0, tk.END)
        self.feedback1.delete(0, tk.END)
        self.startdate1.delete(0, tk.END)
        self.enddate1.delete(0, tk.END)

class ManageTest(tk.Frame):
    # Page to manage test.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = tk.Button(self, text="Formative Test", font=16, fg="black",
                            command=lambda: controller.show_frame("OpenFormativeTest"))
        button1.place(x=550, y=200)

        button2 = tk.Button(self, text="Summative Test", font=16, fg="black",
                            command=lambda: controller.show_frame("OpenSummativeTest"))
        button2.place(x=550, y=400)

        button3 = tk.Button(self, text="Back", font=16, fg="black", command=lambda: controller.show_frame("StartPage"))
        button3.place(x=0, y=760)

        logout = tk.Button(self, text="Logout", font=16, fg="black", command=quit)
        logout.place(x=1125, y=760)

class OpenFormativeTest(Test2):

    def __init__(self, parent, controller):
        Test2.__init__(self, parent, controller)
        self.quiz = Test('name', self.test_number, 'module')

        self.test1 = tk.Label(self, text="Tests", font=14, fg="black")
        self.test1.place(x=530, y=0)
        self.test2 = ttk.Combobox(self, width='70')

        test_list = []
        path = "./formative/Unreleased"
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            test_list.append(file_path)

        self.test2['values'] = tuple(test_list)
        self.test2.place(x=588, y=5)

        select = tk.Button(self, text="Select", font=16, fg="black", command=lambda: self.OpenFile(self.test2.get()))
        select.place(x=780, y=60)

        self.previous['state'] = 'disabled'
        self.next['state'] = 'disabled'

    def OpenFile(self, path):
        try:
            f = open(path, encoding='utf-8')
            file_data = json.load(f)

            self.previous = tk.Button(self, text="previous", font=16, fg="black",
                                      command=lambda: self.managetest_show_previuos(file_data))
            self.previous.place(x=0, y=690)
            self.next = tk.Button(self, text="next", font=16, fg="black",
                                  command=lambda: self.managetest_show_next(file_data))
            self.next.place(x=150, y=690)
            self.previous['state'] = 'disabled'
            self.add = tk.Button(self, text="Add another question", font=16, fg="black",
                                 command=lambda: self.managetest_add_question(file_data))
            self.add.place(x=300, y=0)
            self.add_q = tk.Button(self, text="Save Question(must click after each question is created)", font=16,
                                   fg="black", command=lambda: self.managetest_save_question(file_data))
            self.add_q.place(x=250, y=690)
            self.save_file = tk.Button(self, text="Save test", font=16, fg="black",
                                       command=lambda: self.save_formativetest(file_data))
            self.save_file.place(x=200, y=755)
            self.release_file = tk.Button(self, text="Release test", font=16, fg="black",
                                          command=lambda: self.release_formativetest(file_data))
            self.release_file.place(x=0, y=755)
            self.delete = tk.Button(self, text="Delete Question", font=16, fg="black",
                                    command=lambda: self.managetest_delete(file_data))
            self.delete.place(x=300, y=55)

            self.m.set(file_data["module"])
            self.t.set(file_data["name"])
            if len(file_data["QnA"]) >= 1:
                self.q.set(file_data["QnA"]['1']["q"])
                self.b.set(file_data["QnA"]['1']["feedback"])
                self.c.set(file_data["QnA"]['1']["correctA"][0])
                self.w_1.set(file_data["QnA"]['1']["wrongAs"][0][0])
                self.w_2.set(file_data["QnA"]['1']["wrongAs"][1][0])
                self.w_3.set(file_data["QnA"]['1']["wrongAs"][2][0])
                # self.managetest_save_question()

            if len(file_data["QnA"]) > 1:
                self.next['state'] = 'normal'
                self.add['state'] = 'disabled'
            else:
                self.next['state'] = 'disabled'
                self.add['state'] = 'normal'

        except Exception as e:
            tk.messagebox.showinfo("", "Please select a test")

    def release(self):
        # Release button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = None
        self.quiz.enddate = None
        self.quiz.save_json("formative/Released")
        tk.messagebox.showinfo("", "Test Released")

    def save(self):
        # Save button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = None
        self.quiz.enddate = None
        self.quiz.save_json("formative/Unreleased")
        tk.messagebox.showinfo("", "Test Saved")

    def save_formativetest(self, file_data):
        # Save button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = None
        self.quiz.enddate = None
        for m in range(len(file_data["QnA"])):
            ansOptions = []
            ansOptions.append(file_data["QnA"][str(m + 1)]["correctA"][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][0][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][1][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][2][0])
            self.quiz.addQuestion(False, m + 1, file_data["QnA"][str(m + 1)]["q"],
                                  file_data["QnA"][str(m + 1)]["correctA"][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][0][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][1][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][2][0],
                                  mark=file_data["QnA"][str(m + 1)]["mark"],
                                  feedback=file_data["QnA"][str(m + 1)]["feedback"])

        self.quiz.save_json("formative/Unreleased")
        tk.messagebox.showinfo("", "Test Saved")

    def release_formativetest(self, file_data):
        # Save button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = None
        self.quiz.enddate = None
        for m in range(len(file_data["QnA"])):
            ansOptions = []
            ansOptions.append(file_data["QnA"][str(m + 1)]["correctA"][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][0][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][1][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][2][0])
            self.quiz.addQuestion(False, m + 1, file_data["QnA"][str(m + 1)]["q"],
                                  file_data["QnA"][str(m + 1)]["correctA"][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][0][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][1][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][2][0],
                                  mark=file_data["QnA"][str(m + 1)]["mark"],
                                  feedback=file_data["QnA"][str(m + 1)]["feedback"])

        self.quiz.save_json("formative/Released")
        tk.messagebox.showinfo("", "Test Released")

    def back(self):
        # Back button.
        self.attempts1 = None
        self.unlimitedattempts = None
        self.quiz.Questions = {}
        self.controller.show_frame("ManageTest")
        self.question_number = 1
        self.question_number_text.set("Question #" + str(self.question_number))
        self.module2.delete(0, tk.END)
        self.testname2.delete(0, tk.END)
        self.question2.delete(0, tk.END)
        self.correct1.delete(0, tk.END)
        self.incorrect4.delete(0, tk.END)
        self.incorrect5.delete(0, tk.END)
        self.incorrect6.delete(0, tk.END)
        self.feedback1.delete(0, tk.END)
        self.test2.delete(0, tk.END)

class OpenSummativeTest(Test2):

    def __init__(self, parent, controller):
        Test2.__init__(self, parent, controller)
        self.quiz = Test('name', self.test_number, 'module')
        self.test1 = tk.Label(self, text="Tests", font=16, fg="black")
        self.test1.place(x=530, y=0)
        self.test2 = ttk.Combobox(self, width='70')

        test_list = []
        path = "./summative/Unreleased"
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            test_list.append(file_path)

        self.test2['values'] = tuple(test_list)
        self.test2.place(x=588, y=5)

        self.startdate = tk.Label(self, text="Start Date", font=14, fg="black")
        self.startdate.place(x=0, y=540)
        self.startdate1 = tk.Entry(self, textvariable=self.sd)
        self.startdate1.place(x=125, y=545)
        self.enddate = tk.Label(self, text="End Date", font=14, fg="black")
        self.enddate.place(x=0, y=600)
        self.enddate1 = tk.Entry(self, textvariable=self.ed)
        self.enddate1.place(x=125, y=605)

        select = tk.Button(self, text="Select", font=14, fg="black", command=lambda: self.OpenFile(self.test2.get()))
        select.place(x=780, y=60)

        self.previous['state'] = 'disabled'
        self.next['state'] = 'disabled'

    def OpenFile(self, path):

        try:
            f = open(path, encoding='utf-8')
            file_data = json.load(f)

            self.previous = tk.Button(self, text="previous", font=16, fg="black",
                                      command=lambda: self.managetest_show_previuos(file_data))
            self.previous.place(x=0, y=690)
            self.next = tk.Button(self, text="next", font=16, fg="black",
                                  command=lambda: self.managetest_show_next(file_data))
            self.next.place(x=150, y=690)
            self.previous['state'] = 'disabled'
            self.add = tk.Button(self, text="Add another question", font=16, fg="black",
                                 command=lambda: self.managetest_add_question(file_data))
            self.add.place(x=300, y=0)
            self.add_q = tk.Button(self, text="Save Question(must click after each question is created)", font=16,
                                   fg="black", command=lambda: self.managetest_save_question(file_data))
            self.add_q.place(x=250, y=690)
            self.save_file = tk.Button(self, text="Save test", font=16, fg="black",
                                       command=lambda: self.save_summativetest(file_data))
            self.save_file.place(x=200, y=755)
            self.release_file = tk.Button(self, text="Release test", font=16, fg="black",
                                          command=lambda: self.release_summativetest(file_data))
            self.release_file.place(x=0, y=755)
            self.delete = tk.Button(self, text="Delete Question", font=16, fg="black",
                                    command=lambda: self.managetest_delete(file_data))
            self.delete.place(x=300, y=55)

            self.m.set(file_data["module"])
            self.t.set(file_data["name"])

            if len(file_data["QnA"]) >= 1:
                self.q.set(file_data["QnA"]['1']["q"])
                self.b.set(file_data["QnA"]['1']["feedback"])
                self.c.set(file_data["QnA"]['1']["correctA"][0])
                self.w_1.set(file_data["QnA"]['1']["wrongAs"][0][0])
                self.w_2.set(file_data["QnA"]['1']["wrongAs"][1][0])
                self.w_3.set(file_data["QnA"]['1']["wrongAs"][2][0])

            if len(file_data["QnA"]) > 1:
                self.next['state'] = 'normal'
                self.add['state'] = 'disabled'

            else:
                self.next['state'] = 'disabled'
                self.add['state'] = 'normal'

            self.sd.set(file_data["Start date"])
            self.ed.set(file_data["End date"])

        except Exception as e:
            tk.messagebox.showinfo("", "Please select a test")

    def release(self):
        # Release button for summative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = self.startdate1.get()
        self.quiz.enddate = self.enddate1.get()
        self.quiz.save_json("summative/Released")
        tk.messagebox.showinfo("", "Test Released")

    def save(self):
        # Save button for summative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = self.startdate1.get()
        self.quiz.enddate = self.enddate1.get()
        self.quiz.save_json("summative/Unreleased")
        tk.messagebox.showinfo("", "Test Saved")

    def save_summativetest(self, file_data):
        # Save button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = self.startdate1.get()
        self.quiz.enddate = self.enddate1.get()
        for m in range(len(file_data["QnA"])):
            ansOptions = []
            ansOptions.append(file_data["QnA"][str(m + 1)]["correctA"][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][0][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][1][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][2][0])
            self.quiz.addQuestion(False, m + 1, file_data["QnA"][str(m + 1)]["q"],
                                  file_data["QnA"][str(m + 1)]["correctA"][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][0][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][1][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][2][0],
                                  mark=file_data["QnA"][str(m + 1)]["mark"],
                                  feedback=file_data["QnA"][str(m + 1)]["feedback"])

        self.quiz.save_json("summative/Unreleased")
        tk.messagebox.showinfo("", "Test Saved")

    def release_summativetest(self, file_data):
        # Save button for formative test.
        self.quiz.name = self.testname2.get()
        self.quiz.module = self.module2.get()
        self.quiz.startdate = self.startdate1.get()
        self.quiz.enddate = self.enddate1.get()
        for m in range(len(file_data["QnA"])):
            ansOptions = []
            ansOptions.append(file_data["QnA"][str(m + 1)]["correctA"][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][0][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][1][0])
            ansOptions.append(file_data["QnA"][str(m + 1)]["wrongAs"][2][0])
            self.quiz.addQuestion(False, m + 1, file_data["QnA"][str(m + 1)]["q"],
                                  file_data["QnA"][str(m + 1)]["correctA"][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][0][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][1][0],
                                  file_data["QnA"][str(m + 1)]["wrongAs"][2][0],
                                  mark=file_data["QnA"][str(m + 1)]["mark"],
                                  feedback=file_data["QnA"][str(m + 1)]["feedback"])

        self.quiz.save_json("summative/Released")
        tk.messagebox.showinfo("", "Test Released")

    def back(self):
        # Back button.
        self.attempts1 = None
        self.unlimitedattempts = None
        self.quiz.Questions = {}
        self.controller.show_frame("ManageTest")
        self.question_number = 1
        self.question_number_text.set("Question #" + str(self.question_number))
        self.module2.delete(0, tk.END)
        self.testname2.delete(0, tk.END)
        self.question2.delete(0, tk.END)
        self.correct1.delete(0, tk.END)
        self.incorrect4.delete(0, tk.END)
        self.incorrect5.delete(0, tk.END)
        self.incorrect6.delete(0, tk.END)
        self.feedback1.delete(0, tk.END)
        self.startdate1.delete(0, tk.END)
        self.enddate1.delete(0, tk.END)
        self.test2.delete(0, tk.END)

class ModulesChooser(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        self.frame = tk.Frame(self)

        # make_plot()

        # background
        self.logo = tk.PhotoImage(file="interface/img/staff_main.png")
        self.bg_label = tk.Label(self.master,
                                 image=self.logo).place(x=0, y=0)

        # data
        self.TEST_NAME = tk.StringVar(self.master)
        self.TEST_NAME.set("Select a Test")
        self.test_name_0 = "Capital Cities"
        self.test_name_1 = "General Knowledge."

        self.DEADLINE = tk.StringVar(self.master)
        self.DEADLINE.set("")
        self.deadline_0 = "07/04/2019"
        self.deadline_1 = "08/04/2019"

        self.TYPE = tk.StringVar(self.master)
        self.TYPE.set("")
        self.type_0 = "Sumative"
        self.type_1 = "Formative"

        self.HANDOUT = tk.StringVar(self.master)
        self.HANDOUT.set("")
        self.handout_0 = "01/04/2019"
        self.handout_1 = "01/05/2019"

        self.ATTEMPTS = tk.StringVar(self.master)
        self.ATTEMPTS.set("")
        self.attempts_0 = "1"
        self.attempts_1 = "Unlimited"

        self.ASSESSED = tk.StringVar(self.master)
        self.ASSESSED.set("")
        self.assessed_0 = "Yes"
        self.assessed_1 = "Yes"

        self.STATS_PLOT = tk.PhotoImage(file="core/data/empty_figure.png")

        self.stats_plot_0 = tk.PhotoImage(file='core/data/pltfigure.png')

        # Title Frame
        self.title_frame = tk.Frame(
            self.master,
            borderwidth=1,
            relief=tk.FLAT,
            bg="floral white"
        )
        self.title_frame.grid_rowconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(0, weight=1)

        # Title text label
        self.title_label =tk.Label(
            self.title_frame,
            text="Staff Results Panel",
            font=("Helvetica", 50),
            bg="floral white"
        ).grid(row=0, column=0, sticky="w")

        # Title Place

        self.title_frame.place(x=50, y=20)

        # Select Module Frame
        self.modules_chooser_frame = tk.Frame(
            self.master,
            borderwidth=2,
            relief=tk.GROOVE,
            bg="azure"
        )
        self.modules_chooser_frame.grid_rowconfigure(0, weight=1)
        self.modules_chooser_frame.grid_rowconfigure(1, weight=2)
        self.modules_chooser_frame.grid_rowconfigure(2, weight=2)
        self.modules_chooser_frame.grid_columnconfigure(0, weight=1)

        self.modules_chooser_frame.place(x=100, y=150)

        # Module Label
        self.modules_chooser_label = tk.Label(
            self.modules_chooser_frame,
            text="Module:",
            font=("Helvetica", 14),
            bg="azure"
        ).grid(row=0, column=0, sticky="w")

        # Hamburguer Option Menu

        def callback(selection):
            print(selection)
            module_selected = load_test_ids(selection)
            print(module_selected)
            self.questions_list.delete(0, 'end')
            for i in module_selected:
                self.questions_list.insert('end', i)

        def select_test_id(selection):
            w = selection.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            print("Value: {}".format(type(value)))
            if value == 'Capital Cities':
                # self.TEST_NAME.
                self.TEST_NAME.set(self.test_name_0)
                self.DEADLINE.set(self.deadline_0)
                self.TYPE.set(self.type_0)
                self.HANDOUT.set(self.handout_0)
                self.ATTEMPTS.set(self.attempts_0)
                self.ASSESSED.set(self.assessed_0)
                self.STATS_PLOT.config(file='core/data/pltfigure.png')
            if value == 'General Knowledge':
                self.TEST_NAME.set(self.test_name_1)
                self.DEADLINE.set(self.deadline_1)
                self.TYPE.set(self.type_1)
                self.HANDOUT.set(self.handout_1)
                self.ATTEMPTS.set(self.attempts_1)
                self.ASSESSED.set(self.assessed_1)
                self.STATS_PLOT.config(file='core/data/pltfigure_python.png')


        tk_module = tk.StringVar(self.master)
        tk_module.set("Select")
        modules_list = load_modules()
        self.modules_chooser_menu = tk.OptionMenu(
            self.modules_chooser_frame,
            tk_module,
            *modules_list,
            command=callback
        )


        self.modules_chooser_menu.config(
            width=10,
            font=("Helvetica", 14),

        )

        self.modules_chooser_menu.grid(row=1, column=0, sticky="w")

        # Questions

        self.questions_list = tk.Listbox(
            self.modules_chooser_frame,
            # width=14,
            height=10,
            font=("Helvetica", 14),
        )
        self.questions_list.bind('<<ListboxSelect>>', select_test_id)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.questions_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.questions_list.yview)

        # Grid
        self.questions_list.grid(row=2, column=0)
        # Populate
        # for i in range(5):
        #     self.questions_list.insert(tk.END,i)
            # broken
        # self.scrollbar.grid(column=0, sticky="nswe")

        self.quizes_frame = tk.Frame(
            self.master,
            width=800,
            height=600,
            borderwidth=2,
            relief=tk.SUNKEN,
        )
        # grid config
        self.quizes_frame.grid_rowconfigure(0, weight=0)
        self.quizes_frame.grid_rowconfigure(1, weight=1)
        self.quizes_frame.grid_columnconfigure(0, weight=1)
        self.quizes_frame.grid_columnconfigure(1, weight=1)
        self.quizes_frame.grid_propagate(False)
        # place the frame
        self.quizes_frame.place(x=350, y=150)

        # info about the test frame.
        self.quizes_info_frame = tk.LabelFrame(
            self.quizes_frame,
            text="Information about the Test",
            # width=400,
            # height = 100,
            borderwidth=1,
            relief=tk.FLAT,
        )
        self.quizes_info_frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        # self.quizes_info_frame.grid_rowconfigure(0, weight=1)
        # self.quizes_info_frame.grid_rowconfigure(1, weight=1)
        self.quizes_info_frame.grid_columnconfigure(0, weight=1)
        self.quizes_info_frame.grid_columnconfigure(1, weight=1)
        self.quizes_info_frame.grid_columnconfigure(2, weight=1)
        self.quizes_info_frame.grid_columnconfigure(3, weight=1)
        self.quizes_info_frame.grid_columnconfigure(4, weight=1)
        self.quizes_info_frame.grid_columnconfigure(5, weight=1)
        # self.quizes_info_frame.grid_propagate(False)

        # Labels for quizes_info_frame
        self.quiz_name_label = tk.Label(
            self.quizes_info_frame,
            borderwidth=2,
            relief="raised",
            text="Test Name:",
            font=("Helvetica", 12),
            bg="Azure",
        )
        self.quiz_name_label.grid(row=0, column=0, sticky="nwe")
        self.quiz_name_get_label = tk.Label(
            self.quizes_info_frame,
            textvariable=self.TEST_NAME,
            font=("Helvetica", 12),
        )
        self.quiz_name_get_label.grid(row=0, column=1, sticky="nwe")

        # Labels for deadline,

        self.quiz_deadline_label = tk.Label(
            self.quizes_info_frame,
            borderwidth=2,
            relief="raised",
            text="Deadline: ",
            font=("Helvetica", 12),
            bg="azure"
        )
        self.quiz_deadline_label.grid(row=0, column=2, sticky='nwe')

        self.quiz_deadline_get_label = tk.Label(
            self.quizes_info_frame,
            textvariable=self.DEADLINE,
            font=("Helvetica", 12)
        )
        self.quiz_deadline_get_label.grid(row=0, column=3, sticky='nwe')

        # Label for Quiz Type

        self.quiz_type_label = tk.Label(
            self.quizes_info_frame,
            borderwidth=2,
            relief="raised",
            text="Type: ",
            font=("Helvetica", 12),
            bg="azure"
        )
        self.quiz_type_label.grid(row=0, column=4, sticky="nwe")

        self.quiz_type_label_get = tk.Label(
            self.quizes_info_frame,
            textvariable=self.TYPE,
            font=("Helvetica", 12),
        )
        self.quiz_type_label_get.grid(row=0, column=5, sticky="nwe")

        self.quiz_handout_label = tk.Label(
            self.quizes_info_frame,
            borderwidth=2,
            relief="raised",
            text="Handout: ",
            font=("Helvetica", 12),
            bg="azure"
        )
        self.quiz_handout_label.grid(row=1, column=0, sticky="nwe")

        self.quiz_handout_get_label = tk.Label(
            self.quizes_info_frame,
            textvariable=self.HANDOUT,
            font=("Helvetica", 12)
        ).grid(row=1, column=1, sticky="nwe")

        # Max attemps

        self.quiz_max_attemps_label = tk.Label(
            self.quizes_info_frame,
            borderwidth=2,
            relief="raised",
            text="Attemps: ",
            font=("Helvetica", 12),
            bg="azure"
        ).grid(row=1, column=2, sticky="nwe")

        self.quiz_max_attemps_get_label = tk.Label(
            self.quizes_info_frame,
            textvariable=self.ATTEMPTS,
            font=("helvetica",12)
        ).grid(row=1, column=3, sticky="nwe")

        self.quiz_assess_label = tk.Label(
            self.quizes_info_frame,
            borderwidth=2,
            relief="raised",
            text="Assessed: ",
            font=("Helvetica", 12),
            bg="azure"
        ).grid(row=1, column=4, sticky="nwe")

        self.quiz_assess_get_label = tk.Label(
            self.quizes_info_frame,
            textvariable=self.ASSESSED,
            font=("Helvetica", 12),
        ).grid(row=1, column=5, sticky="nwe")

        # Uni logo,
        self.uni_logo = tk.PhotoImage(file="interface/img/uni_logo.png")
        self.uni_logo_label = tk.Label(
            self.quizes_frame,
            image=self.uni_logo
        ).grid(row=0, column=1, pady=5)

        # Results main frame
        self.quizes_results_frame = tk.Frame(
            self.quizes_frame,
            # text="Results",
            # font=("Helvetica", 10),
            borderwidth = 2,
            relief = "ridge",
            bg = "lemon chiffon"
        )

        self.quizes_results_frame.grid(row=1, sticky="nesw", padx=10, pady=10, columnspan=2)
        # self.quizes_results_frame.grid_rowconfigure(0, weight=1)
        # self.quizes_results_frame.grid_rowconfigure(1, weight=0)
        # self.quizes_results_frame.grid_rowconfigure(2, weight=0)
        # self.quizes_results_frame.grid_columnconfigure(0, weight=1)
        # self.quizes_results_frame.grid_columnconfigure(1, weight=0)
        # self.quizes_results_frame.grid_columnconfigure(2, weight=0)
        # self.quizes_results_frame.grid_columnconfigure(3, weight=0)


        # Results info Frame
        self.results_info_frame = tk.LabelFrame(
            self.quizes_results_frame,
            text="Graphics",
            borderwidth=2,
            relief="flat",
            bg="lemon chiffon"
        )
        self.results_info_frame.grid(row=0, column=0)


        self.test_label = tk.Label(
            self.results_info_frame,
            image=self.STATS_PLOT,
            borderwidth=2,
            relief='sunken'
        ).grid(row=0, column=0, sticky="nwe", padx=31)

if __name__ == "__main__":
    app = TestCreaterApp()
    app.mainloop()