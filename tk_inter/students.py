from tkinter import *
from tkinter import messagebox
myFile='data/studentsFile.txt'
def AddName():
    name=entry1.get().strip()
    if len(name) is 0:#==
        messagebox.showwarning('','write name')
        return
    with open(myFile,'a') as file:
        file.write(f'{name}\n')
        messagebox.showinfo('','success')
        entry1.delete(0,END)

def ShowName():
    listBox1.delete(0,END)
    with open(myFile) as file:
        fileData=file.readlines()
        # 1
        # listBox1.insert(0,*fileData)
        # 2
        for n in fileData:
            # listBox1.insert(0,n)
            listBox1.insert(END,n)

def Select():
    with open(myFile) as file:
        names=file.readlines()
        from random import choice
        btnSelect['text']=choice(names)

app=Tk()
app.title('students')
app.geometry('400x400')
app.resizable(FALSE,FALSE)

entry1=Entry(app,width=15,font='none 14',justify=CENTER)
entry1.place(x=200,y=20)

btnAdd=Button(app,text='add',
              font='none 12 bold',
              width=5,command=AddName)
btnAdd.place(x=120,y=15)

listBox1=Listbox(app,width=10,font='none 14')
listBox1.place(x=10,y=75)

btnShow=Button(app,text='show names',
               font='none 12 bold',
               command=ShowName)
btnShow.place(x=10,y=15)

btnSelect=Button(app,text='?',
                 font='none 24',
                 command=Select)
btnSelect.place(x=220,y=200)

app.mainloop()