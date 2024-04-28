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

app.mainloop()