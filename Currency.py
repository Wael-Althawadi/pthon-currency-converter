import requests 
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
import datetime
from PIL import Image, ImageTk


req = requests.get("https://www.coingecko.com")
soup = bs(req.text,"lxml")

a = [i.text.strip() for i in soup.find_all(class_="tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between")]
    
c = [x.text.strip() for x in soup.find_all(class_="td-price price text-right pl-0")]
    
result = [(i,x) for i,x in zip(a,c) ]


root = Tk()
root.title("coin price")



img = ImageTk.PhotoImage(Image.open("/home/wael/Desktop/C_p.jpg"))

l = Label(image = img)
l.grid(row = 0,column= 0,sticky=NSEW,rowspan=4)





l_1 = Label(root,text="enter a coin name  ",padx=50,pady=20)
l_1.grid(row= 0 , column = 0,rowspan =3)

e_1 = Entry(root,width=40,borderwidth=10)
e_1.grid(row = 1 ,column = 0,rowspan=2)
e_1.insert(0,"the coin name")


 
def click():
    name = e_1.get()
    for n,p in result:
        if name == n:
            label_1 = Label(root,text = f" {p}")
            label_1.grid(row=3,column=0,columnspan=2)

            

b_1 = Button(root,text = "show price",command = click)
b_1.grid(row = 2,column = 0)


def clear():
    e_1.delete(0,END)

"""
b_2 = Button(root,text = "clear",command = clear)
b_2.grid(row =3 ,column = 0)
"""

mainloop()
