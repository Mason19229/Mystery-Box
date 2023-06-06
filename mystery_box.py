from tkinter import *
from functools import partial #to present unwanted windows
import re

import random

class Mystery_Box:
    def __init__(self):

        #formatting variables
        background_color = "#008A00"


        #Initialise list to hold spin history
        self.all_spin_list = []

        #Gamble frame
        self.gamble_frame = Frame(width=490, height=360, bg=background_color,
                                  pady=10)
        self.gamble_frame.grid()

        #Title heading (row 0)
        self.mystery_box_label = Label(self.gamble_frame, text="Mystery Box Gambling",
                                       font=("Arial 16 bold"),
                                       bg=background_color,
                                       padx=10, pady=10)
        self.mystery_box_label.grid(row=0)

        #Split frame (row 1)
        self.split_page_frame = Frame(self.gamble_frame)
        self.split_page_frame.grid(row=1, pady=10)

        #Balance Display (row 1, column 1)
        self.balance_label = Label(self.split_page_frame, text=balance,
                                   font="arial 10 italic", justify=CENTER, Bg="#FFDF00")


        #Image Display (row 1, column 2)

        
        #Description


        #History


        #Help


        #Play


        #Summary
