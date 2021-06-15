from tkinter import *
from time import strftime
import datetime

root = Tk()
root.config(bg='black')
root.title("Clock")

def time():
    # string = strftime("%H:%M:%S %p")
    clock_string = strftime("%I:%M:%S %p")
    date_string = datetime.date.today()
    date_label.config(text=date_string)
    clock_label.config(text=clock_string)
    now = datetime.datetime.now()
    day_string = now.strftime("%A")
    day_name.config(text=day_string)
    clock_label.after(1000, time)


date_label = Label(root, font=("ds-digital", 30), background="black", foreground="cyan")
clock_label = Label(root, font=("ds-digital", 60), background="black", foreground="cyan")
day_name = Label(root, font=("ds-digital", 30), background="black", foreground="cyan")

clock_label.grid(row=0,columnspan=2)
date_label.grid(row=1,column=0)
day_name.grid(row=1,column=1)

time()
mainloop()
