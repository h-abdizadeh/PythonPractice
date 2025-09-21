from tkinter import *
import sqlite3
from tkinter import ttk

database='data/mydata.db'

def createDatabaseTable():
    con=sqlite3.connect(database)
    con.execute('''Create Table If Not Exists Students
                (Id Integer Primary Key,
                Fname Text,
                Lname Text Not Null,
                Mcode Text,
                Phone Text Not Null,
                Grade Text Not Null)''')
    con.commit()#save change


def insertData():
    data=('رضا','اسدی','260','0911','10')
    con=sqlite3.connect(database)
    con.execute(f'''Insert Into 
                Students(Fname,Lname,Mcode,Phone,Grade)
                values {data}''')
    con.commit()

def selectData():
    con=sqlite3.connect(database)
    # con.execute('Select Fname,Lname From Students')
    data=con.execute('Select * From Students')
    dataTree.delete(*dataTree.get_children())
    for i in data:
        dataTree.insert('',END,values=i)

def deleteData():
    id=2
    con=sqlite3.connect(database)
    con.execute(f'''Delete From Students Where Id={id}''')
    con.commit()
    selectData()

def searchData():
    search=entrySearch.get()
    con=sqlite3.connect(database)
    # con.execute(f'''Select * From Students 
    #             where Lname=\'{search}\' ''')
    result = con.execute(f'''Select * From Students 
                where Lname Like \'%{search}%\' ''')
    dataTree.delete(*dataTree.get_children())
    for i in result:
        dataTree.insert('',END,values=i)

def selectStudent():
    id=3
    con=sqlite3.connect(database)
    result=con.execute(f'Select * From Students Where id={id}').fetchone()
    entryFname.insert(0,result[1])
    entryLname.insert(0,result[2])
    entryPhone.insert(0,result[4])
    
def updateData():
    id=3
    data=(entryFname.get(),
          entryLname.get(),
          entryPhone.get())
    con=sqlite3.connect(database)
    con.execute(f'''Update Students Set
                Fname=\'{entryFname.get()}\',
                Lname=\'{data[1]}\',
                Phone=\'{data[2]}\'
                Where Id={id}''')
    con.commit()
    selectData()

app=Tk()

entryFname=Entry(app)
entryFname.pack()
entryLname=Entry(app)
entryLname.pack()
entryPhone=Entry(app)
entryPhone.pack()

btnInsert=Button(app,text='insert data',command=insertData)
btnInsert.pack()

btnUpdate=Button(app,text='update data',command=updateData)
btnUpdate.pack()

btnDelete=Button(app,text='delete data',command=deleteData)
btnDelete.pack()

btnSelect=Button(app,text='select data',command=selectData)
btnSelect.pack()

entrySearch=Entry(app)
entrySearch.pack()
btnSearch=Button(app,text='search data',command=searchData)
btnSearch.pack()

btnSelectId=Button(app,text='select student',command=selectStudent)
btnSelectId.pack()


dataTree=ttk.Treeview(app,columns=[0,1,2,3,4,5],show='headings')
dataTree.heading(0,text='ردیف')
dataTree.heading(1,text='نام')
dataTree.heading(2,text='نام خانوادگی')
dataTree.heading(3,text='کد ملی')
dataTree.heading(4,text='شماره تماس')
dataTree.heading(5,text='پایه')

dataTree.column(0,width=35)
dataTree.column(1,width=75)
dataTree.column(2,width=100)
dataTree.column(3,width=100)
dataTree.column(4,width=100)
dataTree.column(5,width=35)
dataTree.pack()

createDatabaseTable()
app.mainloop()