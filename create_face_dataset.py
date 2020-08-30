#from email.contentmanager import set_text_content
import cv2  # import OpenCV
import os
from tkinter import *
import random
from playsound import playsound

ran=random.randint(1,1000)
def check_path(path):  # function to confirm whether the given path exists or not
    dir = os.path.dirname(path)  # if it doesn't exist this function will create
    if not os.path.exists(dir):
        os.makedirs(dir)


cam = cv2.VideoCapture(0)  # Start video capturing
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Detect object in video stream using Haarcascade Frontal Face
count = 0  # Initialize sample face image
check_path("dataset/")
playsound("sounds/prompt.mp3")
user=input("Enter name=")
while (cam.isOpened()):
    _, image_frame = cam.read()  # Capture video frame _, is used to ignored first value because vid_cam.read() is returning 2 values
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.4, 5)  # Detect faces using Cascade Classifier(xml file)

    for (x, y, w, h) in faces:
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Crop the image frame into rectangle
        count += 1  # Increment face image
        cv2.imwrite("dataset/" + str(user) + '.' +str(ran)+'.'+ str(count) + ".jpg",gray[y:y + h, x:x + w])  # Save the captured image into the datasets folder
        cv2.imshow('Creating Dataset!!!',image_frame)  # Display the video frame, with rectangular box on the person's face

    if cv2.waitKey(10) & 0xFF ==(' '):  # To stop taking video, press 'Esc'
        break

    elif count > 200:  # If image taken reach 100, stop taking video
        break

cam.release()  # Stop video
cv2.destroyAllWindows()  # Close all windows
playsound("sounds/samples.mp3")
