# http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm
# Example are for Python 2! So some fixing is needed
from tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()
