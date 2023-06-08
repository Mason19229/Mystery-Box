from tkinter import *
from tkinter import messagebox
from functools import partial #to present unwanted windows

import random

class Mystery_Box:
    def __init__(self):

        #formatting variables
        background_color = "#008A00"

        #Initialise list to hold spin history
        self.all_spin_list = []

        #Gamble frame
        self.gamble_frame = Frame(width=300, bg=background_color,
                                  pady=10)
        self.gamble_frame.grid()

        #Title heading (row 0)
        self.mystery_box_label = Label(self.gamble_frame, text="Mystery Box Gambling",
                                       font=("Arial 18 bold"),
                                       bg=background_color, fg="white",
                                       padx=10, pady=10)
        self.mystery_box_label.grid(row=0)

        #Balance Display (row 1)
        def balanceMsg(amount):
            amount = self.balance.get()
            self.balance = Label(self.gamble_frame, text=f"Balance: ${int(amount):.2f}",
                                       font=("Arial 10 bold"), wrap=250, justify=CENTER, bg = "#FFDF00", 
                                       padx=10, pady=10, width=30)
            self.balance.grid(row=1)
            return messagebox.showinfo("mystery box program", f"you have entered a starting balance of ${int(amount):.2f}. Thank you for donating!")

        self.balance = Entry(self.gamble_frame, text="Please enter a starting balance.",
                             font="Arial 14 italic")
        self.balance.bind("<Return>", balanceMsg)
        self.balance.grid(row=1)  
             

        #Description label (row 2)
        self.description_label = Label(self.gamble_frame, text="This gambling game contributes all earnings to charity. The possible prizes are Pb($0), Cu($2), Ag($4), and Au($10).",
                                       font ="arial 10", justify=LEFT, bg="white", wrap=200,
                                       padx=10, pady=10, width=30)
        self.description_label.grid(row=2, pady=10)

        #Play button (row 3)
        self.play_button = Button(self.gamble_frame, text = "Press to Play ($2)", 
                                  font = "Arial 10 bold", bg="#A20025", fg="white",
                                  padx=10, pady=10, width=20)
        self.play_button.grid(row=3)

        #Split frame (row 4)
        self.split_page_frame = Frame(self.gamble_frame, bg=background_color)
        self.split_page_frame.grid(row=4, pady=10)

        #History button (row 0, column 0 of split page)
        self.history_button = Button(self.split_page_frame, text = "History", 
                                     font = "Arial 10 bold", bg="#66B2FF", fg="white",
                                     padx=10, pady=10, width=8)
        self.history_button.grid(row=0, column=0, padx=5)

        #Help button (row 0, column 1 of split page)
        self.help_button = Button(self.split_page_frame, text = "Help", 
                                     font = "Arial 10 bold", bg="black", fg="white",
                                     padx=10, pady=10, width=8)
        self.help_button.grid(row=0, column=1, padx=5)

        #Summary button (row 5)
        self.summary_button = Button(self.gamble_frame, text = "Summary / Exit", 
                                  font = "Arial 10 bold", bg="#E51400", fg="white",
                                  padx=10, pady=10, width=20)
        self.summary_button.grid(row=5)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Gambling")
    something = Mystery_Box()
    root.mainloop()