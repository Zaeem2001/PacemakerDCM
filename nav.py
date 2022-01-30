from tkinter import *
from loginPage import *
from mainApplication import *
from serial.tools.list_ports import comports
from functools import partial
from serialcom import*
import serial
from mainApplication import *

class nav:

    def __init__(self, parent, *args, **kwargs):
        
        self.nav = parent
        self.DCM = args[0]
        self.userName = args[1];
        self.serial = args[2]
        

        Label(self.nav, text="     Welcome to the DCM, " + self.userName + ": ", font=("Calibri", 14)).grid(row=0, column=0)
        self.pmStatus = Label(self.nav, text="Pacemaker Device Status: No Pacemaker Device Detected", font=("Calibri", 13), padx = 35)
        self.pmStatus.grid(row=0, column=1, sticky = W, columnspan= 2)
        Button(self.nav, text="Dismiss", font=("Calibri", 12), command=self.changePmStatus).grid(row=0, column=3, pady=3, ipadx= 50)
        Button(self.nav, text="About", font=("Calibri", 12), command = self.about).grid(row=1, column=0, pady=3, ipadx= 50)

        self.connectStatus = Label(self.nav, text="Connection Status:  Disconnected ", font=("Calibri", 13), padx= 35 )
        self.connectStatus.grid(row=1, column=1, sticky = W)
       
        self.portnums = []

        com_ports = Menubutton(self.nav, text="Connect to COM Port", relief = GROOVE)
        com_ports.menu = Menu(com_ports, tearoff=0)
        com_ports["menu"] = com_ports.menu

        for port in sorted(self.serial.ports):
            self.portnums.append(("{}".format(port)))

        print(self.portnums)
        for x in range(len(self.portnums)):
            com_ports.menu.add_command(label = self.portnums[x], command = partial(self.on_select, x))
        com_ports.grid(row=1, column=2, sticky = W)

        Button(self.nav, text="New Patient", font=("Calibri", 12), command=self.changeConnectStatus).grid(row=1, column=3, pady=3, ipadx= 27)

        Label(self.nav, text= "-------------------------------------------------------", font=("Calibri", 13), padx = 10).grid(row=2, column=0, sticky = W)
        Label(self.nav, text= "     ---------------------------------------------------------------------------------------------", font=("Calibri", 13), padx = 10).grid(row=2, column=1, sticky = W, columnspan= 2)
        Button(self.nav, text="End Session", font=("Calibri", 12), command= lambda : self.back_to_welcome(self.DCM)).grid(row=2, column=3, pady=3, ipadx= 50)

        self.nav.grid(row=0)
    
    def changePmStatus(self):
        self.pmStatus.config(text ="Pacemaker Device Status: No Issues")

    def changeConnectStatus(self):
        self.connectStatus.config(text ="Connection Status: Disconnected")
        self.pmStatus.config(text = "Pacemaker Device Status: No Pacemaker Device Detected")
        self.serial.ser.port = ""
    
    def on_select(self,index):
        print(index)
        comport = self.portnums[index][0:4]

        print(comport)

        try:
            self.serial.ser.port = comport
            print("Connected to " + comport)
            print(self.portnums[index][7:21])
            self.connectStatus.config(text ="Connection Status: Connected to " + comport)

            if(self.portnums[index][7:21] == "JLink CDC UART"):
                self.pmStatus.config(text = "Pacemaker Device Status: New Pacemaker Device Detected")
            else:
                self.pmStatus.config(text = "Pacemaker Device Status: No Pacemaker Device Detected")


        except serial.serialutil.SerialException:
            print("Port not Connected")
            self.connectStatus.config(text ="Disconnected")


    def back_to_welcome(self,DCM):
        DCM.destroy()
    

        #welcome_page()

    def about(self):
        aboutScr = Toplevel(self.DCM)
        aboutScr.title("About")
        aboutScr.geometry("500x300")
        Label(aboutScr, text=" About ", font=("Calibri", 18)).grid(row=0, column=0, pady= 7, padx = 10)
        Label(aboutScr, text=" Application model number: 774945732672798", font=("Calibri", 14)).grid(row=1, column=0, pady= 4, padx = 10)
        Label(aboutScr, text=" Application software revision number in use: Version 2.1.0", font=("Calibri", 14)).grid(row=2, column=0, pady= 4, padx = 10)
        Label(aboutScr, text=" DCM serial number: 9M5agyn3QDzi25T", font=("Calibri", 14)).grid(row=3, column=0, pady= 4, padx = 10)
        Label(aboutScr, text=" Institution name: McMaster University ", font=("Calibri", 14)).grid(row=4, column=0, pady= 4, padx = 10)
        Button(aboutScr, text="Close", font=("Calibri", 14), command= aboutScr.destroy).grid(row=5, column=0, pady = 7, ipadx= 30, ipady= 5, padx = 10)