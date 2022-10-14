
from dataclasses import asdict, dataclass
from re import A
from sqlite3 import adapt
import pyautogui
from tkinter import *
import time

def letsgo():
    text = (gettext.get())
    reps = (getnum.get())
    reps = int(reps) 
    name = (getname.get())
    time.sleep(3)
    pyautogui.hotkey('win','s')
    time.sleep(2)
    pyautogui.write("WhatsApp")
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.hotkey('ctrl','f')
    time.sleep(0.5)
    pyautogui.write(name)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(reps):
        pyautogui.write(text)
        pyautogui.press("enter")
    gettext.set("")
    getnum.set("")
    getname.set("")
    pyautogui.alert("Completed","Status")

root = Tk()

root.title("Whatsapp Spam Bot")
root.resizable(0,0)
root.config(background='#e6ffe6')

fr = Frame(root,padx=20, pady=20, bg="#04AA6D")
fr.pack()

l1 = Label(fr, text="Enter your Message", padx=20, pady=10, bg='#04e096', width=24, font=('BouncyPERSONALUSEONLY'), fg='#e6ffe6')
l1.grid(row = 0, column = 0, columnspan = 2)

gettext = StringVar()
e1 = Entry(fr, textvariable= gettext,bg='#04e096', fg='white', width=24, font=('BouncyPERSONALUSEONLY'))
e1.grid(row = 0, column = 4, columnspan = 2)

l2 = Label(fr, text="Enter no. of repetitions", padx=20, pady=10, bg='#04e096', width=24, font=('BouncyPERSONALUSEONLY'), fg='#e6ffe6')
l2.grid(row = 1, column = 0, columnspan = 2)

getnum = StringVar()
e2 = Entry(fr, textvariable= getnum, bg='#04e096', fg='white', width=24, font=('BouncyPERSONALUSEONLY'))
e2.grid(row = 1, column = 4, columnspan = 2)

l3 = Label(fr, text="Enter proper Name of Recipient", padx=20, pady=10, bg='#04e096', width=24, font=('BouncyPERSONALUSEONLY'), fg='#e6ffe6')
l3.grid(row = 2, column = 0, columnspan = 2)

getname = StringVar()
e3 = Entry(fr, textvariable= getname, bg='#04e096', fg='white', width=24, font=('BouncyPERSONALUSEONLY'))
e3.grid(row = 2, column = 4, columnspan = 2)

btn = Button(fr, text="Send", padx=10, pady=1, font='OldEnglishTextMT', bg='#e6ffe6', activebackground='#04e096', fg='black', underline=1, command=letsgo)
btn.grid(row = 3, column = 4)

root.mainloop()






