from tkinter import *
from tkinter.ttk import Combobox
import random

root = Tk()
root.title("Random Password Generator")
root.geometry("650x400")

def pwd():
    sc.set("")
    l = int(entry_3.get())
    passwd = ""
    lwcase = "abcdefghijklmnopqrstuvwxyz"
    upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "123456789"
    spec = "@#$%&!"
    mix = lwcase + upcase + num + spec*3

    if (ch.get() == "Low"):
        for i in range(0,l):
            passwd += random.choice(lwcase+num)
        sc.set(passwd)
    
    elif(ch.get()=="Medium"):
        for i in range(0,l):
            passwd += random.choice(lwcase+upcase+num)
        sc.set(passwd)
    elif (ch.get() == "Strong"):
        for i in range(0,l):
            passwd += random.choice(mix)
        sc.set(passwd)
sc = StringVar()
click = StringVar()
label_1 = Label(root,text="Random Password Generator",fg = 'blue', font=("Verdana",22))
label_2 = Label(root,text="Password",font=("Arial",14))
entry_2 = Entry(root,textvariable=sc)
label_3 = Label(root,text="Length",font=('Arial',14))
label_4 = Label(root,text="Strength: ",font=('Arial',14))
entry_3 = Entry(root)
click.set('Strength')
ch = Combobox(root,textvariable=click,width='20')
ch['values'] = ['Low','Medium','Strong']
btn = Button(root,text='Generate',fg='red',command=pwd,width='15')

label_1.grid(row=0,column=3)
label_2.grid(row=2,column=2)
entry_2.grid(row=2,column=3)
label_3.grid(row=4,column=2)
entry_3.grid(row=4,column=3)
ch.grid(row=6,column=3)
btn.grid(row=7,column=2)
