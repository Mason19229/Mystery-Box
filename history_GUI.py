from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Mystery_Box:
    def __init__(self):
        
        #formatting variables...
        background_color = "light blue"       

        #in actual program this is blank and populated by user calculations
        self.spin_list = ["you got $2, your total is now $20", "you got $4, your total is now $22", "you got $10, your total is now $30", "you got $0, your total is now $28", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20"]
        #self.spin_list = []

        #converter main screen gui
        self.gamble_frame = Frame(width=600, height=600, bg=background_color)
        self.gamble_frame.grid()

        #Temperature conversion heading (row 0)
        self.mystery_box_label = Label(self.gamble_frame, text="Mystery Box", 
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.mystery_box_label.grid(row=0)

        #history Button (row 1)
        self.history_button = Button(self.gamble_frame, text="history", font="Arial 14", 
                                  padx=10, pady=10, command=lambda: self.history(self.spin_list),)
        self.history_button.grid(row=1)

        if len(self.spin_list) == 0:
            self.history_button.config(state=DISABLED)

    
    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):

        background = "#008A00"      #dark green

        #Disable history button
        partner.history_button.config(state=DISABLED)

        #Sets up child window (ie: history box)
        self.history_box = Toplevel()

        #IF users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        #Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        #Set up history heading (row 0)
        self.history_label = Label(self.history_frame, text="Spin History", bg="black", fg="white",
                                font=("Arial", "14", "bold"))
        self.history_label.grid(row=0)

        #history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent spins. Please use the export button to create a text file of all your spins for this session", 
                                     wrap=250, font=" arial 10 italic", 
                                     justify=LEFT, bg=background, fg="white", padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)

        #generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 10:
            for item in range (0, 10):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your spin history. You can use the export button to save this data to a text file if desired.")

        #label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string, fg="white",
                                bg=background, font="Arial 12 bold", justify=LEFT)
        self.calc_label.grid(row=2)

        # export button
        self.export_button = Button(self.history_frame, text="Export", 
                                    font="Arial 12 bold", width=20,
                                    fg="white", bg="black")
        self.export_button.grid(row=3, pady=5)

        # dismiss button
        self.dismiss_button = Button(self.history_frame, text="Dismiss", 
                                     font="Arial 12 bold", width=20, 
                                     fg="white", bg="#E51400",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=4, pady=5)

    def close_history(self, partner):
        #put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Gambling")
    something = Mystery_Box()
    root.mainloop()