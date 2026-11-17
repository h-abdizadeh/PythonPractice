from tkinter import *
from tkinter import messagebox
import json

myfile='data/file.json'

def saveJson():
    jsondata=json.dumps(data)
    with open(myfile,'w') as file:
        json.dump(jsondata,file)

app=Tk()
b1=Button(app,text='save json',command=saveJson)
b1.pack()

b2=Button(app,text='show json')
b2.pack()

data=[{'name':'amir','age':16},
      {'name':'ava','age':75},
      {'name':'reza','age':14}]

app.mainloop()