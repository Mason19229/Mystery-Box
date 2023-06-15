from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Mystery_Box:
    def __init__(self):
        
        #formatting variables...
        background_color = "light blue"

        #converter main screen gui
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        #Temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Mystery Box Gambling", 
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Help Button (row 1)
        self.export_button = Button(self.converter_frame, text="Help", 
                                  padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    
    def export(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):

        background = "#008A00" #dark green

        #Disable export button
        partner.export_button.config(state=DISABLED)

        #Sets up child window (ie: export box)
        self.export_box = Toplevel()

        #IF users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        #Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        #Set up Export heading (row 0)
        self.export_label = Label(self.export_frame, text="Export",
                                font=("Arial", "14", "bold"),
                                bg="black", fg="white")
        self.export_label.grid(row=0)

        #Export Instructions (label, row 1)
        self.export_text_label = Label(self.export_frame, text="Enter a filename in the box below and press the save button to save your spin history to a text file", 
                                     justify=LEFT, width=40, 
                                     bg=background, fg="white", wrap=250)
        self.export_text_label.grid(row=1)

        # warning text
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists its contents will be replaced with your spin history",
                                       justify=LEFT, bg=background, fg="white",
                                       font="Arial 10 italic", wrap=225, padx=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.export_frame, text="Save", 
                                  fg="white", bg="black", width=30)
        self.save_button.grid(row=4, pady=5)

        self.cancel_button = Button(self.export_frame, text="Cancel", 
                                    fg="white", bg="#E51400", width=30,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=5, pady=5)

    def close_export(self, partner):
        #put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Gambling")
    something = Mystery_Box()
    root.mainloop()