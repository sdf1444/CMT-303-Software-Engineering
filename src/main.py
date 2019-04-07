# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 4:30
# @Author  : Chaoran Wang
# @FileName: main.py
# @Software: PyCharm
from tkinter import *
from tkinter import messagebox
import os
import json
from create_manageTest import TestCreaterApp
from takeTestInterface import TestTakeApp


headingfont = ('Helvetica ', 50)
labelfont = ('Helvetica ', 16)
class StudentLogin:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='white')
        self.root.title("Student Login Page")
        self.root.geometry("1200x800")
        self.heading = Label(self.root, text="Login",font=headingfont)
        self.Username = Label(self.root, text="Username",font=labelfont)
        self.Password = Label(self.root, text="Password",font=labelfont)
        self.uname = Entry(self.root)
        self.pw = Entry(self.root,show="*")
        self.status = Entry(self.root)
        self.submit = Button(self.root, text="Submit", command=self.login)
        self.reset = Button(self.root, text="Reset", command=self.clear)
    def clear(self):
        self.uname.delete(0, END)
        self.pw.delete(0, END)

    def login(self):
        if (self.uname.get() == "" or self.pw.get() == ""):
            messagebox.showwarning("Error!","Username or Passwod or Status cannot be empty!",parent=self.root)
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
                                    messagebox.showinfo("Success!","Hello " + str(u) + "! Welcome to Interface!",parent=self.root)
                                    app = TestTakeApp()
                                    app.mainloop()

                                    break
                        except:
                            messagebox.showwarning("Failed!","Sorry. User not found!",parent=self.root)
                            break
                self.clear()
            except:
                messagebox.showwarning("Database Empty!","No users were found. Please Register.",parent=self.root)

                self.root.destroy()

    def render(self):
        self.heading.grid(row=0, column=1,pady="20")
        self.Username.grid(row=1, column=0)
        self.Password.grid(row=2, column=0)
        self.uname.grid(row=1, column=1, ipadx="100",ipady="10",padx="10")
        self.pw.grid(row=2, column=1,ipadx="100",ipady="10",padx="10")
        self.submit.grid(row=4,column=1,columnspan=2,sticky=W,padx="20",pady="20")
        self.reset.grid(row=4,column = 1 ,columnspan=2,sticky=E,padx="20",pady="20")
        self.root.mainloop()

class StaffLogin:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='white')
        self.root.title("Staff Login Page")
        self.root.geometry("1200x800")
        self.heading = Label(self.root, text="Login",font=headingfont)
        self.Username = Label(self.root, text="Username",font=labelfont)
        self.Password = Label(self.root, text="Password",font=labelfont)
        self.uname = Entry(self.root)
        self.pw = Entry(self.root,show="*")
        self.status = Entry(self.root)
        self.submit = Button(self.root, text="Submit", command=self.login)
        self.reset = Button(self.root, text="Reset", command=self.clear)
    def clear(self):
        self.uname.delete(0, END)
        self.pw.delete(0, END)

    def login(self):
        if (self.uname.get() == "" or self.pw.get() == ""):
            messagebox.showwarning("Error!","Username or Passwod or Status cannot be empty!",parent=self.root)
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
                                    messagebox.showinfo("Success!","Hello " + str(u) + "! Welcome to Interface!",parent=self.root)
                                    app = TestCreaterApp()
                                    app.mainloop()

                        except:
                            messagebox.showwarning("Failed!","Sorry. User not found!",parent=self.root)
                            break
                self.clear()
            except:
                messagebox.showwarning("Database Empty!","No users were found. Please Register.",parent=self.root)

                self.root.destroy()

    def render(self):
        self.heading.grid(row=0, column=1,pady="20")
        self.Username.grid(row=1, column=0)
        self.Password.grid(row=2, column=0)
        self.uname.grid(row=1, column=1, ipadx="100",ipady="10",padx="10")
        self.pw.grid(row=2, column=1,ipadx="100",ipady="10",padx="10")
        self.submit.grid(row=4,column=1,columnspan=2,sticky=W,padx="20",pady="20")
        self.reset.grid(row=4,column = 1 ,columnspan=2,sticky=E,padx="20",pady="20")
        self.root.mainloop()
def do_studentlogin():
    x=StudentLogin()
    x.render()

def do_stafflogin():
    x=StaffLogin()
    x.render()

class Register:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='white')
        self.root.title("Registration Form")
        self.root.geometry("1200x800")
        self.heading = Label(self.root, text="Register", font=headingfont)
        self.Username = Label(self.root, text="Username",font=labelfont)
        self.Password = Label(self.root, text="Password",font=labelfont)
        self.Status = Label(self.root, text = "Status",font=labelfont)
        self.uname = Entry(self.root)
        self.pw = Entry(self.root,show="*")
        self.status = Entry(self.root)
        from time import time
        self.id = str(int(time()*100))
        self.submit = Button(self.root, text="Submit", command=self.insert)
        self.reset = Button(self.root, text="Reset", command=self.clear)

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
            messagebox.showwarning("Empty Input!","Please fill all the details.",parent=self.root)
        if(
                self.status.get() not in ["Student","Staff"]
        ):
            messagebox.showwarning("Empty Input!", "Please ensure Status with Student or Staff.", parent=self.root)

        else:
                if (self.status.get()== "Student"):
                   path = "./User/Student"
                   saveUser = self.user_wrapper()
                   filename = "%s/%s.json" % (path, self.id)
                   with open(filename, "w") as outfile:
                      json.dump(saveUser, outfile, indent=4)
                      messagebox.showinfo("Account created.","Please login using new credentials. :)",parent=self.root)
                   self.root.destroy()

                if (self.status.get()== "Staff"):
                   path = "./User/Staff"
                   saveUser = self.user_wrapper()
                   filename = "%s/%s.json" % (path, self.id)
                   with open(filename, "w") as outfile:
                      json.dump(saveUser, outfile, indent=4)
                      messagebox.showinfo("Account created.","Please login using new credentials. :)",parent=self.root)
                   self.root.destroy()


    def render(self):

        self.heading.grid(row=0, column=1,pady="20")
        self.Username.grid(row=4, column=0)
        self.Password.grid(row=5, column=0)
        self.Status.grid(row=6, column=0)
        self.uname.grid(row=4, column=1, ipadx="100", ipady="10", padx="10")
        self.pw.grid(row=5, column=1, ipadx="100",ipady="10",padx="10")
        self.status.grid(row=6, column=1, ipadx="100",ipady="10",padx="10")
        self.submit.grid(row=9,column=1,columnspan=2,sticky=W,padx="20",pady="20")
        self.reset.grid(row=9,column = 1 ,columnspan=2,sticky=E,pady="20",padx="20")
        self.root.mainloop()

def do_register():
    x=Register()
    x.render()
if __name__ == '__main__':
    root = Tk()
    root.configure(background='white')
    root.title("Home Page")
    root.geometry("1200x800")
    heading = Label(root, text="Home")
    heading.config(height=3, width=20,font=headingfont)
    heading.grid(row=0, column=1)
    login = Button(root, text="Login for Student", command=do_studentlogin)
    login.grid(row=1,column=1,sticky=N,padx=200,pady=40)
    login2 = Button(root, text="Login for Staff", command=do_stafflogin)
    login2.grid(row=2, column=1, sticky=N, padx=200, pady=40)
    register = Button(root, text="Register",  command=do_register)
    register.grid(row=3,column=1,sticky=N,padx=200,pady=40)
    root.mainloop()

