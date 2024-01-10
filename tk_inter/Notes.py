from tkinter import *
from datetime import datetime
from tkinter import messagebox
from persiantools import jdatetime

fileAddress='Data/notes.txt'

def SaveNote():
    if len(text1.get('1.0','end').strip())>0:
        dt=datetime.now()
        day=dt.strftime('%Y/%m/%d %H:%M:%S')#%D -> date
        m=dt.strftime('%m')
        match m:
            case '08':
                day=day.replace('/08/','/August/')
                
        #messagebox.showinfo('time',day)
        note=text1.get('1.0','end')
        # note+=day
        text1.insert('end','\n'+day+'\n')

        with open('Data/notes.txt','a') as obj:
            obj.write(text1.get('1.0','end'))
    else:
        messagebox.showinfo('notes','please write...')

def ClearNote():
    text1.delete('1.0','end')

def ShowNote():
    with open(fileAddress) as obj:
        filetext=obj.read()
        #messagebox.showinfo('notes.txt',filetext)
        text1.insert('end',filetext)

def EditNote():
    with open(fileAddress,'w') as obj:
            obj.write(text1.get('1.0','end'))

def LineNote():
    with open(fileAddress) as obj:
        for line in obj:
            if '12:46' in line:
                break
            text1.insert('end',line)

form=Tk()
form.title('notes')
form.geometry('360x320')
form.resizable()

text1=Text(form,font='None 14',height='10')
text1.pack()

btnSave=Button(form,text='Save',font='none 14',
               command=SaveNote)
btnSave.place(x=10,y=250)

btnShow=Button(form,text='Show',font='none 14',
               command=ShowNote)
btnShow.place(x=75,y=250)

btnClear=Button(form,text='Clear',font='none 14',
                command=ClearNote)
btnClear.place(x=140,y=250)

btnEdit=Button(form,text='Edit',font='none 14',
                command=EditNote)
btnEdit.place(x=205,y=250)

btnLine=Button(form,text='line',font='none 14',
                command=LineNote)
btnLine.place(x=260,y=250)


print(jdatetime.JalaliDateTime.now())

form.mainloop()