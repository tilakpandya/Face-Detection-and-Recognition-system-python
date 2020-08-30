from subprocess import call
import cv2
import sys
import numpy as np
import os
import datetime
from tkinter import *
import webbrowser
from playsound import playsound


#os.system("training_model.py")
now = datetime.datetime.now()
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
        

recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read('trainer/trainer.yml')  #load training model
cascadePath = "haarcascade_frontalface_default.xml"  #cascade path
faceCascade = cv2.CascadeClassifier(cascadePath);  #load cascade
font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Set the font style


folderPath = 'D:/sample.docx'
def History():
    os.system("History.txt")


def hide():
        call(["attrib", "+H", folderPath])
        #tkinter.messagebox.showinfo('answer', 'HIDE SUCCESSFULLY....')
        playsound("sounds/hide.mp3")


def unhide():
        call(["attrib", "-H", folderPath])
        webbrowser.open('file:///' + folderPath)
        #tkinter.messagebox.showinfo('answer', 'UNHIDE SUCCESSFULLY....')
        playsound("sounds/unhide.mp3")

def dataset():
    Path='D:/BCA/bca-6/Face-Detection-and-Recognition-system-python/dataset'
    webbrowser.open('file:///' +Path)

def function6():
    root.destroy()

f = open("History.txt", "a")
f.write(str(now)+"\n")
f.close()

root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Face Detection System')
frame.config(background='light blue')
label = Label(frame, text="Face Detection System",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

# stting title for the window
root.title("Face Comparision Found")

# creating second button
menu = Menu(root)
root.config(menu=menu)

but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=unhide,text='UNHIDE FILE',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=hide,text='HIDE FILE',font=('helvetica 15 bold'))
but2.place(x=5,y=190)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=dataset,text='Open Dataset Folder',font=('helvetica 15 bold'))
but3.place(x=5,y=270)

but6=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='History',command=History,font=('helvetica 15 bold'))
but6.place(x=5,y=350)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=function6,font=('helvetica 15 bold'))
but5.place(x=220,y=490)

count=0
count1=0
cam = cv2.VideoCapture(0)
while (cam.isOpened()):

    ret, im =cam.read()
    if ret:
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 1)
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # Recognize the face belongs to which ID

            if (confidence <= 40):  # confidence usually comes greater than 80 for strangers
                cv2.rectangle(im, (x - 5, y - 5), (x + w + 20, y + h + 20), (0, 255, 0), 2)
                cv2.putText(im, str(round(confidence)), (x + 198, y + h), font, 1.00, (0, 255, 0), 1)
                # Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # Recognize the face belongs to which ID
                print("allowed   " + str(confidence))
                count = count + 1
                if (count == 15):
                    cam.release()
                    playsound("sounds/recognize successfully.mp3")
                    root.mainloop()

            else:  # confidence usually comes greater than 50 for correct user(s)
                cv2.rectangle(im, (x - 5, y - 5), (x + w + 20, y + h + 20), (0, 0, 255), 2)
                cv2.putText(im, str(round(confidence)), (x + 198, y + h), font, 1.00, (0, 0, 255), 1)
                # Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # Recognize the face belongs to which ID
                count1 = count1 + 1
                print("not allowed  " + str(confidence))
                if (count1 == 250):
                    playsound("sounds/recognize unsuccessfully.mp3")
                    cam.release()

    cv2.imshow('Webcam',im) 

    if cv2.waitKey(10) & 0xFF == ord(' '):      # If space key is pressed, terminate the  program
        break
cam.release()
cv2.destroyAllWindows()
