# Thank you for viewing this code.
# A huge round of applause to Crossroads team for all those efforts.

# contact : +919544151856
# email : jijojohnlikeu@gmail.com

from math import *
from tkinter import *
from tkinter import ttk

calc = Tk()
calc.geometry("300x480+450+100")
calc.minsize(300,480)
# calc.resizable(0, 0)
calc.title("Calculator")
calc.iconbitmap('./Icon/calc_icon1.ico')

theme_var = IntVar()  # To change themes
view_var = IntVar()   # To toggle scientific view
inv_var = IntVar()    # To toggle Inverse functions in scientific view
next_oper = IntVar()  # To clear screen before a new entry


# show input on screen
def show(a):
    if isinstance(a, str):
        next_oper.set(0)
        en.insert(END, a)
    else:
        if next_oper.get() == 1:
            clear("c")
        next_oper.set(0)
        # if the input is a tkinter event
        en.insert(END, a.widget["text"])


# clear all or delete backwards
def clear(a):
    if a == "b":
        temp = en.get()
        en.delete(0, END)
        en.insert(END, temp[0:-1])
    else:
        en.delete(0, END)
        en_top.delete(0, END)


# get input, evaluate and show answer
def operate():
    value = en.get()
    en_top.delete(0, END)
    en.delete(0, END)
    # To avoid error from input like '10(2+2)'
    if "(" in value:
        if value.split("(")[0][-1:].isnumeric():
            temp = value.split("(")[0] + "*(" + value.split("(")[1]
            value = temp

    en_top.insert(END, str(value))
    en.insert(END, eval(str(value)))
    history_entry.append(str(value) + " = " + str(eval(str(value))))
    next_oper.set(1)


# get value and do scientific operations
def sci_operate(a):
    value = ""
    if isinstance(a, str):
        op = a
    else:
        op = a.widget["text"]

    # If tried to operate without entering value except for pi.
    if en.get() == "" and op != "\u03C0":
        en_top.delete(0, END)
        en_top.insert(END, "Enter value,then calculate")
    else:
        en_top.delete(0, END)
        value = en.get()

    if op == "%" and en.get() != "" or op == "!" and en.get() != "":
        en_top.insert(END, value + op)
    elif op == "\u221A" and en.get() != "":
        en_top.insert(END, op + value)
    elif op == "\u03C0":
        en_top.insert(END, op)
    else:
        if en.get() != "":
            en_top.insert(END, op + "(" + value + ")")

    en.delete(0, END)
    if op == "sin":
        en.insert(END, sin(radians(float(value))))
    elif op == "cos":
        en.insert(END, cos(radians(float(value))))
    elif op == "tan":
        en.insert(END, tan(radians(float(value))))
    elif op == "sinh":
        en.insert(END, sinh(radians(float(value))))
    elif op == "cosh":
        en.insert(END, cosh(radians(float(value))))
    elif op == "tanh":
        en.insert(END, tanh(radians(float(value))))
    elif op == "sin\u207b\u00B9":
        en.insert(END, degrees(asin(float(value))))
    elif op == "cos\u207b\u00B9":
        en.insert(END, degrees(acos(float(value))))
    elif op == "tan\u207b\u00B9":
        en.insert(END, degrees(atan(float(value))))
    elif op == "sinh\u207b\u00B9":
        en.insert(END, degrees(asinh(float(value))))
    elif op == "cosh\u207b\u00B9":
        en.insert(END, degrees(acosh(float(value))))
    elif op == "tanh\u207b\u00B9":
        en.insert(END, degrees(atanh(float(value))))
    elif op == "%":
        en.insert(END, eval(value + "/100"))
    elif op == "!":
        en.insert(END, factorial(int(value)))
    elif op == "\u221A":
        en.insert(END, sqrt(int(value)))
    elif op == "\u03C0":
        en.insert(END, pi)

    history_entry.append(str(en_top.get()) + " = " + str(en.get()))


# To save history
history_entry = []


