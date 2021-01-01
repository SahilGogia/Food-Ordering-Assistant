import numpy as np
import cv2
import pickle

def faceid():
 i=0
 face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
 recognizer = cv2.face.LBPHFaceRecognizer_create()
 recognizer.read("trainner.yml")

 labels ={}
 with open("labels.pickle", 'rb') as f:
    og_labels=pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}


 cap = cv2.VideoCapture(0)

 while(True):

    ret, frame = cap.read() #captures frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for(x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w] #(start_cord, end_cord)
        roi_color = frame[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)
        if conf>=45:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            if name == "sahil":
             color = (255,255,255)
             stroke = 2
             cv2.putText(frame,f"User {name} detected please press q",(x,y),font,1,color,stroke,cv2.LINE_AA)
             fname = name
             i=1
            color = (255,255,255)
            stroke = 2
            #cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

        color = (0,255,0)
        stroke =1
        end_x = x+w
        end_y = y+h
        cv2.rectangle(frame, (x,y), (end_x,end_y ),color,stroke)

    cv2.imshow('frame',frame) #display the resulting farme

    if cv2.waitKey(100) & 0xFF == ord('q'): #breaks when q is pressed
      break

 #releases the capture when done      
 cap.release()
 cv2.destroyAllWindows()
 return name
