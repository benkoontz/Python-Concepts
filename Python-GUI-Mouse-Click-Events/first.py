# Binding Function to Layouts

from tkinter import *

root = Tk()  # create a blank window

def leftClick(event):
    print("Left")

def middleclick(event):
    print("middle")

def rightClick(event):
    print("right")

frame = Frame(root, width = 300, height = 250) # 300 px by 250 px
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightClick)

frame.pack()



root.mainloop()
