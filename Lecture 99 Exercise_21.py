# CP3_Tiraphat_Saeseai
import math
from tkinter import *

def leftClickButton(event):
    print(float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2))
    labelResult.configure(text=float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2))
    if float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2)>=30:
        textboxBMI.configure(text="อ้วนมาก")
    elif float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2)>=25:
        textboxBMI.configure(text="อ้วน")
    elif float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2)>=23:
        textboxBMI.configure(text="น้ำหนักเกิน")
    elif float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2)>=18.6:
        textboxBMI.configure(text="ปกติ")
    elif float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2)<18:
        textboxBMI.configure(text="ผอมเกินไป")



Mainwindow = Tk()
labelHight = Label(Mainwindow,text="Tall (cm.)")
labelHight.grid(row=0,column=0)
textboxHight = Entry(Mainwindow)
textboxHight.grid(row=0,column=1)
labelWeight = Label(Mainwindow,text="Weight (kg.)")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(Mainwindow)
textboxWeight.grid(row=1,column=1)
Calculate = Button(Mainwindow,text="Calaculata")
Calculate.grid(row=2,column=0)
Calculate.bind('<Button-1>',leftClickButton)
labelResult = Label(Mainwindow,text="Result")
labelResult.grid(row=2,column=1)
textboxBMI = Label(Mainwindow,text="Result")
textboxBMI.grid(row=3,column=1)
Mainwindow.mainloop()
