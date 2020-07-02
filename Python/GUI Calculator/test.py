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
from tkinter import *
from tkinter import colorchooser
from tkinter import ttk

root = Tk()
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
        color[2].insert(0, temp1[1])
        temp2 = colorchooser.askcolor(color="black", title="Text")
        color[2].insert(1, temp2[1])
        theme()

def destroy():
    for widget in fr1.winfo_children():
        widget.pack_forget()
    root.geometry("124x160")

def refresh():
    for widget in fr1.winfo_children():
        widget.pack()
    root.geometry("100x300")

rd1 = ttk.Radiobutton(fr, text="Yes", variable=a, value=0, command=theme).pack()
rd2 = ttk.Radiobutton(fr, text="No", variable=a, value=1, command=theme).pack()
rd3 = Radiobutton(fr, text="Custom", variable=a, value=2, command=custom).pack()
en1 = Entry(fr).pack()
lab = Label(fr, text="Hello world", background=color[a.get()][0], fg=color[a.get()][1])
lab.pack()
bt1 = Button(fr,command=destroy,text = "Delete").pack()
bt2 = Button(fr,command=refresh,text = "Refresh").pack()

fr1 = Frame(root)
fr1.pack()
bt3 = Button(fr1,command=destroy,text = "sample1",name="bt3")
bt4 = Button(fr1,command=refresh,text = "sample2",name="bt4")

root.mainloop()