# Show history and to use selected history.
def history():
    hist = Tk()
    hist.title("History")
    hist.geometry("250x320+770+100")
    hist.minsize(250, 320)
    scrollbar = Scrollbar(hist)
    scrollbar.pack(side=RIGHT, fill=Y)

    def histuse():
        selection = listbox.get(listbox.curselection())
        clear("c")
        en_top.insert(END, selection.split("=")[0])
        en.insert(END, selection.split("=")[1].strip())

    listbox = Listbox(hist, font=("Helvetica", 18, 'normal'))
    listbox.pack(fill=BOTH)
    use = ttk.Button(hist, text="Use", command=histuse)
    use.pack(expand=True, fill="both")

    if history_entry == []:
        listbox.insert(END, " Empty")
    for i in history_entry:
        listbox.insert(END, " " + i)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    mainloop()


# For changing theme as selection.
def theme():
    extra_num = [btn_zero, btn_dot]
    extra_opt = [btn_sqr, btn_div, btn_multi, btn_plus, btn_minus]
    # value of theme_var become index of list of colors in color list.
    for i in numbtns:
        i.configure(background=color[theme_var.get()][2],
                    fg=color[theme_var.get()][0])
    for i in extra_num:
        i.configure(background=color[theme_var.get()][2],
                    fg=color[theme_var.get()][0])
    for i in extra_opt:
        i.configure(background=color[theme_var.get()][6],
                    fg=color[theme_var.get()][1])
    for i in sci_list:
        i.configure(background=color[theme_var.get()][6],
                    fg=color[theme_var.get()][1])
    btn_clear.configure(background=color[theme_var.get()][3],
                        fg=color[theme_var.get()][1])
    btn_back.configure(background=color[theme_var.get()][4],
                       fg=color[theme_var.get()][1])
    btn_equal.configure(background=color[theme_var.get()][5],
                        fg=color[theme_var.get()][1])
    en.configure(background=color[theme_var.get()][7],
                 fg=color[theme_var.get()][8])
    en_top.configure(background=color[theme_var.get()][7],
                     fg=color[theme_var.get()][8])


# Changes for scientific view.
def scientific():
    calc.geometry("300x520+450+100")
    for i in scienframe:
        i.pack(expand=True, fill="both")
    for i in sci_list:
        i.configure(font=("Verdana", 14), relief=GROOVE,
                    border=0, background=color[theme_var.get()][6],
                    fg=color[theme_var.get()][1])
        i.pack(side=LEFT, expand=True, fill="both")


# for changing back to standard view.
def standard():
    for i in sci_list:
        i.pack_forget()
    for i in scienframe:
        i.pack_forget()
    calc.geometry("300x480+450+100")


count = True


# For toggling inverse functions in scientific view
def inverse():
    global count
    count = not count
    # If inverse is selected
    if not count:
        sci_inv.configure(background="#f48c06", fg="#fff")
        for i in sci_list[:6]:
            temp = i.cget("text")
            temp1 = temp + "\u207b\u00B9"
            i.configure(text=temp1, command="")
            i.bind('<Button-1>', sci_operate)
        sci_list[6].configure(text="10^", command=lambda: show("10**"))
        sci_list[7].configure(text="e\u02e3", command=lambda: show("e**"))
    # If not selected
    elif count:
        sci_inv.configure(background=color[theme_var.get()][6], fg=color[theme_var.get()][1])
        for i in sci_list[:6]:
            temp = i.cget("text")
            temp1 = temp.replace("\u207b\u00B9", "")
            i.configure(text=temp1, command="")
            i.bind('<Button-1>', sci_operate)
        sci_list[6].configure(text="log", command=lambda: sci_operate("log"))
        sci_list[7].configure(text="ln", command=lambda: sci_operate("ln"))


# Each list of colors for each theme.
#      0butFont, 1operFont, 2number,   3clear,    4back,    5equal,   6operator,  7screen, 8scrn_font
color = [["#000", "#fff", "#f1faee", "#e63946", "#f48c06", "#aacc00", "#2a9d8f", "#264653", "#fff"],
         ["#000", "#000", "#cbf3f0", "#ffbf69", "#2ec4b6", "#ff9f1c", "#2ec4b6", "#fdfffc", "#000"],
         ["#000", "#fff", "#d9d9d9", "#353535", "#353535", "#284b63", "#353535", "#ffffff", "#000"],
         ["#000", "#fff", "#edf2f4", "#d80032", "orange", "#2b2d42", "teal", "#073b4c", "#fff"],
         ["#fff", "#fff", "#000", "#000", "#000", "orange", "#000", "#000", "#fff"]]


