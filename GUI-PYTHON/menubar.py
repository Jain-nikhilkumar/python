from tkinter import *

root=Tk()

def hello():
    print("hello")

menubar=Menu(root)
menubar.add_command(label="hellomenu",command=hello)
menubar.add_command(label="Exit",command=root.quit)

root.config(menu=menubar)
root.mainloop()