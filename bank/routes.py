import mimetypes
from pickle import FALSE
from unicodedata import name
from io import BytesIO
import base64, os
from unittest import result
import sys
import os
import numpy as np
from datetime import datetime
import cv2
from bank import app
from werkzeug.utils import secure_filename
from bank.bank_attendance import att
import face_recognition
from flask import render_template, redirect, url_for, flash, request,Response
from bank.models import Employee, Customer, Upload
from bank.forms import EmployeeRegisterForm, UserLoginForm, EmployeeLoginForm, UserRegisterForm, Debit
from bank import db
from bank.face_reg import faceCap
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/index') #two urls for same page
def index_page():
    return render_template('index.html')

@app.route('/user_home') 
def user_home_page():
    return render_template('user_home.html')

@app.route('/employee_home') 
def employee_home_page():
    return render_template('employee_home_page.html')

ALLOWED_EXTENSIONS = {'txt','pdf','png','jpg','jpeg','gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDERR = "bank/emp_reg_faces/emp_reg_faces/.."
app.config['UPLOAD_FOLDERR'] = UPLOAD_FOLDERR


@app.route('/employee_register', methods=['GET','POST'])
def employee_register_page():
    form = EmployeeRegisterForm()
    if form.validate_on_submit():
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('user_home_page'))

        if file and allowed_file(file.filename):
            filename = secure_filename(form.username.data)
            filename = f"{filename}.jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDERR'], filename))
        user_to_create = Employee(username=form.username.data,password=form.password1.data,filename = file.filename,filedata = file.read())
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Employee Account Created Successfully! Welcome {user_to_create.username}', category='success')
        return redirect(url_for('account_details')) 
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f"Account was not created due to {msg}", category='danger')
 
    return render_template('employee_register.html', form=form)

@app.route('/account_details', methods=['GET','POST'])
def account_details():
    debit_form = Debit()
    form = UserLoginForm()
    # logged_user = Customer.query.filter_by(username=form.username.data).first()
    # logged_bal = logged_user.balance
    return render_template('account_details.html')
  

@app.route('/employee_login',methods=['GET','POST'])
def employee_login_page():
    form = EmployeeLoginForm()
    if form.validate_on_submit():
        attempted_user = Employee.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username} ', category='success')
            flash(f'Your attendance marked as: {attempted_user.username} ', category='success')
            return redirect(url_for('cams'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('employee_login.html', form=form)    


UPLOAD_FOLDER = "bank/uploads/uploads/.."
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def face_validation(upload_id):
    form = UserRegisterForm()
    user_reg_face = Customer.query.filter_by(id=upload_id).first()
    known_face = face_recognition.load_image_file(f"bank/uploads/{user_reg_face.username}.jpg")
    try:
        face_encoded = face_recognition.face_encodings(known_face)[0]
    except IndexError as e:
        print(e)
        sys.exit(1)
    log_user = Customer.query.filter_by(username=form.username.data).first()
    face_test = face_recognition.load_image_file(f"bank/known_faces/{log_user.username}.jpg")
    
    try:
        user_encoded = face_recognition.face_encodings(face_test)[0]
    except IndexError as e:
        print(e)
        sys.exit(1)
    results = face_recognition.compare_faces([face_encoded],user_encoded)
    return results
    
@app.route('/user_register', methods=['GET','POST'])
def user_register_page():
    form = UserRegisterForm()
    if form.validate_on_submit():
    #if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('user_home_page'))

        if file and allowed_file(file.filename):
            filename = secure_filename(form.username.data)
            filename = f"{filename}.jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user_to_create = Customer(username=form.username.data,email_address=form.email_address.data,password=form.password1.data,filename = file.filename,filedata = file.read())
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Customer Account Created Successfully! Welcome {user_to_create.username}', category='success')
        return redirect(url_for('transfer'))
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f"Account was not created due to {msg}", category='danger')

    return render_template('user_register.html', form=form)

@app.route('/user_login', methods=['GET', 'POST'])
def user_login_page():
    form = UserLoginForm()
    flash("We are accessing your camera for face id please face your Webcam properly",category='danger')
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data 
        ):
            
            tim=3
            faceCap(tim)
            res = face_validation(attempted_user.id)
            # if res == [False]:
            #     for i in range(2):
            #         faceCap()
            #         i=i+1
            if res == [True]:
                login_user(attempted_user)
                print(res)
                flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
                #return redirect(url_for('transfer'))
                return redirect(url_for('user_details'))
            else:
                print(res)
                flash('Face Id did not match! Please try again', category='danger')
        else:
            flash('Username and password did not match! Please try again', category='danger')

    return render_template('user_login.html', form=form)


@app.route('/user_details', methods=['GET','POST'])
def user_details():
    # if request.method == 'POST':
    #     return redirect(url_for('transfer'))
    return render_template('user_details.html')


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    form = Debit()
    flash("We are accessing your camera for face i please face your Webcam properly",category='danger')
    if form.validate_on_submit():
        
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        credit_user = Customer.query.filter_by(username=form.username2.data).first()
        if attempted_user and credit_user:
            money = form.money.data
            #flash(f'You are requesting to transfer {form.money.data} rupees',category='danger')
            
            tim=3
            faceCap(tim)
            res = face_validation(attempted_user.id)
        
            if res == [True]:
                print(res)
                attempted_user.balance -= money
                credit_user.balance += money
                db.session.commit()
                flash(f'Success {money} rupees have been debited from your account and credited to {form.username2.data} ', category='success')
                return redirect(url_for('transfer'))
            else:
                flash(f'Your Face id did not match with our database! :( Please try again', category='danger')
        else:
            flash('Username did not match with our database! Please try again', category='danger')

    return render_template('transfer.html', form=form)



@app.route('/cams',methods=['GET', 'POST'])
def cams():
    if request.method == 'POST':
        camera.release()            
        cv2.destroyAllWindows()
        return redirect(url_for('account_details'))      
    return render_template('cam_streaming.html')

camera = cv2.VideoCapture(0)

path = UPLOAD_FOLDERR
images = []
known_face_names = []
mylist = os.listdir(path)
for cls in mylist:
    curr_img = cv2.imread(f"{path}/{cls}")
    images.append(curr_img)
    known_face_names.append(os.path.splitext(cls)[0])

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
known_face_encodings = findEncodings(images)

def MarkAttendance(name):
    with open('bank/attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                MarkAttendance(name)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
  

@app.route('/cam_stream',methods=['GET', 'POST'])
def cam_stream():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You are Logged out!", category='info')
    return redirect(url_for('index_page'))
