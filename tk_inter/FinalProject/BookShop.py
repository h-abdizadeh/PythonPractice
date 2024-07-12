from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

database='data/bookshop.db'
booksTable='Books'
groupsTable='Groups'


def CreateTableGroup():
    con=sqlite3.Connection(database)
    con.execute(f'''CREATE TABLE IF NOT EXISTS {groupsTable} 
                    (Id INTEGER PRIMARY KEY,
                    Title TEXT NOT NULL)''')
    con.commit()
    con.close()

def AddGroup():
    try:
        groupName=entryGroup.get().strip()
        if len(groupName)>0:
            #add group
            command=f'INSERT INTO {groupsTable}(Title) VALUES (\'{groupName}\')'
            con=sqlite3.Connection(database)
            con.execute(command)
            con.commit()#save changes
            messagebox.showinfo('پیام','ثبت موفق')
            entryGroup.delete(0,END)
        else:
            messagebox.showwarning('اخطار','نام گروه را وارد کنید')
    except Exception as error:
        messagebox.showerror('خطا',f'ثبت ناموفق\n{error}')

def GetGroups():
    result=[]

    try:
        con=sqlite3.Connection(database)
        groups=con.execute(f'SELECT Title FROM {groupsTable}')
        for g in groups:
            # print(g[0])
            result.insert(0,g[0])
    except:
        pass
    return result


def CreateTableBook():
    con=sqlite3.Connection(database)
    con.execute(f'''CREATE TABLE IF NOT EXISTS {booksTable} 
                (Id INTEGER PRIMARY KEY,
                Bname TEXT NOT NULL,
                Bwriter TEXT NOT NULL,
                Publisher TEXT NOT NULL,
                GroupName Text NOT NULL)''')

def AddEditBook():
    bookTuple=CheckInput()
    # print(bookTuple)
    if bookTuple is NONE:
        messagebox.showwarning('هشدار','فیلدهای خالی')
        return
    if(btnSubmit['text']=='ویرایش'):
        #editBook
        # print(bookId.get())
        query=f'''UPDATE {booksTable} SET 
                    Bname='{bookTuple[0]}',
                    Bwriter='{bookTuple[1]}',
                    publisher='{bookTuple[2]}',
                    GroupName='{bookTuple[3]}' WHERE Id={bookId.get()}'''
        con=sqlite3.Connection(database)
        con.execute(query)
        con.commit()

        messagebox.showinfo('پیام','ویرایش موفق')
        btnSubmit['text']='ثبت کتاب'      
    else:
        #addBook
        query=f'''INSERT INTO {booksTable}(Bname,Bwriter,Publisher,GroupName) 
                values (?,?,?,?)'''
        con=sqlite3.Connection(database)
        con.execute(query,bookTuple)
        con.commit() #save change
        messagebox.showinfo('پیام','ثبت موفق')
    ShowBooks('')

def CheckInput():
    bName=entryName.get().strip()
    writer=entryWriter.get().strip()
    publisher=entryPublisher.get().strip()
    group=default.get()
    # print(group)


    if len(bName)>0 and len(writer) and len(publisher)>0 and len(group):
        return (bName,writer,publisher,group)
    else:
        return NONE

def ShowBooks(search):
    query=f'SELECT * FROM {booksTable}'
    if len(search)>0:
        query=f'SELECT * FROM {booksTable} WHERE bname LIKE \'%{search}%\''
    
    con=sqlite3.Connection(database)
    result=con.execute(query)

    bookTree.delete(*bookTree.get_children())
    for book in result:
        bookTree.insert('',index=0,values=book)
    
    result.close()

def DeleteBook():
    id=entrySearch.get().strip()
    if id.isdigit():
        query=f'DELETE FROM {booksTable} WHERE id={int(id)}'
        con=sqlite3.Connection(database)
        con.execute(query)
        con.commit()
        ShowBooks('')

def SelectBook():
    id=entrySearch.get()
    if not id.isdigit(): return

    query=f'SELECT * FROM {booksTable} WHERE Id={int(id)}'
    con=sqlite3.Connection(database)
    book=con.execute(query).fetchall()
    # print(book[0])
    bookId.set(book[0][0])
    entryName.insert(0,book[0][1])
    entryWriter.insert(0,book[0][2])
    entryPublisher.insert(0,book[0][3])

    btnSubmit['text']='ویرایش'


