from tkinter import *

def DrawCircle():
    x=200
    y=200
    r=int(radiusEntry.get())
    canvas.delete(ALL)
    canvas.create_oval(x-r,
                       y-r,
                       x+r,
                       y+r,
                       outline='yellow',
                       fill='blue',
                       width=int(r/10))
    canvas.create_text(x,y,
                       text='hello',
                       fill='white',
                       font=f'none {int(r/2)}')

app=Tk()

radiusLabel=Label(app,text='enter radius : ')
radiusLabel.grid(row=0,column=0)

radiusEntry=Entry(app)
radiusEntry.grid(row=1,column=0)

canvas=Canvas(app,width=400,
              height=400,
              bg='#000000')

canvas.grid(row=2,column=0)

radiusBtn=Button(app,text='draw',
                 command=DrawCircle)
radiusBtn.grid(row=3,column=0)

app.mainloop()