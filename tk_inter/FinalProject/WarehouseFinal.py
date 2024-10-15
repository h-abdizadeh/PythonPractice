from tkinter import *
from tkinter import ttk
import sqlite3

mydatabase='data/warehouse.db'
products='products'#table name

def CreateProductTable():
    con=sqlite3.connect(mydatabase)
    con.execute(f'''CREATE TABLE IF NOT EXISTS {products} 
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    brand TEXT,
    inv INT,
    Category TEXT)''')
    con.commit()

def InsertProduct():
    # productTuple=('laptop','asus',5,categoryList[2])
    productTuple=(nameEntry.get(),
                  brandEntry.get(),
                  int(invEntry.get()),
                  categoryDefault.get())
    con=sqlite3.connect(mydatabase)
    if btnSubmit['text']=='ویرایش':
        con.execute(f'''UPDATE {products} SET 
                    name='{productTuple[0]}',
                    brand='{productTuple[1]}',
                    inv={productTuple[2]},
                    category='{productTuple[3]}' 
                    WHERE id={int(searchEntry.get())}''')
        con.commit()
        SelectAllProducts()
        btnSubmit['text']='ثبت'
        return
    #myId=(5,)
    con.execute(f'''INSERT INTO 
                {products}(name,brand,inv,category) 
                VALUES {productTuple}''')
    con.commit()
    SelectAllProducts()

def SelectAllProducts():
    con=sqlite3.connect(mydatabase)
    # result=con.execute(f'SELECT name,inv FROM {products}')
    result=con.execute(f'SELECT * FROM {products}')
    
    showTree.delete(*showTree.get_children())
    for item in result:
        showTree.insert('',END,values=item)
    
def SelectSearchProducts():
    search=searchEntry.get()
    con=sqlite3.connect(mydatabase)
    result=con.execute(f'''SELECT * FROM {products} 
    WHERE name LIKE \'%{search}%\' or brand=\'{search}\'''')

    showTree.delete(*showTree.get_children())
    for item in result:
        showTree.insert('',END,values=item)
    
def DeleteProduct():
    id=int(searchEntry.get())
    con=sqlite3.connect(mydatabase)
    con.execute(f'''DELETE FROM {products} 
                WHERE id={id}''')
    con.commit()
    searchEntry.delete(0,END)
    SelectAllProducts()

def SelectProduct():
    id=int(searchEntry.get())
    con=sqlite3.connect(mydatabase)
    result=con.execute(f'''SELECT * FROM {products} 
                        WHERE id={id}''').fetchall()

    nameEntry.delete(0,END)
    brandEntry.delete(0,END)
    invEntry.delete(0,END)
    
    nameEntry.insert(0,result[0][1])
    brandEntry.insert(0,result[0][2])
    invEntry.insert(0,result[0][3])
    btnSubmit['text']='ویرایش'



app=Tk()
app.title('warehouse')
app.geometry('600x400')
app.resizable(FALSE,FALSE)

#add product form
addLabel=Label(app,text='ثبت/ویرایش کالا',
               font='tahoma 10 bold',anchor=N,  
               width=28,height=30,
               bg='teal',fg='white')
addLabel.place(x=370,y=0)

nameLabel=Label(app,text='نام کالا',
                font='tahoma 11',
                bg='teal',fg='yellow')
nameLabel.place(x=540,y=32)

nameEntry=Entry(app,font='tahoma 11 bold',width=15)
nameEntry.place(x=375,y=32)

brandLabel=Label(app,text='برند',
                font='tahoma 11',
                bg='teal',fg='yellow')
brandLabel.place(x=540,y=64)

brandEntry=Entry(app,font='tahoma 11 bold',width=15)
brandEntry.place(x=375,y=64)

#inv == inventory
invLabel=Label(app,text='موجودی',
                font='tahoma 11',
                bg='teal',fg='yellow')
invLabel.place(x=540,y=96)

invEntry=Entry(app,font='tahoma 11 bold',width=15)
invEntry.place(x=375,y=96)

#category
categoryList=['لوازم خانگی','مواد غذایی','سایر موارد']
categoryDefault=StringVar(app,'انتخاب دسته بندی کالایی')
categoryOption=OptionMenu(app,categoryDefault,*categoryList)
categoryOption.place(x=375,y=128)

#add/edit button
btnSubmit=Button(app,text='ثبت کالا',
                 width=30,bg='yellow',
                 command=InsertProduct)
btnSubmit.place(x=375,y=175)


#search select delete
searchLabel=Label(app,text='جستجو / انتخاب/ حذف',
               font='tahoma 10 bold',anchor=N,  
               width=45,height=30,
               bg='white',fg='teal')
searchLabel.place(x=0,y=0)

searchEntry=Entry(app,font='tahoma 11 bold',width=15)
searchEntry.place(x=128,y=32)

searchBtn=Button(app,text='بگرد',
                 bg='teal',fg='white',width=5,
                 command=SelectSearchProducts)
searchBtn.place(x=80,y=32)

selectBtn=Button(app,text='انتخاب',
                 bg='yellow',width=13,
                 command=SelectProduct)
selectBtn.place(x=80,y=64)

deleteBtn=Button(app,text='حذف',
                 bg='red',fg='white',width=13,
                 command=DeleteProduct)
deleteBtn.place(x=184,y=64)


# show info (tree)
showTree=ttk.Treeview(app,
                    column=('c1','c2','c3','c4','c5'),
                    show='headings',height=12)
showTree.heading('#1',text='ردیف')
showTree.heading('#2',text='نام کالا')
showTree.heading('#3',text='برند')
showTree.heading('#4',text='تعداد')
showTree.heading('#5',text='دسته بندی')

showTree.column('#1',width=35)
showTree.column('#2',width=100)
showTree.column('#3',width=80)
showTree.column('#4',width=45)
showTree.column('#5',width=100)

showTree.place(x=2,y=96)

btnShowAll=Button(app,text='نمایش تمام کالاها',
                  bg='teal',fg='white',
                  command=SelectAllProducts)
btnShowAll.place(x=10,y=365)

CreateProductTable()
SelectAllProducts()
app.mainloop()