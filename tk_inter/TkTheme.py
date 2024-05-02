from tkinter import *

def SetTheme(theme):
    #1
    # color=default.get()
    # app['bg']=color
    # print(theme)
    #2
    app['bg']=theme

app=Tk()
app.title('theme')
app.geometry('400x300')
app.resizable(False,False)
app['bg']='teal'

options=['teal','red','yellow','green']
default=StringVar(app,'select theme')
# default.set(options[0])
optionMenu=OptionMenu(app,
                      default,
                      *options,
                      command=SetTheme)
optionMenu.pack()
app.mainloop()