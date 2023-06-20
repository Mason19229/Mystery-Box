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
        self.play_button = Button(self.gamble_frame, text="history", font="Arial 14", 
                                  padx=10, pady=10, command=lambda: self.Play(self.spin_list),)
        self.play_button.grid(row=1)

class Play:
    def __init__(self, partner, spin_list):

        background = "#A20025" #Red Brown

        #Disable play button
        partner.play_button.config(state=DISABLED)

        #Sets up child window
        self.play_box = Toplevel()

        #If user press cross at top, closes play and 'releases'
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play, partner))

        #Set up GUI Frame
        self.play_frame = Frame(self.play_box, bg=background)
        self.play_frame.grid()
        





    def balance():
        balance = 20 #Will take balance amount from user in actual program
        spins = 0

        while balance > 2 and spins < 10:
            balance = balance - 2
            prize_list = [0, 2, 4, 10]
            x = random.choices(prize_list, weights=(75, 10, 10, 5), k=1)
            balance = balance + x[0]
            spins += 1
            print("You got ${}, your total balance is ${} with {} spins".format(x, balance, spins))