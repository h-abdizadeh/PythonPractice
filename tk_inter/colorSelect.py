from tkinter import *

def btnRedClick():
    app['bg']='red'

def btnGreenClick():
    app['bg']='green'

def btnBlueClick():
    app['bg']='blue'

def randomColor():
    chars='0 1 2 3 4 5 6 7 8 9 a b c d e f'.split(' ')
    print(chars)
    import random
    color='#'
    for ch in range(6):
        n=random.randrange(len(chars))
        color+=chars[n]
        print(n)
    app['bg']=color
        

app=Tk()
app.title('color select')
app.geometry('150x150')
app.resizable(FALSE,FALSE)

btnRed=Button(app,text='red',bg='red',command=btnRedClick)
btnRed.pack()

btnGreen=Button(app,text='green',bg='green',command=btnGreenClick)
btnGreen.pack()

btnBlue=Button(app,text='blue',bg='blue',command=btnBlueClick)
btnBlue.pack()

btnRandom=Button(app,text='random color',
                 command=randomColor)
btnRandom.pack()

app.mainloop()