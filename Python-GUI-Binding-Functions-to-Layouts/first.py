# Binding Function to Layouts

from tkinter import *

root = Tk()  # create a blank window

def printName(event): 
    print("hello my name is ben")

button_1 = Button(root, text = "print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
