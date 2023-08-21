from tkinter import*
#1
def Counter():
    n=int(label1['text'])
    end=int(entry1.get())
    if n<end:
        n+=1
        label1['text']=n

def Reset():
    label1['text']=0

#2
#def Counter(n):
# no need in #2

form=Tk()
form.title('StepCounter')
form.geometry('280x380')
form.resizable(False,False)
form['bg']='#d3b56c'
label1=Label(form,
             bg='black',
             fg='white',
             text='0',
             font='none 70',
             width='5')
label1.place(x=0,y=20)

btnSet=Button(form,
              text='Click',
              font='none 28')
btnSet.place(x=84,y=220)
#1
btnSet['command']=Counter
#2
#btnSet['command']=lambda:Counter(int(label1['text']))

btnReset=Button(form,
              text='reset',
              font='none 21',
              command=Reset)
btnReset.place(x=98,y=300)

entry1=Entry(form,
             font='none 28',
             width='5',
             justify='center')
entry1.place(x=84,y=150)
entry1.insert(INSERT,'50')

form.mainloop()
