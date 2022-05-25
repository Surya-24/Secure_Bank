import face_recognition
import sys
import numpy as np
import cv2
import os
from datetime import datetime
from bank.models import Employee
def att():
    path = "bank/emp_reg_faces"
    images = []
    classNames = []
    mylist = os.listdir(path)

    for cls in mylist:
        curr_img = cv2.imread(f"{path}/{cls}")
        images.append(curr_img)
        classNames.append(os.path.splitext(cls)[0])

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            try:
                encode = face_recognition.face_encodings(img)[0]
            except IndexError as e:
                print(e)
                sys.exit(1)
            encodeList.append(encode)
        return encodeList

    def MarkAttendance(name):
        with open('attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtstring = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtstring}')


    encodelistKnown = findEncodings(images)

    cap = cv2.VideoCapture(0)

    while True:
        success,img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesinCurrFrame = face_recognition.face_locations(imgS)
        encodesCurrFrame = face_recognition.face_encodings(imgS,facesinCurrFrame)

        for encodeFace, faceLoc in zip(encodesCurrFrame,facesinCurrFrame):
            matches = face_recognition.compare_faces(encodelistKnown,encodeFace)
            facedis = face_recognition.face_distance(encodelistKnown,encodeFace)
            matchindex = np.argmin(facedis)

            if matches[matchindex]:
                name = classNames[matchindex].upper()
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                MarkAttendance(name)

        cv2.imshow('Beautiful Face',img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
        
