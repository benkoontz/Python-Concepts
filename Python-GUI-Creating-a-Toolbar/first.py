# Creating a Toolbar

from tkinter import *

def doNothing():
    print("ok ok i wont")

root = Tk()  # create a blank window

# ---- main menu ----

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

# ----- the toolbar -----

toolbar = Frame(root, bg="blue")
insertButton = Button(toolbar, text="insert image", command=doNothing)
insertButton.pack(side=LEFT,padx=2,pady=2) # padx is extra space
printButton = Button(toolbar, text="print", command=doNothing)
printButton.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP, fill = X) # positions the toolbar right under the menu



root.mainloop()
