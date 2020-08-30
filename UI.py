import numpy
import time
import cv2
from tkinter import *
import os
from playsound import playsound


os.system("splash_screen1.py")
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Welcome To Face Detection System!!!')
frame.config(background='light blue')
label = Label(frame, text="Face Detection System",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)


def function2():
    os.system("permission_for_registration.py")


def function3():
    os.system("lock_unlock_face_recognition.py")


def function4():
    os.system("training_model.py")

def function5():
    os.system("Project_Documentation.docx")

def function6():
    root.destroy()


menu = Menu(root)
root.config(menu=menu)

but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=function2,text='new registration',font=('helvetica 15 bold'))
but1.place(x=5,y=100)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=function4,text='Training Model',font=('helvetica 15 bold'))
but2.place(x=5,y=180)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=function3,text='Recognize',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=function5,text='Documentation of Project',font=('helvetica 15 bold'))
but4.place(x=5,y=320)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=function6,font=('helvetica 15 bold'))
but5.place(x=220,y=490)
playsound("sounds/welcome.mp3")

root.mainloop()

