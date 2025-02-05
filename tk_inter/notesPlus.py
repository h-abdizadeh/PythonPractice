from tkinter import *
from tkinter import messagebox
from datetime import datetime
file='data/notes.txt'

def submit():
    note=text1.get('1.0',END).strip()
    if len(note) is 0:
        messagebox.showwarning('message','empty note')
        return
    
    with open(file,'a') as _file:
        try:
            _file.write(note+'\n')
            _file.write(f'{datetime.now().date()}\n')
            messagebox.showinfo('message','success')
            text1.delete('1.0',END)
        except Exception as e:
            messagebox.showerror('message',e)

def showNotes():
    notesList.delete(0,END)
    with open(file) as _file:
        notes=_file.readlines()
        note=''
        for n in notes:
            note+=n #note=note+n
            if '-' in n:
                notesList.insert(END,note)
                note='' # new note

def getDates():
    tmpOption=[]
    with open(file) as _file:
        notes=_file.readlines()
        for n in list(set(notes)):
            if '-' in n:
                tmpOption.append(n)
    # print(tmpOption)
    return tmpOption

def dateNote(option):
    notesList.delete(0,END)
    print(option)
    with open(file) as _file:
        notes=_file.readlines()
        note=''
        counter=notes.count(option)
        for n in notes:
            note+=n
            if '-' in n:
                if n==option:
                    notesList.insert(END,note)
                    note='' # new note
                    counter-=1
                else:
                    note=''
            
            if n==option and counter==0:break

app=Tk()
app.title('notes')
app.geometry('300x450')
app.resizable(False,False)

text1=Text(app,height=8,font='tahoma 12')
text1.pack()

btnSubmit=Button(app,text='save',command=submit)
btnSubmit.place(x=10,y=160)

btnShow=Button(app,text='show notes',command=showNotes)
btnShow.place(x=50,y=160)

options=getDates()
print(options)

default=StringVar(app,'select date')
dateOption=OptionMenu(app,default,*options,command=dateNote)
dateOption.place(x=190,y=160)

notesList=Listbox(app,font='tahoma 12',width=33,height=12)
notesList.place(x=0,y=195)

# datetime def
# print(datetime.now())
# print(datetime.now().day)
# print(datetime.now().month)
# print(datetime.now().year)
# print(datetime.now().time())
# print(datetime.now().time().hour)
# time=str(datetime.now().time())
# print(time[0:time.index('.')])
# print(datetime.now().date())

app.mainloop()