app=Tk()
app.title('مدیریت کتابخانه')
app.geometry('640x480')
app.resizable(FALSE,FALSE)
bookId=IntVar(app,0)
#books add/edit form
title1=Label(app,text='ثبت/ویرایش کتاب',
             bg='#46adc7',fg='white',font='tahoma 11 bold',
             width=25,height=16,anchor=N)
title1.place(x=408,y=0)

#name
labelName=Label(app,text='نام کتاب',
                font='tahoma 11',
                bg='#46adc7').place(x=580,y=45)
entryName=Entry(app,font='tahoma 11 bold',width=22)
entryName.place(x=410,y=75)

#writer
labelWriter=Label(app,text='نویسنده',
                  font='tahoma 11',
                  bg='#46adc7').place(x=580,y=100)
entryWriter=Entry(app,font='tahoma 11 bold',width=22)
entryWriter.place(x=410,y=125)

#publisher
labelPublisher=Label(app,text='انتشارات',
                     font='tahoma 11',
                     bg='#46adc7').place(x=580,y=150)
entryPublisher=Entry(app,font='tahoma 11 bold',width=22)
entryPublisher.place(x=410,y=175)

#group
labelGroup=Label(app,text='گروه',
                 font='tahoma 11',
                 bg='#46adc7').place(x=605,y=200)
groupsList=['عمومی']
groupsList=groupsList+GetGroups()
default=StringVar(app,'انتخاب گروه')
groupMenu=OptionMenu(app,
                     default,
                     *groupsList)
groupMenu.place(x=480,y=200)

#add/edit book button
btnSubmit=Button(app,
                 text='ثبت کتاب',
                 font='tahoma 11 bold',
                 bg='#46adc7',
                 fg='white',
                 width=23,
                 command=AddEditBook)
btnSubmit.place(x=415,y=240)

#add group form
title2=Label(app,text='ثبت گروه',
             bg='#46cda7',
             fg='white',
             font='tahoma 11 bold',
             width=25,
             height=10,
             anchor=N)
title2.place(x=408,y=295)
#group name
labelGroup=Label(app,text='نام گروه',
                 font='tahoma 11',
                 bg='#46cda7').place(x=580,y=325)
entryGroup=Entry(app,font='tahoma 11 bold',width=22)
entryGroup.place(x=410,y=350)
#add group button
btnGroup=Button(app,
                 text='ثبت گروه',
                 font='tahoma 11 bold',bg='#46cda7',fg='white',
                 width=23,
                 command=lambda:AddGroup())
btnGroup.place(x=415,y=380)

#search box
# labelSearch=Label(app,text='جستجو').place(x=320,y=0)
entrySearch=Entry(app,width=20,font='tahoma 12')
entrySearch.place(x=125,y=0)
btnSearch=Button(app,text='جستجو',bg='#583278',fg='white',
                 command=lambda:ShowBooks(entrySearch.get()))
btnSearch.place(x=105,y=35)

#select button
btnSelect=Button(app,text='انتخاب',
                 bg='orange',fg='white',width=10,
                 command=SelectBook)
btnSelect.place(x=155,y=35)
#delete button
btnDelete=Button(app,text='حذف',bg='red',fg='white',width=10,
                 command=lambda:DeleteBook())
btnDelete.place(x=240,y=35)

#tree view
bookTree=ttk.Treeview(app,columns=('c1','c2','c3','c4','c5'),
                      show='headings',
                      height=18)
#c1
bookTree.column('#1',width=36)
bookTree.heading('#1',text='ردیف')
#c2
bookTree.column('#2',width=125)
bookTree.heading('#2',text='عنوان کتاب')
#c3
bookTree.column('#3',width=100)
bookTree.heading('#3',text='نویسنده')
#c4
bookTree.column('#4',width=80)
bookTree.heading('#4',text='انتشارات')
#c5
bookTree.column('#5',width=50)
bookTree.heading('#5',text='گروه')

bookTree.place(x=5,y=75)


CreateTableGroup()
CreateTableBook()
ShowBooks(entrySearch.get())
app.mainloop()
