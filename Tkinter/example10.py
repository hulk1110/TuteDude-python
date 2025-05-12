# step1: import tkinter
from tkinter import *


# step2: gui interaction
window = Tk()

window.geometry('500x500')

var = StringVar()

message =Message(window,textvariable=var,relief=RAISED,padx=20,pady=20)
var.set("Welcome")
message.pack()

mainloop()