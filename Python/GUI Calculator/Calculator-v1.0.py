#Thank you for viewing this code.
#A huge round of applause to Crossroads team for all those efforts.

#Please check Calculator_beta to view the latest additions to this version.

from tkinter import *
import math

calc = Tk()
calc.geometry("300x450+350+150")
calc.resizable(0, 0)
calc.title("Calculator")

def show(a):
    # print(a)
    if isinstance(a, str):
        en.insert(END, a)
    else:
        en.insert(END, a.widget["text"])

def clear():
    # lab.configure(text="")
    en.delete(0, END)

def operate():
    value = en.get()
    en.delete(0, END)
    en.insert(END, eval(str(value)))
    # lab.configure(text = eval(str(value)))

def hoverin(a):
    # print("kitti")
    numbtns[int(a.widget["text"])-1].configure(background="#a8dadc")
def hoverout(a):
    # print("poyi")
    numbtns[int(a.widget["text"])-1].configure(background="#f1faee")

enframe = Frame(calc, width=300, height=300)
enframe.pack(expand=True, fill="both", ipady=10)

en = Entry(enframe, font=("Helvetica", 25,'bold'), background="#264653", fg="#fff",justify=RIGHT)
en.pack(expand=True, fill="both", ipady=10)

btnframe = [Frame(calc) for i in range(4)]
for i in btnframe:
    i.pack(expand=True, fill="both")

numbtns = [Button(btnframe[math.ceil(i / 3) - 1], text=str(i), font=("Verdana", 22),
                  relief=GROOVE, border=0,background="#f1faee", fg="#000") for i in range(1, 10)]
for i in numbtns:
    i.pack(side=LEFT, expand=True, fill="both")
    i.bind('<Button-1>', show)
    i.bind('<Enter>', hoverin)
    i.bind('<Leave>', hoverout)

btn_plus = Button(btnframe[0], text="+", command=lambda: show("+"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_plus.pack(side=LEFT, expand=True, fill="both", ipadx=1)
btn_minus = Button(btnframe[1], text="-", command=lambda: show("-"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_minus.pack(side=LEFT, expand=True, fill="both", ipadx=6)
btn_multi = Button(btnframe[2], text="*", command=lambda: show("*"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_multi.pack(side=LEFT, expand=True, fill="both", ipadx=3)
btn_clear = Button(btnframe[3], text="C", command=clear, font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#e63946", fg="#fff")
btn_clear.pack(side=LEFT, expand=True, fill="both")
btn_zero = Button(btnframe[3], text="0", command=lambda: show("0"), font=("Verdana", 22), relief=GROOVE, border=0,background="#f1faee", fg="#000")
btn_zero.pack(side=LEFT, expand=True, fill="both", padx=3)
btn_equal = Button(btnframe[3], text="=", command=operate, font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#aacc00", fg="#fff")
btn_equal.pack(side=LEFT, expand=True, fill="both")
btn_div = Button(btnframe[3], text="/", command=lambda: show("/"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_div.pack(side=LEFT, expand=True, fill="both", ipadx=6)

# lab1 = Label(btnframe[4],text=('\u00A9 Jijo'),background="#f1faee", fg="#505050",font=("Helvetica", 12,'bold'),anchor=W)
# lab1.pack(side=LEFT, expand=True, fill="both")

calc.mainloop()

#contact : +919544151856
#email : jijojohnlikeu@gmail.com