# For hovering effect of number buttons.
def hoverin(a):
    numbtns[int(a.widget["text"]) - 1].configure(background="#a8dadc", fg="#000")


def hoverout(a):
    numbtns[int(a.widget["text"]) - 1].configure(background=color[theme_var.get()][2], fg=color[theme_var.get()][0])


# Frame for Entry boxes
entry_frame = Frame(calc)
entry_frame.pack(expand=True, fill="both", ipady=12)

# Top entry screen.
en_top = Entry(entry_frame, font=("Helvetica", 16, 'normal'),
               background=color[theme_var.get()][7],
               fg=color[theme_var.get()][8],
               border=0, justify=RIGHT)
en_top.pack(expand=True, fill="both")
# Main entry screen
en = Entry(entry_frame, font=("Helvetica", 25, 'bold'),
           background=color[theme_var.get()][7],
           fg=color[theme_var.get()][8],
           border=0, justify=RIGHT)
en.pack(expand=True, fill="both", ipady=12)

# Frame for scientific buttons
scienframe = [Frame(entry_frame, background=color[theme_var.get()][7]) for i in range(3)]

# Frame for buttons and standard functions.
btnframe = [Frame(calc) for i in range(5)]
for i in btnframe:
    i.pack(expand=True, fill="both")

# Number buttons from 1 to 9
numbtns = [Button(btnframe[4 - ceil(i / 3)],
                  text=str(i), font=("Verdana", 22),
                  relief=GROOVE, border=0,
                  background=color[theme_var.get()][2],
                  fg=color[theme_var.get()][0]) for i in range(1, 10)]
for i in numbtns:
    i.pack(side=LEFT, expand=True, fill="both")
    i.bind('<Button-1>', show)
    i.bind('<Enter>', hoverin)
    i.bind('<Leave>', hoverout)


# Other buttons on standard view.
btn_clear = Button(btnframe[0], text="C", command=lambda: clear("c"),
                   font=("Verdana", 22, 'bold'), relief=GROOVE,
                   border=0, background=color[theme_var.get()][3],
                   fg=color[theme_var.get()][1])
btn_clear.pack(side=LEFT, expand=True, fill="both", ipadx=3)
btn_back = Button(btnframe[0], text="\u2b05", command=lambda: clear("b"),
                  font=("Verdana", 22, 'bold'), relief=GROOVE,
                  border=0, background=color[theme_var.get()][4],
                  fg=color[theme_var.get()][1])
btn_back.pack(side=LEFT, expand=True, fill="both")
btn_sqr = Button(btnframe[0], text="x\u207f", command=lambda: show("**"),
                 font=("Verdana", 22, 'bold'), relief=GROOVE,
                 border=0, background=color[theme_var.get()][6],
                 fg=color[theme_var.get()][1])
btn_sqr.pack(side=LEFT, expand=True, fill="both", ipadx=2)
btn_div = Button(btnframe[0], text="/", command=lambda: show("/"),
                 font=("Verdana", 22, 'bold'), relief=GROOVE,
                 border=0, background=color[theme_var.get()][6],
                 fg=color[theme_var.get()][1])
btn_div.pack(side=LEFT, expand=True, fill="both", ipadx=3)
btn_multi = Button(btnframe[1], text="*", command=lambda: show("*"),
                   font=("Verdana", 23, 'bold'), relief=GROOVE,
                   border=0, background=color[theme_var.get()][6],
                   fg=color[theme_var.get()][1])
btn_multi.pack(side=LEFT, expand=True, fill="both", ipadx=0)
btn_minus = Button(btnframe[2], text="-", command=lambda: show("-"),
                   font=("Verdana", 25, 'bold'), relief=GROOVE,
                   border=0, background=color[theme_var.get()][6],
                   fg=color[theme_var.get()][1])
