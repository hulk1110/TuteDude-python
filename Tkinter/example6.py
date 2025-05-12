# step1: import tkinter
from tkinter import *
# step2: gui interaction
window = Tk()
# step3: adding input
window.title("Simple")
window.geometry("500x500")

def log_entry():
    print("Logged in")

button =Button(window,text="LOGIN", command=log_entry,width=12,bg="red",font=("bold",12),activebackground="white")
button.pack()

mainloop()