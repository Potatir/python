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


label = Label(text="something")
label.pack()
button = ttk.Button(text='something',command=finish)
button.place(relx=.5, rely=.5,anchor=CENTER, width=80, height=80)


first.protocol("KILL", finish)




first.mainloop()