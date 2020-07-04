from tkinter import *
import math
from tkinter import ttk

calc = Tk()
calc.geometry("300x480+450+100")
calc.minsize(300,480)
# calc.resizable(0, 0)
calc.title("Calculator")
calc.iconbitmap('./Icon/calc_icon1.ico')

thm = IntVar()


def show(a):
    # print(a)
    if isinstance(a, str):
        en.insert(END, a)
    else:
        en.insert(END, a.widget["text"])


def clear(a):
    if a == "b":
        temp = en.get()
        en.delete(0, END)
        en.insert(END, temp[0:-1])
    else:
        en.delete(0, END)
        en_top.delete(0, END)


def operate():
    value = en.get()
    en_top.delete(0, END)
    en_top.insert(END, str(value))
    en.delete(0, END)
    en.insert(END, eval(str(value)))
    history_entry.append(str(value) + " = " + str(eval(str(value))))


history_entry = []


def history():
    hist = Tk()
    hist.title("History")
    hist.geometry("250x150+770+100")
    hist.minsize(250, 150)
    scrollbar = Scrollbar(hist)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(hist, font=("Helvetica", 18, 'normal'))
    listbox.pack(fill=BOTH)

    if history_entry == []:
        listbox.insert(END, "Nill")
    for i in history_entry:
        print(i)
        listbox.insert(END, " "+i)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    mainloop()


#      0butFont, 1operFont, 2number,   3clear,    4back,    5equal,   6operator,  7screen, 8scrn_font
color = [["#000", "#fff", "#f1faee", "#e63946", "#f48c06", "#aacc00", "#2a9d8f", "#264653", "#fff"],
         ["#000", "#000", "#cbf3f0", "#ff9f1c", "#2ec4b6", "#ffbf69", "#2ec4b6", "#fdfffc", "#000"],
         ["#000", "#fff", "#d9d9d9", "#353535", "#353535", "#284b63", "#353535", "#ffffff", "#000"],
         ["#fff", "#fff", "#000", "#000", "#000", "orange", "#000", "#000", "#fff"]]


def hoverin(a):
    # print("kitti")
    numbtns[int(a.widget["text"]) - 1].configure(background="#a8dadc", fg="#000")


def hoverout(a):
    # print("poyi")
    numbtns[int(a.widget["text"]) - 1].configure(background=color[thm.get()][2], fg=color[thm.get()][0])


entry_frame = Frame(calc)
entry_frame.pack(expand=True, fill="both", ipady=12)

en_top = Entry(entry_frame, font=("Helvetica", 16, 'normal'), background=color[thm.get()][7], fg=color[thm.get()][8],
               border=0, justify=RIGHT)
en_top.pack(expand=True, fill="both")
en = Entry(entry_frame, font=("Helvetica", 25, 'bold'), background=color[thm.get()][7], fg=color[thm.get()][8],
           border=0, justify=RIGHT)
en.pack(expand=True, fill="both", ipady=12)

btnframe = [Frame(calc) for i in range(5)]
for i in btnframe:
    i.pack(expand=True, fill="both")

numbtns = [Button(btnframe[4 - math.ceil(i / 3)], text=str(i), font=("Verdana", 22),
                  relief=GROOVE, border=0, background=color[thm.get()][2], fg=color[thm.get()][0]) for i in
           range(1, 10)]
for i in numbtns:
    i.pack(side=LEFT, expand=True, fill="both")
    i.bind('<Button-1>', show)
    i.bind('<Enter>', hoverin)
    i.bind('<Leave>', hoverout)


def theme():
    extra_num = [btn_zero, btn_dot]
    extra_opt = [btn_sqr, btn_div, btn_multi, btn_plus, btn_minus]
    for i in numbtns:
        i.configure(background=color[thm.get()][2], fg=color[thm.get()][0])
    for i in extra_num:
        i.configure(background=color[thm.get()][2], fg=color[thm.get()][0])
    for i in extra_opt:
        i.configure(background=color[thm.get()][6], fg=color[thm.get()][1])
    btn_clear.configure(background=color[thm.get()][3], fg=color[thm.get()][1])
    btn_back.configure(background=color[thm.get()][4], fg=color[thm.get()][1])
    btn_equal.configure(background=color[thm.get()][5], fg=color[thm.get()][1])
    en.configure(background=color[thm.get()][7], fg=color[thm.get()][8])
    en_top.configure(background=color[thm.get()][7], fg=color[thm.get()][8])


btn_clear = Button(btnframe[0], text="C", command=lambda: clear("c"), font=("Verdana", 22, 'bold'), relief=GROOVE,
                   border=0, background=color[thm.get()][3], fg=color[thm.get()][1])
btn_clear.pack(side=LEFT, expand=True, fill="both", ipadx=3)
btn_back = Button(btnframe[0], text="\u2b05", command=lambda: clear("b"), font=("Verdana", 22, 'bold'), relief=GROOVE,
                  border=0, background=color[thm.get()][4], fg=color[thm.get()][1])
