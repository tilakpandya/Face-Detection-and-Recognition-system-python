import cv2
import os
from tkinter import *
from playsound import playsound
import os.path

root = Tk()
root.configure(background="blue")


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def check_path(path):  # function to confirm whether the given path exists or not
    dir = os.path.dirname(path)  # if it doesn't exist this function will create
    if not os.path.exists(dir):
        os.makedirs(dir)


recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read('trainer/trainer.yml')  #load training model
cascadePath = "haarcascade_frontalface_default.xml"  #cascade path
faceCascade = cv2.CascadeClassifier(cascadePath);  #load cascade
font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Set the font style

count = 0
count1 = 0
face_id = 1
check_path("dataset/")
path = "dataset/"
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])


if(num_files == 0):
    os.system("create_face_dataset.py")

else:
    playsound("sounds/permission2.mp3")
    cam = cv2.VideoCapture(0)
    while (cam.isOpened()):
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # Recognize the face belongs to which ID
            if (confidence <= 40):  # confidence usually comes greater than 80 for strangers
                cv2.rectangle(im, (x - 5, y - 5), (x + w + 20, y + h + 20), (0, 255, 0), 2)
                cv2.putText(im, str(round(confidence)), (x + 198, y + h), font, 1.00, (0, 255, 0), 1)
                print("allowed "+str(confidence))
                count = count + 1
                if (count == 15):
                    root.withdraw()
                    #tkinter.messagebox.showinfo('answer', 'You can now register')
                    playsound("sounds/permission granted.mp3")
                    cam.release()
                    os.system("create_face_dataset.py")

            else:  # confidence usually comes less than 80 for correct user(s)
                cv2.rectangle(im, (x - 5, y - 5), (x + w + 20, y + h + 20), (0, 0, 255), 2)
                cv2.putText(im, str(round(confidence)), (x + 198, y + h), font, 1.00, (0, 0, 255), 1)
                count1 = count1 + 1
                print("not allowed "+str(confidence))
                if (count1 == 200):
                    playsound("sounds/recognize unsuccessfully.mp3")
                    cam.release()

        cv2.imshow('Registered Face...', im)
        if cv2.waitKey(10) & 0xFF == ord(' '):  # If '*' is pressed, terminate the  program
            break
cv2.destroyAllWindows()
