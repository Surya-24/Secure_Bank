# Secure_Bank
 Web App Using Flask Web Framework, It Logins users using Face Detection, Marks Attendance for Employees in the bank and When the user wants to transact money, its asks for face id for security
Bank System with Face-Login 

## Requirements: 

Python 3.9.1 version: This can be installed from https://www.python.org/downloads/release/python-391/ 

Visual Studio 2019 community version 

While installing Visual Studio 2019 community version, we have to tick on Desktop development in C++ plugin. 

 

 

Install and Create a Virtual Environment 

pip install virtualenv 

virtualenv bankapp 

After creating Virtual environment, we need first direct our directory to bankapp by using cd bankapp then Scripts folder by using cd Scripts  

Then use activate command 

Then download my github repository from https://github.com/Surya-24/Secure_Bank or clone my github repository by using                 git clone -q https://github.com/Surya-24/Secure_Bank command 

Then change the directory to bank folder by cd bank. 

Then install the requirements using requirements.txt file which is present in the repository itself. Packages can be installed by using pip install requirements.txt 

 

After successful installation of packages present in requirements.txt, there is one last package named dlib, for installation of this package firstly go to https://github.com/Surya-24/Secure_Bank/blob/main/dlib-19.22.99-cp39-cp39-win_amd64.whl then download the file using download option in the github. After downloading the file, copy the path where it is downloaded then come back to command interface where we have installed packages related to the project, type pip install “paste the path here\dlib-19.22.99-cp39-cp39-win_amd64.whl” 

If there is an error make sure you are using Python 3.9.1 version or above. 

If there is no error, we are good to run the WebApp. 

For running the app, firstly we need to create the database 

Make sure you are in Secure_bank directory, if not use cd Secure_bank, then follow the steps:  

 python 

 from bank import db 

 db.create_all() 

 exit() 

Now database is created successfully in the local machine and the app is ready to use 

Now make sure the directory is unchanged, it should be in Secure_bank directory, if not use                   cd Secure_bank. 

Now use command python run.py 

 

If the shown picture is displayed then the app is running successfully on the local machine. 

Now the last step is to open any browser like Chrome, Microsoft Edge or Brave. 

In the search bar paste the given link in the Command Prompt or simply type http://localhost:5000/ and check link to be inserted or explore the website. 

Thank You 

You can connect with me on the LinkedIn  
