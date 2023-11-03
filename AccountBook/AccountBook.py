from tkinter import *
from tkinter import ttk
import sqlite3

db="Data/MyData.db"
def CreateTable():
    con=sqlite3.Connection(db)
    con.execute('''CREATE TABLE IF NOT EXISTS Accounts
                (Id INTEGER PRIMARY KEY,
                 Fname TEXT,
                 Lname TEXT NOT NULL,
                 Phone TEXT NOT NULL)''')

def AddAccount():
    account=(entryFname.get(),
             entryLname.get(),
             entryPhone.get())
    
    if btnAddEdit['text']=='ویرایش':
        EditAccount(account)
        btnAddEdit['text']='ثبت مخاطب   '
    else:
        con=sqlite3.Connection(db)
        con.execute('''INSERT INTO Accounts(Fname,Lname,Phone)
                    VALUES (?,?,?)''',account)
        
        con.commit()

def EditAccount(account):
    id=(int(entrySearch.get()),)
    account=account+id
    command='''UPDATE Accounts SET Fname=?,Lname=?,Phone=? 
                WHERE Id=?'''
    
    con=sqlite3.Connection(command,account)
    con.commit()


def ShowAccounts():
    accountTree.delete(*accountTree.get_children())
    con=sqlite3.Connection(db)
    accounts=con.execute("SELECT * FROM Accounts")

    for account in accounts:
        accountTree.insert('',END,values=account)

def DeleteAccount():
    id=int(entrySearch.get())
    con=sqlite3.Connection(db)
    accountId=(id,)
    con.execute("DELETE FROM Accounts WHERE Id=?",accountId)
    con.commit()
    ShowAccounts()

def Search(inputStr):
    srch=('%'+inputStr+'%',)
    command='SELECT * FROM Accounts WHERE Lname LIKE ?'
    con=sqlite3.Connection(db)
    accounts=con.execute(command,srch)

    accountTree.delete(*accountTree.get_children())
    for account in accounts:
        accountTree.insert('',END,values=account)

def GetAccount():
    id=int(entrySearch.get())
    accountId=(id,)
    command='SELECT * FROM Accounts WHERE Id=?'
    con=sqlite3.Connection(db)
    account=con.execute(command,accountId)

    for a in account:
        entryFname.insert(INSERT,a[1])
        entryLname.insert(INSERT,a[2])
        entryPhone.insert(INSERT,a[3])   

        btnAddEdit['text']='ویرایش'





app=Tk()
app.title('Account Book')
app.geometry('640x400')
app.resizable(False,False)
#app['bg']='black'

#add or edit account
Label1=Label(app,
             font='Tahoma 16',
             text='ثبت / ویرایش مخاطب',
             bg='#245edb',
             fg='white',
             width=25,
             height=2).pack(anchor=E)

LabelFname=Label(app,
                 font='Tahoma 12',
                 text='نام',
                 justify=RIGHT).pack(anchor=E)
entryFname=Entry(app,
                 font='Tahoma 14',
                 width=30,
                 justify=CENTER)
entryFname.pack(anchor=E)

LabelLname=Label(app,
                 font='Tahoma 12',
                 text='نام خانوادگی',
                 justify=RIGHT).pack(anchor=E)
entryLname=Entry(app,
                 font='Tahoma 14',
                 width=30,
                 justify=CENTER)
entryLname.pack(anchor=E)

LabelPhone=Label(app,
                 font='Tahoma 12',
                 text='شماره تماس',
                 justify=RIGHT).pack(anchor=E)
entryPhone=Entry(app,
                 font='Tahoma 14',
                 width=30,                 justify=CENTER)
entryPhone.pack(anchor=E)

btnAddEdit=Button(app,
                  font='Tahoma 11',
                  text='ثبت مخاطب',
                  bg='#245edb',
                  fg='white',
                  border=1,
                  command=AddAccount)
btnAddEdit.place(x=340,y=240)

btnSearch=Button(app,
                 font='Tahoma 10',
                 text='جستجو',
                 bg='white',
                 fg='#245edb',
                 border=1,
                 command=lambda:Search(entrySearch.get()))
btnSearch.place(x=5,y=12)


btnSelect=Button(app,
                 font='Tahoma 10',
                 text='انتخاب',
                 bg='white',
                 fg='#245edb',
                 border=1,
                 command=GetAccount)
btnSelect.place(x=60,y=12)

entrySearch=Entry(app,
                  font='Tahoma 14',
                  width=14,
                  justify=RIGHT)
entrySearch.place(x=112,y=12)
btnDelete=Button(app,
                 text='حذف',
                 bg='red',
                 fg='white',
                 border=1,
                 command=DeleteAccount)
btnDelete.place(x=260,y=12)
accountTree=ttk.Treeview(app,
                         columns=('c1','c2','c3','c4'),
                         show='headings')
accountTree.column('#1',anchor=CENTER,width=10)
accountTree.heading('#1',text='id')
accountTree.column('#2',anchor=CENTER,width=80)
accountTree.heading('#2',text='name')
accountTree.column('#3',anchor=CENTER,width=100)
accountTree.heading('#3',text='family')
accountTree.column('#4',anchor=CENTER,width=100)
accountTree.heading('#4',text='phone')


accountTree.place(x=5,y=45)

btnAll=Button(app,
              text='نمایش همه',
              bg='#245edb',
              fg='white',
              command=ShowAccounts)
btnAll.place(x=5,y=360)

CreateTable()

app.mainloop()