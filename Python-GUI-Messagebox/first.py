# message box

from tkinter import *
import tkinter.messagebox # allows to put message box on screen



root = Tk()  # create a blank window

tkinter.messagebox.showinfo('window title', "hello")

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print('*_*')




root.mainloop()
