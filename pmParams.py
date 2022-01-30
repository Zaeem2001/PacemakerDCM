import serial
import struct
import random
import numpy as np
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep

from loginPage import *
from pacemakerModes import *
from paramChecking import *
from serialcom import*
from tkinter import *
from eGramPage import *

class pmParams:
    def __init__(self, parent, *args, **kwargs):
        self.pmParams = parent
        self.userName = args[0]
        self.serial = args[1]
        self.DCM = args[2]

        # displays current mode name
        self.mode_name = Label(self.pmParams, text="                ")
        self.mode_name.grid(row=0, column=1)

        # displays current mode name
        self.verify = Label(self.pmParams, text="Current Pacemaker Settings: ")
        self.verify.grid(row=0, column=2)

        # initialize pacemaker mode windows
        self.mode_frame = Frame(self.pmParams)
        self.mode_frame.grid(row=1, column=0, columnspan=4)

        self.message = Frame(self.pmParams)
        self.message.grid()

        self.set_mode_VOO()
        self.set_mode_AAI()
        self.set_mode_VVI()
        self.set_mode_DOO()
        self.set_mode_AOOR()
        self.set_mode_VOOR()
        self.set_mode_AAIR()
        self.set_mode_VVIR()
        self.set_mode_DOOR()
        self.set_mode_AOO()

        # set up menu to choose different pacemaker modes
        pm_modes = Menubutton(self.pmParams, text="Choose Pacing Mode: ", relief = GROOVE)
        pm_modes.menu = Menu(pm_modes, tearoff=0)
        pm_modes["menu"] = pm_modes.menu

        pm_modes.menu.add_command(label="AOO (2)", command=self.set_mode_AOO)
        pm_modes.menu.add_command(label="VOO (1)", command=self.set_mode_VOO)
        pm_modes.menu.add_command(label="AAI (4)", command=self.set_mode_AAI)
        pm_modes.menu.add_command(label="VVI (3)", command=self.set_mode_VVI)
        pm_modes.menu.add_command(label="DOO (5)", command=self.set_mode_DOO)
        pm_modes.menu.add_command(label="AOOR (7)", command=self.set_mode_AOOR)
        pm_modes.menu.add_command(label="VOOR (6)", command=self.set_mode_VOOR)
        pm_modes.menu.add_command(label="AAIR (9)", command=self.set_mode_AAIR)
        pm_modes.menu.add_command(label="VVIR (8)", command=self.set_mode_VVIR)
        pm_modes.menu.add_command(label="DOOR (10)", command=self.set_mode_DOOR)

        pm_modes.grid(row=0, column=0, pady=2, padx = 35)

        Button(self.pmParams, text="E-Gram", command= self.eGram).grid(row=2,column=3, ipadx = 20)

        self.pmParams.grid(row=1, column=0, sticky = W, pady = 5)

	# opens egram window
    def eGram(self):
        self.eGramPg = Toplevel(self.pmParams)
        self.eGramWindow = eGramPage(self.eGramPg, self.serial, self.DCM, self.userName)
        self.DCM.withdraw()
        
    # AOO MODE PARAMETERS
    def set_mode_AOO(self):
        # set up AOO frame inside of pm_params frame
        self.mode_name.config(text="AOO")
        self.AOO_mode = Frame(self.pmParams)

        # forget previous mode frame and set this as new one
        self.mode_frame.grid_forget()
        self.mode_frame = self.AOO_mode
        self.mode_frame.grid(row=1, column=0, columnspan=4)

        # parameters for this mode to be modified
        lrl = StringVar(self.AOO_mode)
        url = StringVar(self.AOO_mode)
        aa = StringVar(self.AOO_mode)
        apw = StringVar(self.AOO_mode)

        Label(self.AOO_mode, text="Lower Rate Limit (ppm): ").grid(row=1, column=0, padx=85, pady=2)
        enter_url = Entry(self.AOO_mode, textvariable=lrl).grid(row=1, column=1)

        Label(self.AOO_mode, text="Upper Rate Limit (ppm): ").grid(row=2, column=0, pady=2)
        enter_url = Entry(self.AOO_mode, textvariable=url).grid(row=2, column=1)

        Label(self.AOO_mode, text="Atrial Amplitude (V): ").grid(row=3, column=0, pady=2)
        enter_aa = Entry(self.AOO_mode, textvariable=aa).grid(row=3, column=1)

        Label(self.AOO_mode, text="Atrial Pulse Width (ms): ").grid(row=4, column=0, pady=2)
        enter_apw = Entry(self.AOO_mode, textvariable=apw).grid(row=4, column=1)

        Button(self.AOO_mode, text="Update", padx=20, pady=10, command= lambda : self.send_AOO(lrl, url, aa, apw)).grid(row=5,column=1,pady=20)

        Label(self.AOO_mode, text="Lower Rate Limit (ppm): ").grid(row=1, column=2, padx=85, pady=2)
        Label(self.AOO_mode, text="Upper Rate Limit (ppm): ").grid(row=2, column=2, padx=85, pady=2)
        Label(self.AOO_mode, text="Atrial Amplitude (V): ").grid(row=3, column=2, padx=85, pady=2)
        Label(self.AOO_mode, text="Atrial Pulse Width (ms): ").grid(row=4, column=2, padx=85, pady=2)
        Button(self.AOO_mode, text="Get Current Settings", padx=20, pady=10, command = self.retrieve_AOOR).grid(row=5, column=3, pady=2)

    def send_AOO(self, lrl, url, aa, apw):
        mode = Mode(self.userName, 2)
        errormsg = ""
        error = False

        # initialize message label
        self.message.destroy()
        self.message = Label(self.AOO_mode)
        self.message.grid()

        # make sure values entered are valid
        try:
            error, errormsg = check_LRL(int(lrl.get()))
            if error == False:
                error, errormsg = check_URL(int(url.get()),int(lrl.get()))
                if error == False:
                    error, errormsg = check_AA(float(aa.get()))
                    if error == False:
                        error, errormsg = check_APW(int(apw.get()))

            if error == False:
                mode.set_LRL(int(lrl.get()))
                mode.set_URL(int(url.get()))
                mode.set_AA(float(aa.get()))
                mode.set_APW(int(apw.get()))
                mode.write_params(self.serial)
                echoFromSim = mode.read_echo(self.serial)

                if (mode.verify_write(echoFromSim)):
                    errormsg = "Data retrieved from pacemaker doesn't match data sent from DCM"

                else:
                    self.message.destroy()
                    self.message = Label(self.AOO_mode, text="Update Success!", font=("Calibri", 25), fg="green")
                    self.message.grid(row=6, columnspan=2, pady=15)

                    Label(self.AOO_mode, text= echoFromSim[2]).grid(row=1, column=3,  pady=2)
                    Label(self.AOO_mode, text= echoFromSim[1]).grid(row=2, column=3,  pady=2)
                    Label(self.AOO_mode, text= round(echoFromSim[6], 2)).grid(row=3, column=3,  pady=2)
                    Label(self.AOO_mode, text= echoFromSim[4]).grid(row=4, column=3,  pady=2)

                
            else:
                self.message.destroy()
                self.message = Label(self.AOO_mode, text=f"Update Failed: \n {errormsg}", font=("Calibri", 15),  fg="red")
                self.message.grid(row=6, columnspan=2, pady=15)

        except Exception as e:
            print(f"EXCEPTION: {e}")
            self.message.destroy()
            self.message = Label(self.AOO_mode, 
                                 text="Update Failed: \nPlease use floats for ventricular amplitude/sensitivity\n"
                                      "Please use integers for all other values\n"
                                      "Make sure you have connected to the UART COM", font=("Calibri", 15), fg="red")
            self.message.grid(row=6, columnspan=2, pady=15)

    def retrieve_AOO(self):
        self.serial.ser.open()
        self.serial.ser.flushInput()
        self.serial.ser.flushOutput()
        packed = struct.pack('<BBBIIBBffffIIIBBBBB',34,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        self.serial.ser.write(packed)
        unpacked = struct.unpack('<BBBIIBBffffIIIBBBBB', packed)
        print(unpacked)

        sleep(1)
        print("In waiting: " + str(self.serial.ser.in_waiting))
        read = self.serial.ser.read(160)
        print(read)
        fromSim = struct.unpack('<BIIBBffffIIIBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', read)
        print(fromSim)

        self.serial.ser.close()

        Label(self.AOO_mode, text= fromSim[2]).grid(row=1, column=3,  pady=2)
        Label(self.AOO_mode, text= fromSim[1]).grid(row=2, column=3,  pady=2)
        Label(self.AOO_mode, text= fromSim[6]).grid(row=3, column=3,  pady=2)
        Label(self.AOO_mode, text= fromSim[4]).grid(row=4, column=3,  pady=2)
        Label(self.AOO_mode, text= "Current Mode number: " + str(fromSim[0])).grid(row=5, column=2,  pady=2)

    # ... [REMOVED REST OF IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]