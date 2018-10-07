# http://effbot.org/tkinterbook/button.htm
from tkinter import *

master = Tk()

def callback():
    print("click!")

for i, b in enumerate(9):
    row = int(i/3)
    col = i%3
    btn = Button(window, text=b, relief=GROOVE, width=2, command=callback)
    btn.grid(row=row, column=col, sticky="nsew")

mainloop()