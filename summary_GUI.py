from tkinter import *
from functools import partial #to prevent unwanted windows

import random

spins=10
earned=7

class Mystery_Box:
    def __init__(self):
        
        #formatting variables...
        background_color = "light blue"

        #converter main screen gui
        self.converter_frame = Frame(width=300, height=600, bg=background_color)
        self.converter_frame.grid()

        #Temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Mystery Box", 
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Summmary Button (row 1)
        self.sum_button = Button(self.converter_frame, text="Summary / Exit", 
                                  padx=10, pady=10, command=self.summary)
        self.sum_button.grid(row=1)

    
    def summary(self):
        get_summmary = Summary(self)

class Summary:
    def __init__(self, partner):

        background = "#008A00"

        #Disable summmary button
        partner.sum_button.config(state=DISABLED)

        #Sets up child window (ie: summary box)
        self.sum_box = Toplevel()

        #IF users press cross at top, closes summmary and 'releases' summary button
        self.sum_box.protocol('WM_DELETE_WINDOW', partial(self.close_sum, partner))

        #Set up GUI Frame
        self.sum_frame = Frame(self.sum_box, bg=background, width=300,)
        self.sum_frame.grid()

        #Set up Summary heading (row 0)
        self.sum_label = Label(self.sum_frame, text="Summary", bg="black", fg="white",
                                font=("Arial", "14", "bold"))
        self.sum_label.grid(row=0)

        #Summary text (label, row 1)
        global spins
        global spent
        global earned

        self.sum_text_label = Label(self.sum_frame, text=f"Spins = {spins} \nAmount spent = ${(spins*2):.2f} \nAmount Earned = ${(earned):.2f}", 
                                     justify=LEFT, 
                                     bg=background, fg="white", wraplength=200, padx=10, pady=10)
        self.sum_text_label.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_button = Button(self.sum_frame, text="Return", bg="black", fg="white",
                                     width=10, font=("Arial", "10", "bold"), 
                                     command=partial(self.close_sum, partner))
        self.dismiss_button.grid(row=2, pady=10)
        
        #Exit button (row 3)
        self.exit_button = Button(self.sum_frame, text="Exit", bg="#E51400", fg="white",
                                  width=10, font=("Arial", "10", "bold"),
                                  command=self.exit)
        self.exit_button.grid(row=3, pady=10)

    def close_sum(self, partner):
        #put sum button back to normal
        partner.sum_button.config(state=NORMAL)
        self.sum_box.destroy()

    def exit(self):
        #Exit the program
        root.quit()
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Gambling")
    something = Mystery_Box()
    root.mainloop()