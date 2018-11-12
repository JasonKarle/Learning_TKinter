"""
A simple calculator program based on the example
from the YouTube course "How to create Game:
Python GUI 101 with TKiner Complete TUTORIAL"

https://www.youtube.com/watch?v=whErCLh0-QU

Modified and expanded to add window size, and
title label
   name:   Simple Tkinter Calculator no GUI
   ver:    1.0
   by:     Jason Karle
   date:   12 Nov 2018
"""

#imports

from tkinter import *

#window paramaters

root = Tk()
root.title("Simple Calculator")
root.geometry("300x75")

label1 = Label(root, text = "Entry your expression") 
label1.pack()

#definitions

def evaluate(event):
    data = userEntry.get() #gets the entered value!!!
    answer.config(text = "Answer: " + str(eval(data)))
    """
    configure the label "answer" using two arguments
    "text = " and the string of the data once evealuated
    "eval()"
    """
    
#main program
    
userEntry = Entry(root)
userEntry.bind("<Return>", evaluate) # event parameter must be in the def!!!!
userEntry.pack()

answer = Label(root)
answer.pack()

root.mainloop()
