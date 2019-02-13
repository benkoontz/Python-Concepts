# drop down menus

from tkinter import *

def doNothing():
    print("ok ok i wont")

root = Tk()  # create a blank window

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu) # add dropdown submenu
subMenu.add_command(label="new project", command=doNothing)
subMenu.add_command(label="new", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="redo", command=doNothing)


root.mainloop()
