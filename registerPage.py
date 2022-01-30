from tkinter import *

# file address storing user login information
user_data_file = "user_data.txt"


class registerPage:
	# SET UP PAGE
    def __init__(self, parent, *args, **kwargs):
        register = parent
        register.title("Register New User")
        register.geometry("500x500")

        user = StringVar()
        password = StringVar()

        Label(register, text="Create New Account", font=("Bahnschrift", 24)).grid(row=0, column=0, padx=120, pady=10,
                                                                                  columnspan=2)

        Label(register, text="Username:").grid(row=1, column=0, pady=10)
        enter_user = Entry(register, textvariable=user)
        enter_user.grid(row=1, column=1)

        Label(register, text="Password:").grid(row=2, column=0, pady=10)
        enter_pass = Entry(register, textvariable=password)
        enter_pass.grid(row=2, column=1)

        Button(register, text="Register", padx=20, pady=10, command=lambda: self.register_new_user(register, user, password)
               ).grid(row=3, column=0, pady=20, columnspan=2)
        Button(register, text="Return to Menu", padx=20, pady=10, command=register.destroy).grid(row=5, column=0,
                                                                                                 pady=20,
                                                                                                 columnspan=2)

    def register_new_user(self, mainW, username, password):
        verifyUsers, user_count = self.check_user_limit()
        veryifyNewAccount = self.check_new_account(username, password)

        # write data to file
        if verifyUsers and veryifyNewAccount == 6:
            # update user_count and restore previous data to file
            file = open(user_data_file, "r")
            data = file.readlines()
            data[0] = str(user_count) + "\n"
            file.close()

            file = open(user_data_file, "w")
            file.writelines(data)
            file.close()

            # append new data to file
            file = open(user_data_file, "a")
            file.write(username.get() + "," + password.get() + "\n")
            file.close()

            Label(mainW, text="                 Registration Success                 ", font=("Calibri", 24),
                  fg="green").grid(row=4, column=0,
                                   columnspan=2)
        elif verifyUsers == False:
            Label(mainW, text="Registration Failed: \n Number of Users Exceeded Limit", font=("Calibri", 16),
                  fg="red").grid(row=4, column=0, columnspan=2)

        elif veryifyNewAccount == 1:
            Label(mainW, text="Registration Failed: \n User Already Registered", font=("Calibri", 18),
                  fg="red").grid(row=4, column=0, columnspan=2)

        #  ...
		# [REMOVED REST OF IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
		
    def check_user_limit(self):
        user_count = 0

        # get latest user_count from first line in file
        file = open(user_data_file, "r")
        user_count = int(file.readline())
        file.close()

        if user_count == 10:
            return False, user_count
        else:
            user_count = user_count + 1
            return True, user_count

    def check_new_account(self, username, password):
		
		# get previously registered user data
        file = open(user_data_file, "r")
        data = file.readlines()
        file.close()

        for users in data[1:]:
            if (users.split(',')[0] == username.get()):
                return 1

        if (username.get() == ""):
            #[REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

        if (password.get() == ""):
            #[REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

        for character in username.get():
            if (character == ","):
                #[REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

        for character in password.get():
            if (character == ","):
                #[REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
				
        # if user registration info is valid
        #[REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
