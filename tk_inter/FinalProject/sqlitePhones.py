from tkinter import *
import sqlite3
from tkinter import ttk

database='data/mydata.db'

def createTable():
    #table name : phones
    con=sqlite3.connect(database)
    con.execute('''Create Table If Not Exists Phones
                (id integer primary key,
                name text,
                lastname text not null,
                phone text not null)''')

def insertData():
    # data=('amir','ahmadi','0911')
    data=(entry1.get(),
          entry2.get(),
          entry3.get())
    
    con=sqlite3.connect(database)
    con.execute(f'''insert Into Phones(name,lastname,phone)
                values {data}''')
    con.commit()#save
    selectData()

def selectData():
    con=sqlite3.connect(database)
    result=con.execute('Select * From Phones')
    tree.delete(*tree.get_children())
    for n in result:
        # print(n)
        tree.insert('',END,values=n)

def searchData(search:str):
    if search.isdigit():
        id=int(search)
        con=sqlite3.connect(database)
        result=con.execute(f'Select * From Phones Where id={id}').fetchone()

        entry1.insert(0,result[1])
        entry2.insert(0,result[2])
        entry3.insert(0,result[3])
        return
    # search=entrySearch.get()
    con=sqlite3.connect(database)
    # result=con.execute(f'Select * From Phones Where lastname=\'{search}\'')
    result=con.execute(f'Select * From Phones Where lastname Like \'%{search}%\'')
    tree.delete(*tree.get_children())
    for n in result:
        tree.insert('',END,values=n)

def deleteData():
    id=int(entrySearch.get())
    con=sqlite3.connect(database)
    con.execute(f'Delete From Phones Where id={id}')
    con.commit()
    selectData()

def updateData():
    id=entrySearch.get()
    if id.isdigit():
        id=int(id)
        con=sqlite3.connect(database)
        con.execute(f'''Update Phones Set 
                    name=\'{entry1.get()}\',
                    lastname=\'{entry2.get()}\',
                    phone=\'{entry3.get()}\'
                    Where id={id}''')
        con.commit()
        selectData()

app=Tk()
btnCreate=Button(app,text='create database, phones table')
btnCreate.pack()
btnCreate['command']=createTable

entry1=Entry(app)
entry1.pack()
entry2=Entry(app)
entry2.pack()
entry3=Entry(app)
entry3.pack()

btnInsert=Button(app,text='insert data')
btnInsert.pack()
btnInsert['command']=insertData

btnUpdate=Button(app,text='update data')
btnUpdate.pack()
btnUpdate['command']=updateData

btnSelectAll=Button(app,text='select data')
btnSelectAll.pack()
btnSelectAll['command']=selectData

entrySearch=Entry(app)
entrySearch.pack()

btnSearch=Button(app,text='search')
btnSearch.pack()
btnSearch['command']=lambda:searchData(entrySearch.get())

btnDelete=Button(app,text='delete')
btnDelete.pack()
btnDelete['command']=deleteData

btnImportData=Button(app,text='import data')
btnImportData.pack()
btnImportData['command']=lambda:searchData(entrySearch.get())

tree=ttk.Treeview(app,columns=[0,1,2,3],show='headings')
tree.heading(0,text='id')
tree.heading(1,text='name')
tree.heading(2,text='last name')
tree.heading(3,text='phone')
tree.column(0,width=30)
tree.column(1,width=60)
tree.column(2,width=75)
tree.column(3,width=100)
tree.pack()

app.mainloop()