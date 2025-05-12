# step1: import tkinter
from tkinter import *


# step2: gui interaction
window = Tk()

window.geometry('500x500')

var = StringVar()
ent_var = StringVar()

def insert():
    result =ent_var.get()
    var.set(result)

message =Message(window,textvariable=var,relief=RAISED,padx=50,pady=50)
entry =Entry(window,textvariable=ent_var)
button =Button(window,text="OK",command=insert)
message.pack()
entry.pack()
button.pack()

mainloop()