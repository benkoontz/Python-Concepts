
# shapes and graphics

from tkinter import *

root = Tk()  # create a blank window

canvas = Canvas(root, width = 200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50) # starts at coordinate 0, 0, 200 x direction, 50 y direction
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

canvas.delete(redLine) # delete the redLine
canvas.delete(ALL) # delete everything


root.mainloop()
