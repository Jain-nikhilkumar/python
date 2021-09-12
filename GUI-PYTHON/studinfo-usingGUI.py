import tkinter as tk
from tkinter.constants import X
win=tk.Tk()
win.title("studinfo")

win.geometry('600x600+100+200')
name=tk.Label(win,text="FullName:").place(x=20,y=30)

address=tk.Label(win,text="Address :").place(x=20,y=60)
Email=tk.Label(win,text="Address :").place(x=20,y=90)
Schoolname=tk.Label(win,text="Address :").place(x=20,y=120)
Stding_in_year=tk.Label(win,text="Address :").place(x=20,y=150)
dob=tk.Label(win,text="DOB").place(x=20,y=180)


tp=tk.Label(win,text="_________________________________________________________").place(x=10,y=260)
e1=tk.Entry(win).place(x=80,y=30)
e2=tk.Entry(win).place(x=80,y=60)
e3=tk.Entry(win).place(x=80,y=90)
e4=tk.Entry(win).place(x=80,y=120)
e5=tk.Entry(win).place(x=80,y=150)
e6=tk.Entry(win).place(x=80,y=180)
Gender=tk.Label(win,text="Select Gender").place(x=20,y=280)
radio1=tk.Radiobutton(win,text="male",value=1).place(x=20,y=300)
radio2=tk.Radiobutton(win,text="Femail",value=0).place(x=20,y=320)

tp2=tk.Label(win,text="_________________________________________________________").place(x=10,y=350)
schooltype=tk.Label(win,text="Schooltype").place(x=20,y=370)
radio3=tk.Radiobutton(win,text="Marathi",value=1).place(x=20,y=390)
radio4=tk.Radiobutton(win,text="English",value=0).place(x=20,y=420)

tp3=tk.Label(win,text="_________________________________________________________").place(x=10,y=440)
School_Caregory=tk.Label(win,text="School_Caregory").place(x=20,y=460)
radio5=tk.Radiobutton(win,text="Convent",value=0).place(x=20,y=480)
radio6=tk.Radiobutton(win,text="Semi",value=1).place(x=20,y=500)

tp4=tk.Label(win,text="_________________________________________________________").place(x=10,y=520)
submit=tk.Button(win,text="Submit",activebackground="red",activeforeground="blue").place(x=10,y=550)



win.mainloop()