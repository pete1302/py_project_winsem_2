import tkinter as tk  
from functools import partial 
import numpy as np
from csvhandler import *
from tkinter import messagebox

root = tk.Tk()  
# root.geometry('400x200')  
n = tk.StringVar()

v = tk.IntVar()

# root.title('')  

# def ShowChoice():
#     for i in lngs[1]:

#         print(i.get())

k = 0 
# varlist = []
list1 = importcsv()
# for i in list1:
#     var = tk.IntVar()
#     tk.Checkbutton(root, 
#                    text=i,
#                    padx = 20, 
#                    variable=var,

#                    ).grid(row = k+2 , column=0)
#     varlist.append(var)
#     k += 1

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

checklist = tk.Text(root, width=20)
checklist.pack()

vars = []
for i in list1:
    var = tk.IntVar()
    vars.append(var)
    checkbutton = tk.Checkbutton(checklist, text=i, variable=var)
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n")

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)

# disable the widget so users can't insert text into it
checklist.configure(state="disabled")


def state():
      return map((lambda var: var.get()), vars)

def allstates(): 
    # disp()
    print(list(state()))
    
    disp(exportcsv(list(state())))

def disp(absentlist):
    # tk.messagebox.showinfo("here is the dialog pane ")
    messagebox.showinfo( "absent "  , " absent {}".format(absentlist) )


exitbtn = tk.Button(root , text='EXIT' , bg='red' ,foreground='orange' , command=root.destroy).pack()
showbtn = tk.Button(root , text='SHOW' , bg='red' ,foreground='orange' , command=allstates).pack()

root.mainloop()