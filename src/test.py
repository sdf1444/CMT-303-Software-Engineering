import tkinter as tk
from tkinter import ttk

#using ttk for buttons so they look better on windows

LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self)
		tk.Tk.wm_title(self, "Education System")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand="true")
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}


		# loop for all the pages
		for F in (StartPage, FormativeResultsPage, SummativeResultsPage):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)


	def show_frame(self, controller):

		frame = self.frames[controller]
		# raises it to the top (frame)
		frame.tkraise()




class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack()

		buttonFormative = ttk.Button(self, text="View Formative Results", command=lambda: controller.show_frame(FormativeResultsPage))
		buttonFormative.pack()

		buttonSummative = ttk.Button(self, text="View Summative Results", command=lambda: controller.show_frame(SummativeResultsPage))

		buttonSummative.pack()



class FormativeResultsPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Formative Test Results", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		buttonF2H = ttk.Button(self, text="Back to Start Page", command=lambda: controller.show_frame(StartPage))

		buttonF2H.pack()

		buttonF2S = ttk.Button(self, text="View Sumamtive Results", command=lambda: controller.show_frame(SummativeResultsPage))

		buttonF2S.pack()



class SummativeResultsPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Summative Test Results", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		buttonS2H = ttk.Button(self, text="Back to Start Page", command=lambda: controller.show_frame(StartPage))

		buttonS2H.pack()

		buttonS2F = ttk.Button(self, text="View Formative Results", command=lambda: controller.show_frame(FormativeResultsPage))

		buttonS2F.pack()

		# with open('answers.txt')



app = Application()
app.geometry("500x300")
app.mainloop()


# creating a blank window
# root = Tk()
# h = Hannah(root)
# root.mainloop()

# master = root/main window