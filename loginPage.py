from tkinter import *
import os

from DCM import *
from welcomePage import *

user_data_file = "user_data.txt"

class loginPage:

	# SET UP PAGE
	def __init__(self, parent, *args, **kwargs):
        login = parent
        self.welcome = args[0]
        login.title("Login")
        login.geometry("500x500")

        user = StringVar()
        password = StringVar()
        
        Label(login, text="Login", font=("Bahnschrift", 24)).grid(row=0, column=0, padx=220, pady=10, columnspan=2)
        Label(login, text="Username:").grid(row=1, column=0, pady=10)
        enter_user = Entry(login, textvariable=user)
        enter_user.grid(row=1, column=1)

        Label(login, text="Password:").grid(row=2, column=0, pady=10)
        enter_pass = Entry(login, textvariable=password)
        enter_pass.grid(row=2, column=1)

        Button(login, text="Login", padx=20, pady=10, command= lambda: self.login_check(login, user, password)
               ).grid(row=3, column=0, pady=20, columnspan=2)
        Button(login, text="Return to Menu", padx=20, pady=10, command= login.destroy
               ).grid(row=5, column=0, pady=20, columnspan=2)

    def login_check(self, mainW, username, password):

        # import data from user_data_file
        file = open(user_data_file, "r")
        data = file.readlines()
        file.close()

        flag = 1  # to track if user was found or not
        user_count = self.get_user_limit()  # get latest user_count

        message = Label(mainW, text="", font=("Calibri", 18), fg="green")
        message.grid(row=4, column=0, columnspan=2)  # initialize label

        for i in range(1, user_count + 1):
            # [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
			
            if (username.get() == ...):  # check to see if user is in list [REMOVED PART OF IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
                if (password.get() == ...):  # check to see if password is correct [REMOVED PART OF IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
                    message.config(text="                      Login Success                        ")
                    flag = 0
                    self.DCM_login(username.get())  # go to main DCM page

        if (flag):
            message.config(text="Login Failed: Username and/or \n Password Not Recognized", fg="red")


    def get_user_limit(self):
        user_count = 0

        # get latest user_count from first line in file
        file = open(user_data_file, "r")
        user_count = int(file.readline())
        file.close()
        return user_count
    
    def DCM_login(self, username):

        DCMScreen = Tk()
        DCMWindow = DCM(DCMScreen, username)
        self.welcome.destroy()

        

