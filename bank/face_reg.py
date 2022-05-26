import numpy as np
from bank.models import Customer, Employee
from bank import app
import cv2
import time
import xml.etree.ElementTree as ET
from bank.forms import UserRegisterForm

def faceCap(tim):
    tim = int(tim)
    UPLOAD_FOLDERR = "bank/known_faces/known_faces/.."
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDERR
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        # if cv2.waitKey(1) == ord('q'):
        #     break
        tim = tim-1
        time.sleep(1)
        form = UserRegisterForm()
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        #cv2.imshow('frame', frame)
        name = f"bank/known_faces/{attempted_user}.jpg"
        cv2.imwrite(name , frame)
        if tim == 0:
            break

    cap.release()
    cv2.destroyAllWindows()
