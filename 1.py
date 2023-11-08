from tkinter import *
from tkinter import ttk

first = Tk()
first.title("something")
first.geometry("300x250")
first.resizable(False, False)
first.attributes("-fullscreen", True)
first.attributes("-toolwindow", True)
def finish():
    first.destroy()

make_some_tea = True



if make_some_tea:
    print("some tea")


for i in range(3):
    for g in range(3):
        btn = ttk.Button(text=f"({i},{g})")
        btn.grid(row=i, column=g)




first.protocol("KILL", finish)




first.mainloop()