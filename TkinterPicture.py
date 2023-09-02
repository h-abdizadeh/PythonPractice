from tkinter import *
#2 -> pillow
from PIL import Image
from PIL import ImageTk

form=Tk()
form.geometry('512x480')

imgPath='images/ball.png'

#1
# imgData=PhotoImage(file=imgPath)
# # imgData=imgData.zoom(2)
# imgData=imgData.subsample(5,5)
# imgLabel=Label(form,image=imgData)
# imgLabel.pack()

#2->pillow
img=Image.open(imgPath)
img=img.resize((512,480))
imgData=ImageTk.PhotoImage(img)
imgLabel=Label(form,image=imgData)
imgLabel.pack()


form.mainloop()