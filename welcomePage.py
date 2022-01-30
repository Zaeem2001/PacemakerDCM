from tkinter import *

from loginPage import *
from registerPage import *

class welcomePage:
	# SET UP PAGE
    def __init__(self, parent, *args, **kwargs):
        welcome = parent

        welcome.geometry("500x500")
        welcome.title("Login to DCM")

        Label(welcome, text="Pacemaker DCM", font=("Bahnschrift", 24), justify=CENTER).grid(row=0, column=0, padx=140)
        Label(welcome, text="").grid(row=1, column=0)
        Button(welcome, text="Login", padx=20, pady=10, command=lambda: self.topLevelLogin(welcome)).grid(row=2,
                                                                                                          column=0)
        Label(welcome, text="").grid(row=3, column=0)
        Label(welcome, text="Not a registered user?").grid(row=4, column=0, pady=10)
        Button(welcome, text="Register", padx=20, pady=10, command=lambda: self.topLevelRegister(welcome)).grid(row=5,
                                                                                                                column=0)
        Label(welcome, text="", pady=100).grid(row=6, column=0)
        Button(welcome, text="Quit", padx=20, pady=10, command=welcome.destroy).grid(row=6, column=0)

        welcome.mainloop()

	# connect register and login windows to welcome page
    def topLevelRegister(self, mainW):
        registerPg = Toplevel(mainW)
        registerWindow = registerPage(registerPg)

    def topLevelLogin(self, mainW):
        loginPg = Toplevel(mainW)
        LoginWindow = loginPage(loginPg, mainW)

def main():
    root = Tk()
    app = welcomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()