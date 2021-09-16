
#Import Required Library 

import tkinter as tk
from tkinter import * 
from datetime import date
from typing import ValuesView


# Create Object 

root = Tk(className=" CALCULATOR") 
root.configure(background="lightgreen")
root.geometry("400x400+100+100")

    


tp=tk.Label(root,text="DATE CALCULATION",bg="lightgreen").place(x=10,y=10)
tp1=tk.Label(root,text="DATE1").place(x=40,y=110)
tp2=tk.Label(root,text="__________________________________________________________________________________________________________________",bg="lightgreen").place(x=0,y=140)
tp4=tk.Label(root,text="DATE2").place(x=40,y=180)
tp5=tk.Label(root,text="__________________________________________________________________________________________________________________",bg="lightgreen").place(x=0,y=210)
entry21=tk.Entry(root,width=25).place(x=100,y=180)
entry1=tk.Entry(root,width=25).place(x=100,y=110)



result=tk.Label(root,text='')


e1=entry1
e2=entry21

def btn_clik(e1,e2):
        
        dif=int(e1-e2)
        result.set(dif)
        

buton1=tk.Button(root,text="calculate",fg="black",width=13,height=2,).place(x=45,y=250)
Exit=tk.Button(root,text="Exit",fg="black",width=13,height=2,command=root.quit).place(x=200,y=250)
# Excecute Tkinter'''

root.mainloop()


'''def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression'''