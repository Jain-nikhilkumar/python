
import tkinter as tk

win=tk.Tk()
win.geometry("500x400")

# add frame1
frame1=tk.Frame(master=win,width=100,height=100,bg="orange")
frame1.pack(fill=tk.Y) # fill=tk.X,tk.Y,tk.BOTH

# add frame2
frame2=tk.Frame(master=win,width=50,height=50,bg="blue")
frame2.pack(fill=tk.Y)


# add frame3
fram3=tk.Frame(master=win,width=25,height=25,bg="green")
fram3.pack(fill=tk.Y)

win.mainloop()