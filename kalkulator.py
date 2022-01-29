import tkinter as tk
import math
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
        self.values = ["%", "CE", "C", "<-", "1/x", "x^2", "sqrt()", "/", "7","8","9","*", "4","5","6","-", "1","2","3","+", "+/-", "0",".", "="]
        self.label = self.create_label()
        self.buttons = self.create_buttons(self.values)
        self.addCommand(self.label, self.buttons)
        self.set_position(self.buttons)
        self.hover_effects(self.buttons)
        self.equation  = ""
        
    def create_label(self):
        top_label = tk.Label(self, height = 5 , font = FONT, fg = "white", bg = "#1f1f1f", text = "KALKULATOR", padx = 10, anchor="e")
        top_label.pack(side="top", fill="x")

        return top_label

    def create_buttons(self, values):
        buttons = []
        for i in range(0,24):
            buttons.append(tk.Button(text = values[i], font = FONT, bg = "black", fg = "white", width=9, height=3, anchor="center"))
        
        return buttons

    def addCommand(self, top_label, buttons):
        
        buttons[0]["command"] = lambda: change_text(self.values[0])
        
        buttons[2]["command"] = lambda:button_2()
        buttons[3]["command"] = lambda:button_3()
        buttons[4]["command"] = lambda:button_4()
        buttons[5]["command"] = lambda:button_5()
        buttons[6]["command"] = lambda:button_6()
        buttons[7]["command"] = lambda: change_text(self.values[7])
        buttons[8]["command"] = lambda: change_text(self.values[8])
        buttons[9]["command"] = lambda: change_text(self.values[9])
        buttons[10]["command"] = lambda: change_text(self.values[10])
        buttons[11]["command"] = lambda: change_text(self.values[11])
        buttons[12]["command"] = lambda: change_text(self.values[12])
        buttons[13]["command"] = lambda: change_text(self.values[13])
        buttons[14]["command"] = lambda: change_text(self.values[14])
        buttons[15]["command"] = lambda: change_text(self.values[15])
        buttons[16]["command"] = lambda: change_text(self.values[16])
        buttons[17]["command"] = lambda: change_text(self.values[17])
        buttons[18]["command"] = lambda: change_text(self.values[18])
        buttons[19]["command"] = lambda: change_text(self.values[19])
        buttons[20]["command"] = lambda: change_text(self.values[20])
        buttons[21]["command"] = lambda: change_text(self.values[21])
        buttons[22]["command"] = lambda: change_text(self.values[22])
        buttons[23]["command"] = lambda:button_23()


        def change_text(given_text):
            self.equation += given_text
            top_label.config(text = self.equation)
            #setting button effects
        def button_2():
            self.equation = ""
            top_label.config(text=self.equation)



        def button_3():
            self.equation = self.equation[:-1]
            top_label.config(text = self.equation)


        def button_4():
            eq = self.equation
            self.equation = ""
            self.equation += "1/"+ eq
            top_label.config(text=self.equation)

        def button_5():
            top_label.config(text = f"{self.equation}^2")
            self.equation = f"{self.equation}**2"


        def button_6():
            eq = self.equation
            self.equation = ""
            self.equation += f"math.sqrt({eq})"
            top_label.config(text = self.equation.split('.')[1])


        def button_23():
            try:
                self.equation = str(round(eval(self.equation),5))
            except:
                self.equation = "błąd"
            top_label.config(text = self.equation)

        

    def hover_effects(self, buttons):
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
        
    def set_position(self, buttons):
        x_place = 0
        y_place = 30
        X_VALUE = 80
        Y_VALUE = 55
        for i in range(0,24):
            
            if i%4 != 0:
                buttons[i].place(x = x_place, y = y_place)
                x_place+=X_VALUE 
            else:
                x_place = 0
                y_place += Y_VALUE
                buttons[i].place(x = x_place, y = y_place)
                x_place+=X_VALUE 

app = application()
app.mainloop()