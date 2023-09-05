from tkinter import *

def KeyPad(key):
    txt=label1['text']
    if txt=='0':
        txt=key
    else:
        txt+=key
    label1['text']=txt

def BackSpace():
    #1
    # tmp=list(label1['text'])
    # #print(tmp)
    # tmp.pop()
    # #print(tmp)
    # label1['text']=''
    # for n in tmp:
    #     label1['text']+=n

    #2
    tmp=label1['text']
    # print(tmp[0:len(tmp)-1])   
    if len(tmp)>1:
        label1['text']=tmp[0:len(tmp)-1]
    else:
        label1['text']='0'


form=Tk()
form.title('NumPad')
form.geometry('280x360')
form.resizable(False,False)

label1=Label(form,font='none 25',text='0',
             anchor='w',bg='white',width=14)
label1.pack()

btn1=Button(form,font='none 18',text='1',width=5,height=2,
            command=lambda:KeyPad('1'))
btn1.place(x=10,y=80)

btn2=Button(form,font='none 18',text='2',width=5,height=2,
            command=lambda:KeyPad('2'))
btn2.place(x=100,y=80)

btn3=Button(form,font='none 18',text='3',width=5,height=2,
            command=lambda:KeyPad('3'))
btn3.place(x=190,y=80)

btn0=Button(form,font='none 18',text='0',width=5,height=2,
            command=lambda:KeyPad('0'))
btn0.place(x=10,y=280)

btnBck=Button(form,font='none 18',text='BackSpace',width=11,height=2,
            command=BackSpace)
btnBck.place(x=100,y=280)


form.mainloop()