import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window =tk.Tk()
window.title('Simple Calculator- By Indus')
#tkinter.messagebox.showinfo("Welcome","Thank You for using this calculator!")
frame = tk.Frame(master=window, bg="#F2EBE9", padx=15)
frame.pack()
entry = tk.Entry(master=frame,relief=SUNKEN,borderwidth=6,width=50, bg="#9DD6DF")
entry.grid(row=0, column=0,columnspan=4,ipady=2,pady=2)

def myclick(number):
    entry.insert(tk.END,number)

def equal():
    try:
        y =str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        entry.delete(0, tk.END)
        entry.insert(0,"Syntax Error")
        #tkinter.messagebox.showinfo("","Syntax error")

def clear():
    entry.delete(0,tk.END)

def bspace():
    val =str(entry.get())
    val =val[:-1]
    entry.delete(0, tk.END)
    entry.insert(0,val)

#button layout
but_1=tk.Button(master=frame,text='1',padx=15,pady=5,width=4,command=lambda: myclick(1),bg="#EEE3CB")
but_1.grid(row=1,column=0,pady=2)

but_2=tk.Button(master=frame,text='2',padx=15,pady=5,width=4,command=lambda: myclick(2),bg="#EEE3CB")
but_2.grid(row=1,column=1,pady=2)

but_3=tk.Button(master=frame,text='3',padx=15,pady=5,width=4,command=lambda: myclick(3),bg="#EEE3CB")
but_3.grid(row=1,column=2,pady=2)

but_4=tk.Button(master=frame,text='4',padx=15,pady=5,width=4,command=lambda: myclick(4),bg="#EEE3CB")
but_4.grid(row=2,column=0,pady=2)

but_5=tk.Button(master=frame,text='5',padx=15,pady=5,width=4,command=lambda: myclick(5),bg="#EEE3CB")
but_5.grid(row=2,column=1,pady=2)

but_6=tk.Button(master=frame,text='6',padx=15,pady=5,width=4,command=lambda: myclick(6),bg="#EEE3CB")
but_6.grid(row=2,column=2,pady=2)

but_7=tk.Button(master=frame,text='7',padx=15,pady=5,width=4,command=lambda: myclick(7),bg="#EEE3CB")
but_7.grid(row=3,column=0,pady=2)

but_8=tk.Button(master=frame,text='8',padx=15,pady=5,width=4,command=lambda: myclick(8),bg="#EEE3CB")
but_8.grid(row=3,column=1,pady=2)

but_9=tk.Button(master=frame,text='9',padx=15,pady=5,width=4,command=lambda: myclick(9),bg="#EEE3CB")
but_9.grid(row=3,column=2,pady=2)

but_0=tk.Button(master=frame,text='0',padx=15,pady=5,width=4,command=lambda: myclick(0),bg="#EEE3CB")
but_0.grid(row=4,column=1,pady=2)

but_dot=tk.Button(master=frame,text='.',padx=15,pady=5,width=4,command=lambda: myclick('.'),bg="#EEE3CB")
but_dot.grid(row=4,column=2,pady=2)

but_add=tk.Button(master=frame,text='+',padx=7.5,pady=5,width=4,command=lambda: myclick('+'),bg="#D7C0AE")
but_add.grid(row=3,column=3,pady=2)

but_sub=tk.Button(master=frame,text='-',padx=7.5,pady=5,width=4,command=lambda: myclick('-'),bg="#D7C0AE")
but_sub.grid(row=3,column=4,pady=2)

but_mul=tk.Button(master=frame,text='*',padx=15,pady=5,width=2,command=lambda: myclick('*'),bg="#D7C0AE")
but_mul.grid(row=4,column=3,pady=2)

but_div=tk.Button(master=frame,text='/',padx=15,pady=5,width=2,command=lambda: myclick('/'),bg="#D7C0AE")
but_div.grid(row=4,column=4,pady=2)

but_clr=tk.Button(master=frame,text='AC',padx=15,pady=5,width=8,command=clear,bg="#DF7861")
but_clr.grid(row=1,column=3,pady=2)

but_eql=tk.Button(master=frame,text="=",padx=15,pady=5,width=8,command=equal,bg="#DF7861")
but_eql.grid(row=2,column=3,pady=2)

but_del=tk.Button(master=frame,text="DEL",padx=15,pady=5,width=4,bg="#DF7861",command=bspace)
but_del.grid(row=4,column=0,pady=2)

window.mainloop()


