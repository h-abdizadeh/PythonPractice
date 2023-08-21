from tkinter import*

form=Tk()
# form=Tk(className='مهندسی فردا')
#form
form.title('مهندسی فردا')
form.geometry('512x512')
form.resizable(0,0)
# form.configure(bg='red')
form['bg']='#0B666A'
#label
label1=Label(form)
label1['text']='سلام به همه'
label1.place(x=10,y=10)
label1['font']=(None,25)
label1['bg']='#071952'
label1['fg']='#97FEED'
label1['width']=25
label1['height']=2
#entry
entry1=Entry(form)
entry1.place(x=10,y=100)
entry1['font']=(None,18)
#text
text1=Text(form)
text1.place(x=10,y=150)
text1['width']=50
text1['height']=10
form.mainloop()