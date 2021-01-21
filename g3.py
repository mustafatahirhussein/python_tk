
from tkinter import *
import _datetime
import time


gui = Tk()
gui.title('Payment System')
gui.geometry('1440x900+0+0')
fr = Frame(gui, height = 70, width=1440, border=2 ,relief=GROOVE)
fr.pack(side=TOP)
f1 = Frame(gui, height=700, width=700, bd=2, relief=GROOVE)
f1.pack(side=LEFT)
f2=Frame(gui,width= 400, height=700, bd=2, relief=GROOVE)
f2.pack(side=RIGHT)
f3=Frame(f1, width=700, height=300, bd=2, relief=GROOVE)
f3.pack(side=TOP)
f4 = Frame(f1, height=700, width=700, bd=2, relief=GROOVE)
f4.pack(side=TOP)
lb1 = Label(fr, text='         Payment Management System          ', font=('arial', 54, 'bold'), bd=5)
lb1.grid(row=0,column=0)

Name=StringVar()
Address=StringVar()
Employer=StringVar()
Hours_Worked=StringVar()
Hour_Rate=StringVar()
Tax=StringVar()
Overtime=StringVar()
Gross_Salary=StringVar()
Net_amount=StringVar()
date = StringVar()

date.set(time.strftime('%d/%m/%Y'))

lb2= Label(f3, text='Name ', font=('arial', 12, 'bold'), bd=2).grid(row=0)
lb3= Label(f3, text='Address ', font=('arial', 12, 'bold'), bd=2).grid(row=1)
lb4= Label(f3, text='Employer ', font=('arial', 12, 'bold'), bd=2).grid(row=2)
lb5= Label(f3, text='Hours Worked ', font=('arial', 12, 'bold'), bd=2).grid(row=3)
lb6= Label(f3, text='Hour Rate ', font=('arial', 12, 'bold'), bd=2).grid(row=4)
lb7= Label(f3, text='Tax ', font=('arial', 12, 'bold'), bd=2).grid(row=5)
lb8= Label(f3, text='Overtime ', font=('arial', 12, 'bold'), bd=2).grid(row=6)
lb9= Label(f3, text='Gross Salary ', font=('arial', 12, 'bold'), bd=2).grid(row=7)
lb10= Label(f3, text='Net amount ', font=('arial', 12, 'bold'), bd=2).grid(row=8)

e1 = Entry(f3, textvariable= Name ,font=('arial',12,'bold')).grid(row=0,column=1)
e2 = Entry(f3, textvariable= Address ,font=('arial',12,'bold')).grid(row=1,column=1)
e3 = Entry(f3, textvariable= Employer ,font=('arial',12,'bold')).grid(row=2,column=1)
e4 = Entry(f3, textvariable= Hours_Worked ,font=('arial',12,'bold')).grid(row=3,column=1)
e5 = Entry(f3, textvariable= Hour_Rate ,font=('arial',12,'bold')).grid(row=4,column=1)
e6 = Entry(f3, textvariable= Tax ,font=('arial',12,'bold')).grid(row=5,column=1)
e7 = Entry(f3, textvariable= Overtime ,font=('arial',12,'bold')).grid(row=6,column=1)
e8 = Entry(f3, textvariable= Gross_Salary ,font=('arial',12,'bold')).grid(row=7,column=1)
e9 = Entry(f3, textvariable= Net_amount ,font=('arial',12,'bold')).grid(row=8,column=1)

e10 = Entry(f2, textvariable=date ,font=('arial',12,'bold')).grid(row=0,column=0)
gui.mainloop()
