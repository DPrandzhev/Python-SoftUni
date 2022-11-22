
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

def call():
    res = mb.askquestion('Exit Sirius?',
                         'Make sure nobody is watching!')

    if res == 'yes':
        # mb.showinfo('Return', 'There is always someone watching! Returning to Sirius')
        root.destroy()

    else:
        mb.showinfo('Return', 'Returning to Sirius')


root = tk.Tk()
canvas = tk.Canvas(root,
                   width=200,
                   height=200)

canvas.pack()
b = Button(root,
           text='RAGE QUIT',
           command=call)

canvas.create_window(100, 100,
                     window=b)


root.mainloop()
