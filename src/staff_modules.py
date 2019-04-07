#!/usr/bin/env python3

# from core.student import Student
# from core.quiz import Quiz
from core.engine import load_modules, load_test_ids, make_plot
import matplotlib as plt
import tkinter as tk

QUIZES_DATA = "data/quizes.json"

"""==================================================================
STAFF MODULES CHOOSER
======================================================================
Choose a module and create/ammend questions"""

class ModulesChooser(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.frame = tk.Frame(self.master)

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
            bg="floral white"

        )

        self.modules_chooser_menu.grid(row=1, column=0, sticky="w")

        # Questions

        self.questions_list = tk.Listbox(
            self.modules_chooser_frame,
            # width=14,
            height=10,
            font=("Helvetica", 14),
            bg="floral white",
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
            bg="floral white",
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
            bg="floral white",
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

def main():
    root = tk.Tk()
    root.title("Modules")
    root.geometry('{}x{}'.format(1200, 800))
    root.resizable(width=True, height=True)
    app = ModulesChooser(root, root)
    app.mainloop()

# os.chdir("/home/c1868921/Documents/code/python/Alegria") #REPL line

main()
