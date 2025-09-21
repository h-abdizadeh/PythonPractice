from tkinter import *

def Line():
    #(x1, y1, x2, y2)
    myCanvas.create_line(50,100,120,100,fill='red',width=5)
    myCanvas.create_line(120,100,120,200,fill='blue',width=5)
def rect():
    myCanvas.create_rectangle(50,50,150,150,fill='green',width=10,outline='pink')

def circle():
    myCanvas.create_oval(0,0,100,100)

def arc():
    myCanvas.create_arc(200,200,300,300)

def txt():
    myCanvas.create_text(100,100,text='hello',fill='red',
                         font='impact 50')

def star():
        myCanvas.create_line(100,100,120,180)
        myCanvas.create_line(120,180,200,200)
        myCanvas.create_line(200,200,120,220)
        myCanvas.create_line(120,220,200,280)
        myCanvas.create_line(100,100,80,180)


def delete():
    myCanvas.delete(ALL)

app=Tk()

myCanvas=Canvas(app,width=400,height=400,bg='white')
myCanvas.pack()

btnLine=Button(app,text='Line',command=Line)
btnLine.place(x=0,y=0)
btnRect=Button(app,text='rect',command=rect)
btnRect.place(x=50,y=0)


star()
app.mainloop()

