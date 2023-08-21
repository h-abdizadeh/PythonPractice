from tkinter import*

def sum():
    n=int(entry1.get())
    m=int(entry2.get())
    label1['text']=n+m

def div():
    n=int(entry1.get())
    m=int(entry2.get())
    if m==0:
        label1['text']='Cannot divide'
    else:
        label1['text']=n/m

app=Tk()
app.title('miniCalculator')
app.geometry('420x240')
app.resizable(False,False)
app['bg']='#4445f7'
#entry
#1
entry1=Entry(app,font='none 25',width='10')
entry1.insert(INSERT,'0')
entry1.place(x=10,y=10)
#2
entry2=Entry(app,font='none 25',width='10')
entry2.insert(INSERT,'0')
entry2.place(x=220,y=10)
#label
label1=Label(app,font='none 36',bg='#4445f7',fg='yellow',text='0')
label1.place(x=10,y=70)
#button
btn1=Button(app,width='3',font='none 28',text='+',command=sum)
btn1.place(x=20,y=150)
btn2=Button(app,width='3',font='none 28',text='-')
btn2.place(x=120,y=150)
btn3=Button(app,width='3',font='none 28',text='*')
btn3.place(x=220,y=150)
btn3=Button(app,width='3',font='none 28',text='/',command=div)
btn3.place(x=320,y=150)
app.mainloop()