btn_back.pack(side=LEFT, expand=True, fill="both")
btn_sqr = Button(btnframe[0], text="x\u207f", command=lambda: show("**"), font=("Verdana", 22, 'bold'), relief=GROOVE,
                 border=0, background=color[thm.get()][6], fg=color[thm.get()][1])
btn_sqr.pack(side=LEFT, expand=True, fill="both", ipadx=2)
btn_div = Button(btnframe[0], text="/", command=lambda: show("/"), font=("Verdana", 22, 'bold'), relief=GROOVE,
                 border=0, background=color[thm.get()][6], fg=color[thm.get()][1])
btn_div.pack(side=LEFT, expand=True, fill="both", ipadx=3)
btn_multi = Button(btnframe[1], text="*", command=lambda: show("*"), font=("Verdana", 23, 'bold'), relief=GROOVE,
                   border=0, background=color[thm.get()][6], fg=color[thm.get()][1])
btn_multi.pack(side=LEFT, expand=True, fill="both", ipadx=0)
btn_minus = Button(btnframe[2], text="-", command=lambda: show("-"), font=("Verdana", 25, 'bold'), relief=GROOVE,
                   border=0, background=color[thm.get()][6], fg=color[thm.get()][1])
btn_minus.pack(side=LEFT, expand=True, fill="both", ipadx=2)
btn_plus = Button(btnframe[3], text="+", command=lambda: show("+"), font=("Verdana", 22, 'bold'), relief=GROOVE,
                  border=0, background=color[thm.get()][6], fg=color[thm.get()][1])
btn_plus.pack(side=LEFT, expand=True, fill="both")
# btn_dzero = Button(btnframe[4], text="00", command=lambda: show("00"), font=("Verdana", 22), relief=GROOVE, border=0,background="#f1faee", fg="#000")
# btn_dzero.pack(side=LEFT, expand=True, fill="both")
btn_zero = Button(btnframe[4], text="0", command=lambda: show("0"), font=("Verdana", 22), relief=GROOVE, border=0,
                  background=color[thm.get()][2], fg=color[thm.get()][0])
btn_zero.pack(side=LEFT, expand=True, fill="both")
btn_dot = Button(btnframe[4], text=".", command=lambda: show("."), font=("Verdana", 22), relief=GROOVE, border=0,
                 background=color[thm.get()][2], fg=color[thm.get()][0])
btn_dot.pack(side=LEFT, expand=True, fill="both", ipadx=2)
btn_equal = Button(btnframe[4], text="=", command=operate, font=("Verdana", 22, 'bold'), relief=GROOVE, border=0,
                   background=color[thm.get()][5], fg=color[thm.get()][1])
btn_equal.pack(side=LEFT, expand=True, fill="both", ipadx=36)

# style = ttk.Style()
# style.configure("TRadiobutton", background="#f1faee", fg="#505050",
#                 font=("Helvetica", 12, 'bold'))
#
# lab1 = Label(btnframe[5], text=("Themes"), background="#f1faee", fg="#505050",
#              font=("Helvetica", 12), anchor=NW)
# lab1.pack(side=LEFT, expand=True, fill="both")
# rad1 = ttk.Radiobutton(btnframe[5], text="1", variable=thm, value=0, command=theme)
# rad1.pack(side=LEFT, expand=True, fill="both")
# rad2 = ttk.Radiobutton(btnframe[5], text="2", variable=thm, value=1, command=theme)
# rad2.pack(side=LEFT, expand=True, fill="both")
# rad3 = ttk.Radiobutton(btnframe[5], text="3", variable=thm, value=2, command=theme)
# rad3.pack(side=LEFT, expand=True, fill="both")
# rad4 = ttk.Radiobutton(btnframe[5], text="Dark", variable=thm, value=3, command=theme)
# rad4.pack(side=LEFT, expand=True, fill="both")
# lab2 = Label(btnframe[5], text=('\u00A9 Jijo'), background="#f1faee", fg="#505050", font=("Helvetica", 12, 'bold'),
#              anchor=E)
# lab2.pack(side=LEFT, expand=True, fill="both")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=calc.quit)
menubar.add_cascade(label="File", menu=filemenu)

thememenu = Menu(menubar, tearoff=0)

thememenu.add_radiobutton(label="Default", variable=thm, value=0, command=theme)
thememenu.add_radiobutton(label="light", variable=thm, value=1, command=theme)
thememenu.add_radiobutton(label="Minimal", variable=thm, value=2, command=theme)
thememenu.add_radiobutton(label="Dark", variable=thm, value=3, command=theme)

menubar.add_cascade(label="Themes", menu=thememenu)

historymenu = Menu(menubar, tearoff=0)
historymenu.add_command(label="Show history", command=history)
menubar.add_cascade(label="History", menu=historymenu)

calc.config(menu=menubar)
calc.mainloop()