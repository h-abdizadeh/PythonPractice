from tkinter import *
from tkinter import messagebox

fileAddress='data/students.txt'

def SubmitName():
    name = entryName.get()
    if len(name.strip()) is 0:
        messagebox.showinfo('alert','please enter name')
    else:
        #save name to file (\n line)
        with open(fileAddress,'a') as file:
            file.write(f'{name}\n')
            entryName.delete(0,END)

def ShowNames():
    list1.delete(0,END)#clear listbox
    with open(fileAddress) as file:#'r -> read file'
        names=file.readlines()
        for n in names:
            list1.insert(END,n)
            #list1.insert(0,n)

def SelectStudent():
    from random import randrange
    with open(fileAddress) as file:
        names=file.readlines()
        index=randrange(len(names))
        # list1.insert(0,names[index])
        messagebox.showinfo('student',names[index])


app=Tk()
app.title('students list')
app.geometry('400x300')
app.resizable(FALSE,FALSE)

entryName=Entry(app,
                font='none 16',
                width=15)
entryName.place(x=10,y=10)

btnSubmit=Button(app,
                 font='none 12',
                 text='submit',
                 command=SubmitName)
btnSubmit.place(x=200,y=8)

btnShow=Button(app,
               text='show',
               font='none 12',
               command=ShowNames)
btnShow.place(x=270,y=8)

list1=Listbox(app,
              font='none 12',
              width=20,
              height=10)
list1.place(x=10,y=60)

btnSelect=Button(app,
                 font='none 32',
                 text='?',
                 command=SelectStudent)
btnSelect.place(x=250,y=150)

app.mainloop()
