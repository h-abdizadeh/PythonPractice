from tkinter import*

def Counter():
    n=int(label1['text'])
    n+=1
    label1['text']=n

def Reset():
    label1['text']=0


form=Tk()
form.title('گام شمار')
form.geometry('250x360')
form.resizable(False,False)
form['bg']='#d0ae95'

label1=Label(form,
             fg='#ffffff',
             bg='#000000',
             text='0',
             font='none 62',
             width='5')
label1.place(x=0,y=32)

btn1=Button(form,
            text='Click',
            font='none 32',
            command=Counter)
btn1.place(x=58,y=180)
btn2=Button(form,
            text='reset',
            font='none 26',
            command=Reset)
btn2.place(x=72,y=280)
form.mainloop()