# using classes

from tkinter import *

class BensButtons:
    def __init__(self, master):
        frame = Frame(master) # root is now master
        frame.pack()

        self.printButton = Button(frame, text="print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("wow this actually worked")


root = Tk()  # create a blank window
b = BensButtons(root)
root.mainloop()
