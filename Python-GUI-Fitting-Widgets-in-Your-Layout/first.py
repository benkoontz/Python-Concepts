# fitting widgets in your layout

from tkinter import *

root = Tk()  # create a blank window

one = Label(root, text="one", bg="red", fg="white") # red background and white font
one.pack()
two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X) # fill the widget as wide as the parent is
three = Label(root, text="three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) # fill in the y direction

root.mainloop()
