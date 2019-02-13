# This Program shows how to use grid layout

from tkinter import *

root = Tk()  # create a blank window

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root) # field where user can type in
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) # column is 0 by defualt, E means place to the right (East)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="keep me logged in")
c.grid(columnspan=2) # span two columns

root.mainloop()
