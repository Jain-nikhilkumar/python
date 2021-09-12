
  
# Geometry Managers : -->  grid() 

import tkinter as tk

win=tk.Tk()
win.geometry("500x400")
for i in range(5):
    for j in range(3):
        frame=tk.Frame(win,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=i,column=j,padx=5,pady=5)
        label=tk.Label(master=frame,text=f"Row {i} \n Column {j}")
        label.pack()
win.mainloop()