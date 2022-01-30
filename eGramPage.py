import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import serial
import struct
import numpy as np
from time import sleep
from tkinter import *

class eGramPage:

    def __init__(self, parent, *args, **kwargs):
        eGram = parent
		eGram.title("Egram")
        eGram.geometry("130x160")
        serial = args[0]
        DCM = args[1]
        username = args[2]

        Button(eGram, text="Ventrical ECG", command = self.VEcg).grid(row=1, column=1, pady = 5, ipadx = 15,)
        Button(eGram, text="Atrial ECG", command = self.AEcg).grid(row=2, column=1, pady = 5, ipadx = 20)
        Button(eGram, text="Atrial & Ventrical ECG", command = self.AVEcg).grid(row=3, column=1, pady = 5)
        Button(eGram, text="Return", command = self.backToPm).grid(row=4, column=1, pady = 5)


	# ATRIAL
    def AEcg(self):
        x_len = 200         # Number of points to display
        y_range = [0, 0.7]  # Range of possible Y values to display

        # create figure for plotting [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

        # create a blank line. We will update the line in animate
        line, = ax.plot(xs, ys, color = "r")

        # add labels
        plt.title('Atrial Electrogram')
        plt.xlabel('Samples (Every 20 ms)')
        plt.ylabel('Voltage (V)')

		# get pacemaker data
        self.serial.ser.open()
        sleep(1)
        self.serial.ser.flushInput()
        self.serial.ser.flushOutput()
        self.serial.ser.read_all()
		
        print("ser: " + str(self.serial.ser.in_waiting))

        print("connected to: " + self.serial.ser.portstr)
        print()

        print("ser: " + str(self.serial.ser.in_waiting))
        packed = struct.pack(...) # [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
        self.serial.ser.write(packed)
        print("ser: " + str(self.serial.ser.in_waiting))
        print("opened")
        sleep(0.05)

	# This function is called periodically from FuncAnimation
	def animate(i, ys):

		print("ser: " + str(self.serial.ser.in_waiting))
		read = self.serial.ser.read(160)
		fromSim = struct.unpack(...) # [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
		print()
		
		# Add y to list
		ys.append(sum(fromSim[21:41])/20)

		# Limit y list to set number of items
		ys = ys[-x_len:]

		# Update line with new Y values
		line.set_ydata(ys)

		return line,

        # Set up plot to call animate() function periodically
        ani = animation.FuncAnimation(...) # [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
        plt.tight_layout()
        plt.show()

        self.serial.ser.read_all()
        self.serial.ser.flushInput()
        self.serial.ser.flushOutput()
        packed = struct.pack(...) # [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
        self.serial.ser.write(packed)
        self.serial.ser.close()
	
	# VENTRICULAR
    def VEcg(self):
        x_len = 200         # Number of points to display
        y_range = [0, 0.7]  # Range of possible Y values to display

        # Create figure for plotting [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

        # Create a blank line. We will update the line in animate
        line, = ax.plot(xs, ys, color = "b")

        # Add labels
        plt.title('Ventrical Electrogram')
        plt.xlabel('Samples (Every 20 ms)')
        plt.ylabel('Voltage (V)')

        self.serial.ser.open()
        sleep(1)

        self.serial.ser.flushInput()
        self.serial.ser.flushOutput()
        self.serial.ser.read_all()
        print("ser: " + str(self.serial.ser.in_waiting))

        print("connected to: " + self.serial.ser.portstr)
        print()

        print("ser: " + str(self.serial.ser.in_waiting))
        packed = struct.pack('<BBBIIBBffffIIIBBBBB',34,14,1,1,1,1,1,1.0,1.0,1.0,1.0,1,1,1,1,1,1,1,1)
        self.serial.ser.write(packed)
        print("ser: " + str(self.serial.ser.in_waiting))
        print("opened")
        sleep(0.05)

	# ATRIAL + VENTRICULAR
    def AVEcg(self):
        x_len = 200         # Number of points to display
        y_range = [0, 0.7]  # Range of possible Y values to display

        # Create figure for plotting [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
		
        # Create a blank line. We will update the line in animate
        line1, = ax.plot(xs, ys, color = "b", label = "Ventrical Sigal")
        line2, = ax.plot(xs, ys2, color = "r", label = "Atrial Sigal")

        # Add labels
        plt.title('Atrial and Ventrical Electrogram')
        plt.xlabel('Samples (Every 20 ms)')
        plt.ylabel('Analog Voltage')

        self.serial.ser.open()
        sleep(1)

        self.serial.ser.flushInput()
        self.serial.ser.flushOutput()
        self.serial.ser.read_all()
        print("ser: " + str(self.serial.ser.in_waiting))

        print("connected to: " + self.serial.ser.portstr)
        print()

        print("ser: " + str(self.serial.ser.in_waiting))
        packed = struct.pack('<BBBIIBBffffIIIBBBBB',34,14,1,1,1,1,1,1.0,1.0,1.0,1.0,1,1,1,1,1,1,1,1)
        self.serial.ser.write(packed)
        print("ser: " + str(self.serial.ser.in_waiting))
        print("opened")
        sleep(0.05)
    
    def backToPm(self):
        self.DCM.deiconify()
        self.eGram.destroy()

