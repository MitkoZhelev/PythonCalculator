import tkinter
from tkinter import *

window = Tk()

window.title('Calculator')

window.geometry('500x500')
window.resizable(0, 0)

name_button = tkinter.Button(window, text='0')
name_button.grid(row=0, column=0)

window.mainloop()
