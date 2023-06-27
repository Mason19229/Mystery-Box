from tkinter import *
from functools import partial #to prevent unwanted windows

import random

balance = 20 #Will take balance amount from user in actual program
spins = 0

class Mystery_Box:
    def __init__(self):
        
        #formatting variables...
        background_color = "light blue"       

        #in actual program this is blank and populated by user calculations
        global spin_list 
        #spin_list = ["you got $2, your total is now $20", "you got $4, your total is now $22", "you got $10, your total is now $30", "you got $0, your total is now $28", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20", "you got $2, your total is now $20"]
        spin_list = []

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
        self.play_button = Button(self.gamble_frame, text="play", font="Arial 14", 
                                  padx=10, pady=10, command=lambda: self.play(spin_list))
        self.play_button.grid(row=1)

    def play(self, spin_list):
        Play(self, spin_list)

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
        self.play_frame = Frame(self.play_box)
        self.play_frame.grid()

        #finding win text
        global spins
        global balance

        if balance > 2 and spins < 10:
            balance = balance - 2
            prize_list = [0, 2, 4, 10]
            x = random.choices(prize_list, weights=(75, 10, 10, 5), k=1)
            balance = balance + x[0]
            spins += 1
            win = ("You got ${}, your total balance is ${} with {} spins".format(x, balance, spins))
            


        #Set up Prize label
        self.play_label = Label(self.play_frame, text = win, font="Arial 12 bold", wrap=250)
        self.play_label.grid(row=0)

        #Dismiss button
        self.dismiss_button = Button(self.play_frame, text="Dismiss", font="Arial 12 bold", bg=background, command=partial(self.close_play, partner))
        self.dismiss_button.grid(row=1)

    def close_play(self, partner):
        #put history button back to normal
        if spins < 10:
            partner.play_button.config(state=NORMAL)
        self.play_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Gambling")
    something = Mystery_Box()
    root.mainloop()