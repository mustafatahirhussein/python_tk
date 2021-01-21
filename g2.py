
#grid layout

from tkinter import *

gui = Tk()

txt1 = Label(gui, text='Username : ')
txt2 = Label(gui, text='Password : ')

txt1.grid(row=1)
txt2.grid(row=3)

entry1 = Entry(gui)
entry2 = Entry(gui)

entry1.grid(row=1,column=2)
entry2.grid(row=3,column=2)
gui.mainloop()