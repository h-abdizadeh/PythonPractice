from tkinter import *

app=Tk()
#code(design)
#app window (form)
app.geometry('520x480')
app.title('برنامه من')
# app['bg']='red'
app['bg']='#21ea91'#1f7071
# app.resizable(False,True)#fixed Width
# app.resizable(True,False)#fixed Height
app.resizable(False,False)

#tools
label1=Label(app)
label1['text']='my label'
# label1.pack()
# label1.pack(anchor=W)#E
label1.place(x=15,y=10)
label1['font']='none 21'#'font-name font-size'
label1['bg']='#d2f035'
label1['fg']='#1D24CA'
label1['width']=15
label1['height']=3
label1['anchor']=W#E,S,NE,SW,...

app.mainloop()