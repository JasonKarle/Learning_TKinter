"""
This is a very simple calculator with a simple GUI
that allows the user to add, subtract, multiple, and
divide. Based on the example from the YouTube course

"How to create Game: Python GUI 101 with TKiner Complete TUTORIAL"

https://www.youtube.com/watch?v=whErCLh0-QU

You can ONLY do one calculation at a time. Or in other
words, press equal once. Then you need to start a new
calculation (with or without hiiting clear)

This calculator DOES NOT rememeber the last answer, so
you can not continue to maniplate the last answer.

Future versions will stop the calc label from resizing
and MAY allow for continued calcualtions.

Modified and expanded to add window size, title label, and
better organize the program. (in my opinion that is!)
   name:   Simple Tkinter Calculator with GUI
   ver:    1.0
   by:     Jason Karle
   date:   12 Nov 2018
"""

#imports

from tkinter import *

#window parameters

root = Tk()
root.geometry("200x200")

#global variables

equaString = ""

#definitions

def btnPress(num):
    global equaString
    equaString += str(num)
    equation.set(equaString)

def equalPress():
    global equaString
    total = str(eval(equaString))
    equation.set(total)
    equaString = ""    

def clearPress():
    global equaString
    equation.set("0")
    equaString = ""

#main program

equation = StringVar() #makes equation a string var
equation.set("Enter your equation") 
             
calculation = Label(root, textvariable = equation)
calculation.grid(columnspan = 4)

#number buttons

Button0 = Button(root, text = "0", command = lambda: btnPress(0))
Button0.grid(row = 4, column = 1)
Button1 = Button(root, text = "1", command = lambda: btnPress(1))
Button1.grid(row = 3, column = 0)
Button2 = Button(root, text = "2", command = lambda: btnPress(2))
Button2.grid(row = 3, column = 1)
Button3 = Button(root, text = "3", command = lambda: btnPress(3))
Button3.grid(row = 3, column = 2)
Button4 = Button(root, text = "4", command = lambda: btnPress(4))
Button4.grid(row = 2, column = 0)
Button5 = Button(root, text = "5", command = lambda: btnPress(5))
Button5.grid(row = 2, column = 1)
Button6 = Button(root, text = "6", command = lambda: btnPress(6))
Button6.grid(row = 2, column = 2)
Button7 = Button(root, text = "7", command = lambda: btnPress(7))
Button7.grid(row = 1, column = 0)
Button8 = Button(root, text = "8", command = lambda: btnPress(8))
Button8.grid(row = 1, column = 1)
Button9 = Button(root, text = "9", command = lambda: btnPress(9))
Button9.grid(row = 1, column = 2)

#function buttons

ButtonMinus = Button(root, text = "-", command = lambda: btnPress("-"))
ButtonMinus.grid(row = 1, column = 4)
ButtonPlus = Button(root, text = "+", command = lambda: btnPress("+"))
ButtonPlus.grid(row = 2, column = 4)
ButtonDivide = Button(root, text = "/", command = lambda: btnPress("/"))
ButtonDivide.grid(row = 3, column = 4)
ButtonTimes = Button(root, text = "*", command = lambda: btnPress("*"))
ButtonTimes.grid(row = 4, column = 4)

#execution buttons

ButtonEqual = Button(root, text = "=", command = equalPress)
ButtonEqual.grid(row = 4, column = 2)

ButtonClear = Button(root, text = "C", command = clearPress)
ButtonClear.grid(row = 4, column = 0)

root.mainloop()
