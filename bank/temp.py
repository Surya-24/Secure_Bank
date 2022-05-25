# from crypt import methods
# from unicodedata import name
# from bank import app
# from flask import render_template, redirect, url_for, flash, request
# from bank.models import Employee, Customer
# from bank.forms import EmployeeRegisterForm, UserLoginForm, EmployeeLoginForm, UserRegisterForm
# from bank import db
# from bank.face_reg import faceCap
# from flask_login import login_user, logout_user, login_required, current_user

# @app.route('/')
# @app.route('/index') #two urls for same page
# def index_page():
#     return render_template('index.html')

# @app.route('/user_home') 
# def user_home_page():
#     return render_template('user_home.html')

# @app.route('/employee_home') 
# def employee_home_page():
#     return render_template('employee_home_page.html')


# @app.route('/employee_register', methods=['GET','POST'])
# def employee_register_page():
#     form = EmployeeRegisterForm()
#     if form.validate_on_submit():
#         user_to_create = Employee(username=form.username.data,password=form.password1.data)
#         db.session.add(user_to_create)
#         db.session.commit()
#         login_user(user_to_create)
#         flash(f'Employee Account Created Successfully! Welcome {user_to_create.username}', category='success')
#         return redirect(url_for('account_details')) 
#     if form.errors != {}:
#         for msg in form.errors.values():
#             flash(f"Account was not created due to {msg}", category='danger')

#     return render_template('employee_register.html', form=form)

# @app.route('/account_details', methods=['GET','POST'])
# def account_details():
#     return render_template('account_details.html')

# @app.route('/employee_login',methods=['GET','POST'])
# def employee_login_page():
#     form = EmployeeLoginForm()
#     if form.validate_on_submit():
#         attempted_user = Employee.query.filter_by(username=form.username.data).first()

        
#         if attempted_user and attempted_user.check_password_correction(
#                 attempted_password=form.password.data
#         ):
#             login_user(attempted_user)
#             flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
#             return redirect(url_for('account_details'))
#         else:
#             flash('Username and password are not match! Please try again', category='danger')

#     return render_template('user_login.html', form=form)    

# @app.route('/user_register', methods=['GET','POST'])
# def user_register_page():
#     form = UserRegisterForm()
#     if form.validate_on_submit():
#         user_to_create = Customer(username=form.username.data,email_address=form.email_address.data,password=form.password1.data)
#         db.session.add(user_to_create)
#         db.session.commit()
        
#         login_user(user_to_create)
#         face = faceCap()
#         flash(f'Customer Account Created Successfully! Welcome {user_to_create.username}', category='success')
#         return redirect(url_for('account_details'))
#     if form.errors != {}:
#         for msg in form.errors.values():
#             flash(f"Account was not created due to {msg}", category='danger')

#     return render_template('user_register.html', form=form)

# @app.route('/upload',methods=['GET','POST'])
# def upload_files():


# @app.route('/user_login', methods=['GET', 'POST'])
# def user_login_page():
#     form = UserLoginForm()
#     if form.validate_on_submit():
#         attempted_user = Customer.query.filter_by(username=form.username.data).first()

        
#         if attempted_user and attempted_user.check_password_correction(
#                 attempted_password=form.password.data
#         ):
#             login_user(attempted_user)
#             flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
#             return redirect(url_for('account_details'))
#         else:
#             flash('Username and password are not match! Please try again', category='danger')

#     return render_template('user_login.html', form=form)


# @app.route('/logout')
# def logout_page():
#     logout_user()
#     flash("You are Logged out!", category='info')
#     return redirect(url_for('index_page'))





# def face_frame(self,upload_id):
#     form = UserRegisterForm()
#     user_reg_face = Customer.query.filter_by(id=upload_id).first()
#     file = user_reg_face.face_data
#     img = Image.open(file.stream)
#     img.show()
#     return img.save("{user_reg_face.username}_.jpg")


    

# @app.route('/upload',methods=['GET','POST'])
# def upload_files():
#     if request.method == 'POST':
#         file = request.files['file']
#         upload = Customer(filename = file.filename, filedata = file.read())
#         db.session.add(upload)
#         db.session.commit()
#         return redirect(url_for('account_details.html'))
#     return render_template('upload_files.html')




# <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-dark" style="color:white">
#         <div class="col-md-5 p-lg-5 mx-auto my-5">
#             <form method="POST" class="form-register" style="color:white" >
#                 <h1 class="display-4 font-weight-normal">Welcome {{ current_user.username }}</h1>
#                 <h2 class="display-4 font-weight-normal">{{ current_user.balance }}</h2>
#                 {{ form.money.label() }}
#                 {{ form.money(class="form-control", placeholder="Enter Money") }}
                
            
#             {{ form.submit(class="btn btn-lg btn-block btn-primary") }}
#             </form>
#         </div>      


# @app.route('/user_register', methods=['GET','POST'])
# def user_register_page():
#     form = UserRegisterForm()
#     if form.validate_on_submit():
#     #if request.method == 'POST':
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(url_for('user_home_page'))

#         if file and allowed_file(file.filename):
#             filename = secure_filename(form.username.data)
#             filename = f"{filename}.jpg"
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         user_to_create = Customer(username=form.username.data,email_address=form.email_address.data,password=form.password1.data,filename = file.filename,filedata = file.read())
#         db.session.add(user_to_create)
#         db.session.commit()
#         login_user(user_to_create)
#         #face = faceCap()
#         flash(f'Customer Account Created Successfully! Welcome {user_to_create.username}', category='success')
#         return redirect(url_for('account_details'))
#     if form.errors != {}:
#         for msg in form.errors.values():
#             flash(f"Account was not created due to {msg}", category='danger')

