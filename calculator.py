from tkinter import *




root3 = Tk()
root3.title("sample calculator")

# text above the input field

label1 = Label(root3,text="enter a number ").grid(row =2,column=1)

# the input dield

InpuT = Entry(root3,fg="blue",width=40,borderwidth=10)
InpuT.grid(row=3,column=0,columnspan=3)

# create fucnction

def click(number):
    cuurent = InpuT.get()
    InpuT.delete(0,END)
    InpuT.insert(0,str(cuurent) + str(number))

def clr():
    InpuT.delete(0,END)

def add():
    firist_n = InpuT.get()
    global math
    math = "add"
    global f_n
    f_n = int(firist_n)
    InpuT.delete(0,END)

def equel():
    second_n = InpuT.get()
    InpuT.delete(0,END)
    if math == "add":
        InpuT.insert(0,f_n + int(second_n))
    elif math == "sub":
        InpuT.insert(0,f_n - int(second_n))
    elif math == "mult":
        InpuT.insert(0,f_n * int(second_n))
    elif math == "divid":
        InpuT.insert(0,f_n / int(second_n))
    
    
def sub():
    firist_n = InpuT.get()
    global math
    math = "sub"
    global f_n
    f_n = int(firist_n)
    InpuT.delete(0,END)

def mult():
    firist_n = InpuT.get()
    global math
    math = "mult"
    global f_n
    f_n = int(firist_n)
    InpuT.delete(0,END)

def divid():
    firist_n = InpuT.get()
    global math
    math = "divid"
    global f_n
    f_n = int(firist_n)
    InpuT.delete(0,END)
# 123 buttons

button1 = Button(root3,text="1",padx=40,pady=20,command=lambda:click(1)).grid(row=5,column=0)
button2 = Button(root3,text="2",padx=40,pady=20,command=lambda:click(2)).grid(row=5,column=1)
button3 = Button(root3,text="3",padx=40,pady=20,command=lambda:click(3)).grid(row=5,column=2)
# 456 buttons

button4 = Button(root3,text="4",padx=40,pady=20,command=lambda:click(4)).grid(row=6,column=0)
button5 = Button(root3,text="5",padx=40,pady=20,command=lambda:click(5)).grid(row=6,column=1)
button6 = Button(root3,text="6",padx=40,pady=20,command=lambda:click(6)).grid(row=6,column=2)

# 789 buttons

button7 = Button(root3,text="7",padx=40,pady=20,command=lambda:click(7)).grid(row=7,column=0)
button8 = Button(root3,text="8",padx=40,pady=20,command=lambda:click(8)).grid(row=7,column=1)
button9 = Button(root3,text="9",padx=40,pady=20,command=lambda:click(9)).grid(row=7,column=2)
button0 = Button(root3,text="0",padx=40,pady=20,command=lambda:click(0)).grid(row=8,column=0)


# + , = and clear buttons

button10 = Button(root3,text="+",padx=90,pady=20,command=add).grid(row=9,column=1,columnspan=2)
button13 = Button(root3,text="-",padx=40,pady=20,command=sub).grid(row=10,column=0)
button14 = Button(root3,text="*",padx=40,pady=20,command=mult).grid(row=10,column=1)
button15 = Button(root3,text="/",padx=40,pady=20,command=divid).grid(row=10,column=2)


button11 = Button(root3,text="clear",padx=27,pady=20,command=clr).grid(row=9,column=0)

button12 = Button(root3,text="=",padx=90,pady=20,command=equel).grid(row=8,column=1,columnspan=2)

    
mainloop()

