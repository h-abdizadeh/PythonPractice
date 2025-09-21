from tkinter import *
def action(number):
    if number==1:
        if btn1['text']=='': 
            btn1['text']=label1['text']
        else:
            return
    elif number==2:
         btn2['text']=label1['text']
    elif number==3:
        btn3['text']=label1['text']
    elif number==4:
        btn4['text']=label1['text']
    elif number==5:
        btn5['text']=label1['text']
    elif number==6:
        btn7['text']=label1['text']
    elif number==8:
        btn8['text']=label1['text']
    elif number==9:
        btn9['text']=label1['text']

    if label1['text']=='X':
        label1['text']='O'
    else:
        label1['text']='X'

    checkWin()
    
def checkWin():
    if btn1['text']==btn2['text']==btn3['text']!='':
        label1['text']=btn1['text']+'win'
    
app=Tk()
app.geometry('315x350')
label1=Label(app,text='X',font='impact 32')
label1.pack()

btn1=Button(app,font='none 24',width=5,height=2,
            command=lambda:action(1))
btn1.place(x=0,y=50)

btn2=Button(app,font='none 24',width=5,height=2)
btn2['command']=lambda:action(2)
btn2.place(x=105,y=50)

btn3=Button(app,font='none 24',width=5,height=2)
btn3['command']=lambda:action(3)
btn3.place(x=210,y=50)

btn4=Button(app,font='none 24',width=5,height=2)
btn4['command']=lambda:action(4)
btn4.place(x=0,y=150)

btn5=Button(app,font='none 24',width=5,height=2,command=action)
btn5.place(x=105,y=150)
btn6=Button(app,font='none 24',width=5,height=2,command=action)
btn6.place(x=210,y=150)
btn7=Button(app,font='none 24',width=5,height=2,command=action)
btn7.place(x=0,y=250)
btn8=Button(app,font='none 24',width=5,height=2,command=action)
btn8.place(x=105,y=250)
btn9=Button(app,font='none 24',width=5,height=2,command=action)
btn9.place(x=210,y=250)

app.mainloop()