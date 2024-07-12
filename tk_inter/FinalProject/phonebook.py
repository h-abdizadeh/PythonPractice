from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

dbname='data/mydatabase.db'
accountId=0

def CreateTable():
    #connet to database (create dbname if not exists)
    con=sqlite3.connect(dbname)
    #craete table
    tableName='Accounts'
    con.execute(f'''CREATE TABLE IF NOT EXISTS {tableName}
                    (Id INTEGER PRIMARY KEY,
                    Fname TEXT NOT NULL,
                    Lname TEXT NOT NULL,
                    Phone TEXT NOT NULL)''')#Id -> auto number

def InsertAccount():
    con=sqlite3.connect(dbname)
    # accountData=('ali','ahmadi','0930')#tuple
    accountData=CreateRecord()
    #test
    #print(accountData)
    if accountData is None: return

    try:
        if saveBtn['text']=='ویرایش':
            # messagebox.showinfo(accountId)
            # messagebox.showinfo(accountId)
            #update/edit
            query=f'''UPDATE Accounts SET 
                      Fname='{accountData[0]}',
                      Lname='{accountData[1]}',
                      Phone='{accountData[2]}' WHERE Id={int(entrySearch.get())}'''
            con.execute(query)
            con.commit()
            ShowAccounts('')#show accounts after insert

            saveBtn['text']='ثبت مخاطب'
            entryFname.delete(0,END)
            entryLname.delete(0,END)
            entryPhone.delete(0,END)
            return

        #insert
        con.execute('''INSERT INTO Accounts(Fname,Lname,Phone)
                    VALUES (?,?,?)''',accountData)
    
        con.commit()
        messagebox.showinfo('پیام','ثبت موفق')
        ShowAccounts('')#show accounts after insert
    except Exception as error:
        messagebox.showerror('خطا',f'خطای ثبت {error}')

def CreateRecord():
    fname=entryFname.get().strip()
    lname=entryLname.get().strip()
    phone=entryPhone.get().strip()

    if len(fname)>0 and len(lname)>0 and len(phone)>0:
        record=(fname,lname,phone)
        return record
    else:
        messagebox.showwarning('هشدار','فیلدهای خالی')        

def ShowAccounts(search):
    query='SELECT * FROM Accounts' #select all accounts

    input=str(search).strip()
    if len(input)>0:
        # query=f'SELECT * FROM Accounts WHERE Lname={input}'
        query=f'SELECT * FROM Accounts WHERE Lname LIKE  \'%{input}%\''

    con=sqlite3.Connection(dbname)
    accountList=con.execute(query)
    
    accountsTree.delete(*accountsTree.get_children())
    for item in accountList:
        # print(item)
        accountsTree.insert('',index=END,values=item)
    
    accountList.close()

def DeleteAccount():
    try:
        id=int(entrySearch.get())
        query=f'DELETE FROM Accounts WHERE Id={id}'

        con=sqlite3.Connection(dbname)
        con.execute(query)
        con.commit()

        ShowAccounts('')#show accounts after delete
        entrySearch.delete(0,END)
    except Exception as error:
        messagebox.showerror('خطا',f'برای حذف شماره ردیف را وارد کنید\n{error}')

def SelectRecord():
    try:
        id=int(entrySearch.get())
        #select
        query=f'SELECT * FROM Accounts WHERE Id={id}'
        con=sqlite3.Connection(dbname)
        account= list(con.execute(query))
        #print(account)
        if len(account)>0:
            accountId=account[0][0]
            entryFname.insert(0,account[0][1])
            entryLname.insert(0,account[0][2])
            entryPhone.insert(0,account[0][3])
            saveBtn['text']='ویرایش'


    except Exception as error:
        messagebox.showerror('خطا',f'برای انتخاب شماره ردیف را وارد کنید\n{error}')

app = Tk()
app.title('account book')
app.geometry('500x400')
app.resizable(FALSE,FALSE)

#1 submit form - فرم ثبت مخاطب
submitTitle=Label(app,
                  bg='#2d5f8d',
                  fg='white',
                  text='ثبت / ویرایش مخاطب',
                  width=22,
                  height=2,
                  font='tahoma 12',
                  anchor=CENTER)
submitTitle.place(x=294,y=0)

labelFname=Label(app,
                 text='نام',
                 font='tahoma 12')
labelFname.place(x=470,y=55)

entryFname=Entry(app,
                 font='tahoma 12',
                 width=14)
entryFname.place(x=295,y=55)

labelLname=Label(app,
                 text='خانوادگی',
                 font='tahoma 12')
labelLname.place(x=430,y=90)

entryLname=Entry(app,
                 font='tahoma 12',
                 width=14)
entryLname.place(x=295,y=90)

labelPhone=Label(app,
                 text='تلفن',
                 font='tahoma 12')
labelPhone.place(x=460,y=125)

entryPhone=Entry(app,
                 font='tahoma 12',
                 width=14)
entryPhone.place(x=295,y=125)

saveBtn=Button(app,
               text='ثبت مخاطب',
               font='tahoma 12 bold',
               width=12,
               command=InsertAccount)
saveBtn.place(x=295,y=160)

#2 search box - کادر جستجو
searchTitle=Label(app,
                  text='جستجو / انتخاب / حذف',
                  bg='#2d5f8d',
                  fg='white',
                  width=31,
                  height=10,
                  font='tahoma 12',
                  anchor=N)
searchTitle.place(x=2,y=0)

entrySearch=Entry(app,
                  font='tahoma 12',
                  width=24)
entrySearch.place(x=30,y=30)
btnSearch=Button(app,
                 font='tahoma 12 bold',
                 text='بگرد',
                 command=lambda:ShowAccounts(entrySearch.get()))
btnSearch.place(x=30,y=60)

btnSelect=Button(app,
                 text='انتخاب',
                 font='tahoma 12 bold',
                 width=21,
                 bg='orange',
                 command=SelectRecord)
btnSelect.place(x=30,y=100)

btnDelete=Button(app,
                 text='حذف',
                 font='tahoma 12 bold',
                 width=21,
                 bg='red',
                 fg='white',
                 command=DeleteAccount)
btnDelete.place(x=30,y=140)

#tree
accountsTree=ttk.Treeview(app,
                          columns=('c1','c2','c3','c4'),
                          show='headings',
                          height=8)

accountsTree.heading('c1',text='ردیف')
accountsTree.heading('c2',text='نام')
accountsTree.heading('c3',text='نام خانوادگی')
accountsTree.heading('c4',text='تلفن')

accountsTree.column('c1',width=45)
accountsTree.column('c2',width=120)
accountsTree.column('c3',width=160)
accountsTree.column('c4',width=170)

accountsTree.place(x=2,y=200)


CreateTable()
# InsertAccount()#test insert
ShowAccounts('')

app.mainloop()