#     return render_template('user_register.html', form=form)


# # #login logout template code
# # <!--{% if current_user.is_authenticated %}
# #                 <ul class="navbar-nav">
# #                     <li class="nav-item">
                        
# #                         <a class="nav-link" style="color: lawngreen"; font-weight: bold>
# #                             <i class="bi bi-cash-coin">{{ current_user.prettier_budget }}</i>
# #                         </a>
# #                     </li>
# #                     <li class="nav-item">
# #                         <a class="nav-link">Welcome, {{ current_user.username }}</a>
# #                     </li>
# #                     <li class="nav-item">
# #                         <a class="nav-link" href="{{ url_for('logout_page') }}">Logout</a>
# #                     </li>
# #                 </ul>
# #             {% else %}
# #                 <ul class="navbar-nav">
# #                     <li class="nav-item">
# #                         <a class="nav-link" href="{{ url_for('user_login_page') }}">Login</a>
# #                     </li>
# #                     <li class="nav-item">
# #                         <a class="nav-link" href="{{ url_for('user_register_page') }}">Register</a>
# #                     </li>
# #                 </ul>
# #             {% endif %}-->

# @app.route('/user_login', methods=['GET', 'POST'])
# def user_login_page():
#     form = UserLoginForm()
#     if form.validate_on_submit():
#         attempted_user = Customer.query.filter_by(username=form.username.data).first()
#         faceCap()
#         res = face_validation(attempted_user.id)
#         if attempted_user and attempted_user.check_password_correction(
#                 attempted_password=form.password.data 
#         )and res == [True]:
            

#             login_user(attempted_user)
#             print(res)
#             flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
#             return redirect(url_for('account_details'))
#             # else:
#             #     print(res)
#             #     flash('Face Id did not match! Please try again', category='danger')
#         else:
#             print(res)
#             flash('Username and password did not match! Please try again', category='danger')

#     return render_template('user_login.html', form=form)









# cam = cv2.VideoCapture(0)
# path = "emp_reg_faces"
# images = []
# classNames = []
# mylist = os.listdir(path)
# for cls in mylist:
#     curr_img = cv2.imread(f"{path}/{cls}")
#     images.append(curr_img)
#     classNames.append(os.path.splitext(cls)[0])

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         try:
#             encode = face_recognition.face_encodings(img)[0]
#         except IndexError as e:
#             print(e)
#             sys.exit(1)
#         encodeList.append(encode)
#     return encodeList

# def MarkAttendance(name):
#     with open('attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             dtstring = now.strftime('%H:%M:%S')
#             f.writelines(f'\n{name},{dtstring}')

# encodelistKnown = findEncodings(images)
# def generate_frames():
#     while True:
#         ret,frame = cam.read()
#         if not ret:
#             break
#         else:
#             imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
#             imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#             facesinCurrFrame = face_recognition.face_locations(imgS)
#             encodesCurrFrame = face_recognition.face_encodings(imgS,facesinCurrFrame)

#             for encodeFace, faceLoc in zip(encodesCurrFrame,facesinCurrFrame):
#                 matches = face_recognition.compare_faces(encodelistKnown,encodeFace)
#                 facedis = face_recognition.face_distance(encodelistKnown,encodeFace)
#                 matchindex = np.argmin(facedis)

#                 if matches[matchindex]:
#                     name = classNames[matchindex].upper()
#                     y1,x2,y2,x1 = faceLoc
#                     y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
#                     cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#                     cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#                     cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#                     MarkAttendance(name)
#                 ret,buffer = cv2.imencode('.jpg',frame)
#                 frame = buffer.tobytes()
        
#         yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
      
# # <!--{% else %}
# #                 <ul class="navbar-nav">
# #                     <li class="nav-item">
# #                         <a class="nav-link" href="{{ url_for('login_page') }}">Login</a>
# #                     </li>
# #                     <li class="nav-item">
# #                         <a class="nav-link" href="{{ url_for('register_page') }}">Register</a>
# #                     </li>
# #                 </ul>-->






# @app.route('/transfer',methods=['GET','POST'])
# def transfer():
#     form = Debit()
#     if form.validate_on_submit():
#         money = request.form.get('money')
#         user = Customer.query.filter_by(id=current_user.id).first()
#         flash(f"You have {user.balance}")
#         flash(f"You have {money}")
#         user.balance -= money
        
#         db.commit()
        
#         #faceCap()
#         #res = face_validation(user.id)
#         # if res == [True]:
#         #     user.balance = user.balance - form.money.data
#         #     db.session.commit()
#         #     flash("Face Id Matched and Amount Deducted Successfully")
#         # else:
#         #     flash("Face Id did not match")
        
#         return redirect(url_for('transfer'))    
        
#     return render_template('transfer.html',form=form)

# <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-dark" style="color:white">
#         <div class="col-md-5 p-lg-5 mx-auto my-5">
#             <form method="POST" class="form-register" style="color:white" >
#                 <h1 class="display-4 font-weight-normal">Welcome {{ current_user.username }}</h1>
#                 <h2 class="display-4 font-weight-normal">{{ current_user.balance }}</h2>
#                 {{ form.money.label() }}
#                 {{ form.money(class="form-control", placeholder="Enter Money") }}
                
            
#             {{ form.submit(class="btn btn-lg btn-block btn-primary") }}
#             </form>
#         </div>