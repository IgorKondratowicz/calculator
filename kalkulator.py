import tkinter as tk
from tkinter.constants import COMMAND

FONT = ("Verdana", 10)

class application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("320x416")
        self.resizable(0,0)
        self.title("kalkulator")
        container = tk.Frame(self)
        container.pack(expand=True, fill="both")

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        frame = StartPage(container, self)
        frame.grid(row = 0, column = 0, sticky = "nsew")
        frame.tkraise()

    

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.create_widgets()
        self.equation  = ""
        
    def create_widgets(self):
        top_label = tk.Label(self, height = 5 , font = FONT, fg = "white", bg = "#1f1f1f", text = "KALKULATOR", padx = 10, anchor="e")
        top_label.pack(side="top", fill="x")

        
        buttons = []
        values = ["%", "CE", "C", "<-", "1/x", "x^2", "sqrt()", "/", "7","8","9","*", "4","5","6","-", "1","2","3","+", "+/-", "0",".", "="]
        
        #creating buttons 
        for i in range(0,24):
            buttons.append(tk.Button(text = values[i], font = FONT, bg = "black", fg = "white", width=9, height=3, anchor="center"))
        
        #idk why for loop doesn't work, so I had to do it like this
        buttons[0]["command"] = lambda: change_text(values[0])
        #buttons[1]["command"] = lambda: change_text(values[1])
        #buttons[2]["command"] = lambda: change_text(values[2])
        #buttons[3]["command"] = lambda: change_text(values[3])
        #buttons[4]["command"] = lambda: change_text(values[4])
        buttons[5]["command"] = lambda: change_text(values[5])
        buttons[6]["command"] = lambda: change_text(values[6])
        buttons[7]["command"] = lambda: change_text(values[7])
        buttons[8]["command"] = lambda: change_text(values[8])
        buttons[9]["command"] = lambda: change_text(values[9])
        buttons[10]["command"] = lambda: change_text(values[10])
        buttons[11]["command"] = lambda: change_text(values[11])
        buttons[12]["command"] = lambda: change_text(values[12])
        buttons[13]["command"] = lambda: change_text(values[13])
        buttons[14]["command"] = lambda: change_text(values[14])
        buttons[15]["command"] = lambda: change_text(values[15])
        buttons[16]["command"] = lambda: change_text(values[16])
        buttons[17]["command"] = lambda: change_text(values[17])
        buttons[18]["command"] = lambda: change_text(values[18])
        buttons[19]["command"] = lambda: change_text(values[19])
        buttons[20]["command"] = lambda: change_text(values[20])
        buttons[21]["command"] = lambda: change_text(values[21])
        buttons[22]["command"] = lambda: change_text(values[22])
        #buttons[23]["command"] = lambda: change_text(values[23])


        def change_text(given_text):
            self.equation += given_text
            top_label.config(text = self.equation)
            #setting button effects
            def button_2():
                self.equation = ""
                top_label.config(text=self.equation)

            buttons[2]["command"] = lambda:button_2()


            def button_3():
                self.equation = self.equation[:-1]
                top_label.config(text = self.equation)

            buttons[3]["command"] = lambda:button_3()

            def button_4():
                eq = self.equation
                self.equation = ""
                self.equation += "1/"+ eq
                top_label.config(text=self.equation)

            buttons[4]["command"] = lambda:button_4()

            def button_23():
                try:
                    self.equation = str(round(eval(self.equation),5))
                except:
                    self.equation = "błąd"
                top_label.config(text = self.equation)
            buttons[23]["command"] = lambda:button_23()

        #setting hover effects
        def on_enter(e):
            e.widget['background'] = 'black'

        def on_leave(e):
            e.widget['background'] = 'black'
        
        def on_click(e):
            e.widget['background'] = 'black'
        for button in buttons:
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            button.bind("<Button>", on_click)
        
        #positioning buttons in a frame
        x_place = 0
        y_place = 30
        XADD = 80
        YADD = 55
        for i in range(0,24):
            
            if i%4 != 0:
                buttons[i].place(x = x_place, y = y_place)
                x_place+=XADD 
            else:
                x_place = 0
                y_place += YADD
                buttons[i].place(x = x_place, y = y_place)
                x_place+=XADD 

app = application()
app.mainloop()