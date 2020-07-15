# from tkinter import *
# import tkinter.font as font
#
# gui = Tk(className='Python Examples - Button')
# gui.geometry("500x200")
#
# # define font
# myFont = font.Font(family='Helvetica', size=20, weight='bold')
#
# # create button
# button = Button(gui, text='My Button', bg='#0052cc', fg='#ffffff')
# # apply font to the button label
# button['font'] = myFont
# # add button to gui window
# button.pack()

# gui.mainloop()

# from tkinter import *
# import tkinter.ttk as ttk
# import tkinter.font as font
#
# root = Tk()
# style = ttk.Style()
#
# myFont = font.Font(family='Poppins', size=10, weight='bold')
# style.configure("TButton", padding=6, relief="flat",
#    background="#ccc",width=8,height=2, font=myFont)
# style.configure("BW.TLabel", foreground="black", background="white")
#
# l1 = ttk.Label(text="Test", style="BW.TLabel")
# l2 = ttk.Label(text="Test", style="BW.TLabel")
# l1.pack()
# l2.pack()
#
# btn = ttk.Button(text="Sample")
# btn.pack()
#
# root.mainloop()
# import math
# a = 9
# print(math.ceil(a / 3))
# li = [1,2,3,4,5]
# print('x\u00b2')

# from math import *
#
# print(degrees(asin(1)))  # inverse
# print(sin(radians(90)))  # normal
# print(factorial(3))
# i = 5
# j = f"print(factorial({i}))"
# k = "10(2+2)"
# exec(j)
# if k.split("(")[0][-1:].isnumeric():
#     temp = k.split("(")[0]+"*("+k.split("(")[1]
#     k = temp
# print(eval(k))


from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from math import *

root = Tk()
root.geometry("124x160")
root.resizable(0, 0)
a = IntVar()
c1 = IntVar()
c2 = IntVar()
color = (["#000", "#fff"], ["#fff", "#000"], [])
fr = Frame(root)
fr.pack()



def theme():
    lab.configure(background=color[a.get()][0], fg=color[a.get()][1])


def custom():
    if a.get() == 2:
        temp1 = colorchooser.askcolor(color="white", title="Background")
        print(temp1[0])
        color[2].insert(0, temp1[1])
        temp2 = colorchooser.askcolor(color="black", title="Text")
        print(temp2[1])
        color[2].insert(1, temp2[1])
        theme()


def destroy():
    # for widget in fr1.winfo_children():
    #     widget.pack_forget()
    for i in li:
        i.pack_forget()
    root.geometry("124x160")

count = 0
def refresh():
    # for widget in fr.winfo_children():
    #     widget.pack()
    for i in li:
        i.pack(fill=BOTH, expand=True)
    root.geometry("124x260")


rd1 = ttk.Radiobutton(fr, text="Yes", variable=a, value=0, command=theme).pack()
rd2 = ttk.Radiobutton(fr, text="No", variable=a, value=1, command=theme).pack()
rd3 = Radiobutton(fr, text="Custom", variable=a, value=2, command=custom).pack()
en1 = Entry(fr).pack()
lab = Label(fr, text="Hello world", background=color[a.get()][0], fg=color[a.get()][1])
lab.pack()
bt1 = Button(fr, command=destroy, text="Delete").pack()
bt2 = Button(fr, command=refresh, text="Refresh").pack()

fr1 = Frame(root)
fr1.pack()
bt3 = ttk.Button(fr, command=destroy, text="sample1", name="bt3")
bt4 = ttk.Button(fr, command=refresh, text="sample2", name="bt4")
ch4 = ttk.Checkbutton(fr, text="ttkDemo", variable=c1, offvalue=0, onvalue=1)
ch5 = Checkbutton(fr, text="tkDemo", variable=c2, offvalue=0, onvalue=1)
li = [bt3, bt4, ch4,ch5]

print(degrees(asin(1)))
print(ceil(cos(radians(90))))
print(ceil(tan(radians(45))))

j = "#7a7a7a"
k = j.strip("#")
print(int(k,16))

root.mainloop()

