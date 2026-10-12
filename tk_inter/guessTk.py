from tkinter import *

def randomTarget():
    from random import randint
    target.set(randint(1,100))
    # print(target.get())

def game():
    guess=int(e1.get())

    from tkinter import messagebox
    if guess<target.get(): messagebox.showinfo('','بالاتر')
    elif guess>target.get(): messagebox.showinfo('','پایین تر')
    else : messagebox.showinfo('','برنده')

app=Tk()
target=IntVar(app,0)

e1=Entry(app)
e1.pack()

b1=Button(app,text='guess')
b1.pack()

randomTarget()
app.mainloop()