btn_minus.pack(side=LEFT, expand=True, fill="both", ipadx=2)
btn_plus = Button(btnframe[3], text="+", command=lambda: show("+"),
                  font=("Verdana", 22, 'bold'), relief=GROOVE,
                  border=0, background=color[theme_var.get()][6],
                  fg=color[theme_var.get()][1])
btn_plus.pack(side=LEFT, expand=True, fill="both")
btn_zero = Button(btnframe[4], text="0", command=lambda: show("0"),
                  font=("Verdana", 22), relief=GROOVE, border=0,
                  background=color[theme_var.get()][2],
                  fg=color[theme_var.get()][0])
btn_zero.pack(side=LEFT, expand=True, fill="both")
btn_dot = Button(btnframe[4], text=".", command=lambda: show("."),
                 font=("Verdana", 22), relief=GROOVE, border=0,
                 background=color[theme_var.get()][2],
                 fg=color[theme_var.get()][0])
btn_dot.pack(side=LEFT, expand=True, fill="both", ipadx=2)
btn_equal = Button(btnframe[4], text="=", command=operate,
                   font=("Verdana", 22, 'bold'), relief=GROOVE, border=0,
                   background=color[theme_var.get()][5],
                   fg=color[theme_var.get()][1])
btn_equal.pack(side=LEFT, expand=True, fill="both", ipadx=36)


# Scientific Buttons
sci_br1 = Button(scienframe[0], text="  (  ", command=lambda: show("("))
sci_br2 = Button(scienframe[0], text="  )  ", command=lambda: show(")"))
sci_prcnt = Button(scienframe[0], text=" % ", command=lambda: sci_operate("%"))
sci_fact = Button(scienframe[0], text="n!", command=lambda: sci_operate("!"))
sci_inv = Button(scienframe[0], text="Inv", command=inverse)
sci_sin = Button(scienframe[1], text="sin", command=lambda: sci_operate("sin"))
sci_cos = Button(scienframe[1], text="cos", command=lambda: sci_operate("cos"))
sci_tan = Button(scienframe[1], text="tan", command=lambda: sci_operate("tan"))
sci_ln = Button(scienframe[1], text="ln", command=lambda: sci_operate("ln"))
sci_pi = Button(scienframe[1], text="\u03C0", command=lambda: sci_operate("\u03C0"))
sci_sinh = Button(scienframe[2], text="sinh", command=lambda: sci_operate("sinh"))
sci_cosh = Button(scienframe[2], text="cosh", command=lambda: sci_operate("cosh"))
sci_tanh = Button(scienframe[2], text="tanh", command=lambda: sci_operate("tanh"))
sci_log = Button(scienframe[2], text="log", command=lambda: sci_operate("log"))
sci_root = Button(scienframe[2], text="\u221A", command=lambda: sci_operate("\u221A"))
sci_list = [sci_sin, sci_cos, sci_tan, sci_sinh, sci_cosh, sci_tanh,
            sci_log, sci_ln, sci_br1, sci_br2, sci_prcnt, sci_fact, sci_pi, sci_root, sci_inv]

# Top Menubar and Menu Items
menubar = Menu(calc)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_radiobutton(label="Standard", variable=view_var, value=0, command=standard)
viewmenu.add_radiobutton(label="Scientific", variable=view_var, value=1, command=scientific)

viewmenu.add_separator()

viewmenu.add_command(label="Exit", command=calc.quit)
menubar.add_cascade(label="View", menu=viewmenu)

thememenu = Menu(menubar, tearoff=0)

thememenu.add_radiobutton(label="Default", variable=theme_var, value=0, command=theme)
thememenu.add_radiobutton(label="light", variable=theme_var, value=1, command=theme)
thememenu.add_radiobutton(label="Minimal", variable=theme_var, value=2, command=theme)
thememenu.add_radiobutton(label="Vivid", variable=theme_var, value=3, command=theme)
thememenu.add_radiobutton(label="Dark", variable=theme_var, value=4, command=theme)

menubar.add_cascade(label="Themes", menu=thememenu)

historymenu = Menu(menubar, tearoff=0)
historymenu.add_command(label="Show history", command=history)
menubar.add_cascade(label="History", menu=historymenu)

calc.config(menu=menubar)
calc.mainloop()