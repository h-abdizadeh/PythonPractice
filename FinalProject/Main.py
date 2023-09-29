from tkinter import *
from tkinter import ttk #treeView
from SqLiteClass import SqliteDB

def AddProduct():
    mode=entrySearch.get()
    if len(mode)==0:
        productTuple=(entryName.get(),
                        int(entryInv.get()),
                        entryBrand.get(),
                        MenuOption.get())
        db=SqliteDB()
        db.InsertProduct(productTuple)
    else:
        productTuple=(entryName.get(),
                        int(entryInv.get()),
                        entryBrand.get(),
                        MenuOption.get(),
                        int(entrySearch.get()))
        db=SqliteDB()
        db.UpdateProduct(productTuple)

def ShowProducts():
    db=SqliteDB()
    products=db.GetProducts()

    for p in products:
        productTree.insert('',END,values=p)

def RemoveProduct():
    id=(int(entrySearch.get()),)
    db=SqliteDB()
    db.DeleteProduct(id)

def EditProduct():
    id=(int(entrySearch.get()),)
    db=SqliteDB()
    product=db.GetProduct(id)
    for p in product:
        entryName.insert(INSERT,p[1])
        entryInv.insert(INSERT,p[2])
        entryBrand.insert(INSERT,p[3])

form=Tk()
form.title('پروژه پایانی : انبار')
form.geometry('640x420')
form.resizable(False,False)


############## Add / Edit Product #######################
titleAdd=Label(form,font=('',14),text='ثبت / ویرایش کالا',
               width=25,height=2,bg='#071952',fg='white',anchor=E)
titleAdd.pack(anchor=E)

labelName=Label(form,font=('',14),text='نام کالا')
labelName.pack(anchor=E)
entryName=Entry(form,font=('',14),width=25,justify=RIGHT)
entryName.pack(anchor=E)

labelInv=Label(form,font=('',14),text='موجودی')
labelInv.pack(anchor=E)
entryInv=Entry(form,font=('',14),width=25,justify=RIGHT)
entryInv.pack(anchor=E)
6
labelBrand=Label(form,font=('',14),text='برند تولید کننده')
labelBrand.pack(anchor=E)
entryBrand=Entry(form,font=('',14),width=25,justify=RIGHT)
entryBrand.pack(anchor=E)

labelGroup=Label(form,font=('',14),text='گروه کالا')
labelGroup.pack(anchor=E)

groups=['لوازم خانگی',
        'ورزش و سرگرمی',
        'آریشی و بهداشتی',
        'پوشاک']

MenuOption=StringVar(form,'انتخاب گروه کالا')
optionGroup=OptionMenu(form,MenuOption,*groups)
optionGroup.pack(anchor=E)

btnAdd=Button(form,font=('',16),text='ثبت کالا',
              bg='#088395',fg='white',border=1,
              width=6,command=AddProduct)

btnAdd.place(x=360,y=235)
############## Add / Edit Product #######################

############## Search Product #######################
entrySearch=Entry(form,font=('',14),width=15,justify=RIGHT)
entrySearch.place(x=45,y=10)

# imgPath='images/searchicon.png'
imgPath='images/searchicon.png'

#1
imgData=PhotoImage(file=imgPath)
imgData=imgData.subsample(50,50)
imgBtnSearch=Button(form,image=imgData,border=0)
imgBtnSearch.place(x=10,y=2)

btnDelete=Button(form,font=('',12),text='حذف کالا',
                 command=RemoveProduct)
btnDelete.place(x=220,y=7)

btnEdit=Button(form,font=('',12),text='ویرایش',
                 command=EditProduct)
btnEdit.place(x=285,y=7)

############## Search Product #######################

############## Product data #######################

productTree=ttk.Treeview(form,columns=('c1','c2','c3','c4','c5'),
                         show='headings')

productTree.column('#1',anchor=CENTER,width=10)
productTree.heading('#1',text='Id')

productTree.column('#2',anchor=CENTER,width=100)
productTree.heading('#2',text='Name')

productTree.column('#3',anchor=CENTER,width=40)
productTree.heading('#3',text='Inventory')

productTree.column('#4',anchor=CENTER,width=80)
productTree.heading('#4',text='Brand')

productTree.column('#5',anchor=CENTER,width=100)
productTree.heading('#5',text='Group')

productTree.place(x=10,y=50)

btnShow=Button(form,font=('',14),text='نمایش موجودی انبار',
               bg='#3085C3',fg='white',border=1,command=ShowProducts)

btnShow.place(x=10,y=370)

############## Product data #######################

####### create database -> products table ##########
db=SqliteDB()
db.CreateProductTable()

####### create database -> products table ##########


form.mainloop()
