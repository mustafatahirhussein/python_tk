
from tkinter import *

root = Tk()
x = Label(root, text='Hello World')
x.pack()

fr = Frame(root)
fr.pack(fill=BOTH)

Button(fr, text='Python Button 1').pack(side=LEFT)
Button(fr, text='Python Button 1',foreground = 'Purple').pack(side=RIGHT)
Button(fr, text='Python Button 1', fg = 'Orange').pack()
root.mainloop()