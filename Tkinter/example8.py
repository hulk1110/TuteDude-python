# step1: import tkinter
from tkinter import *
import tkinter.messagebox

# step2: gui interaction
window = Tk()

tkinter.messagebox.showerror("Info", "Running out time")
question = tkinter.messagebox.askokcancel("Weather","Will it rain?")

if question ==True :
    print("Take an umbrella")

else:
    print("okey")

mainloop()