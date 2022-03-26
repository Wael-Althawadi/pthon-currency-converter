from tkinter import *
import requests
from tkinter import messagebox


root = Tk()
root.title("Flight info")

frame = LabelFrame(root,padx = 100,pady =100,bg="#ccd1d1")
frame.pack(padx = 10,pady = 10)

label = Label(frame,text = "enter airport code")
label.grid(row = 0 ,column = 0)

entry = Entry(frame)
entry.grid(row = 1,column = 0)

def click():
    global req
    try:
        req = requests.get(f"https://api.flightapi.io/compschedule/61f81decce579974df992762?mode=departures&day=1&iata={entry.get()}").json()
        result = req[0]["airport"]["pluginData"]["details"]["name"]
        flights = [i["flight"]["airport"]["destination"]["timezone"]["name"] for i in req[0]["airport"]["pluginData"]["schedule"]["departures"]["data"]]
        response = messagebox.showinfo("airport info",f"{result} flights for today are \n{flights}")
    except: 
        messagebox.showerror("error message","code not found")
    
button = Button(frame, text = "Get info",bg = "#34495e",command = click)
button.grid(row = 2,column = 0,columnspan = 2)



mainloop()
