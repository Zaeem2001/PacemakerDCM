from serialcom import*
import serial
import struct

from time import sleep


	def write_params_to_file(self, serial, mode):
		# save data stored in file so that it can be written back in after new data is written
        file = open(self.choose_data_file(mode), "r")
        data = file.readlines()
        file.close()

        old_data = []

        # keep other patients' data stored while ignoring current patient's (old) data [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

        # write other patients' data back to file and append new data for current patient [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]

	def write_params_to_pacemaker(self, serial, mode):
        # open serial port for writing data to pacemaker
        serial.ser.open()
        serial.ser.flushInput()
        serial.ser.read_all()   
        serial.ser.flushOutput()    
        self.packed = struct.pack(...)	# [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
        serial.ser.write(self.packed)
    
    def read_echo(self, serial):
        sleep(1.3)
        print("In waiting: " + str(serial.ser.in_waiting))
        read = serial.ser.read(160)
        print(read)
        fromSim = struct.unpack(...) # [REMOVED IMPLEMENTATION FOR ACADEMIC DISHONESTY PURPOSES]
        print(fromSim)

        serial.ser.flushInput()
        serial.ser.read_all()
        serial.ser.flushOutput()
        serial.ser.close()

        return fromSim

    def verify_write(self, echo, mode):
        if (mode != echo[0]):
            return False
        else:
            i = 0 # used to index through echo
            for param in self.paramList:
                if (round(param, 2) != round(echo[i], 2)):
                    return False
                else:
                    i = i + 1

        return True
	
	def choose_data_file(self, mode):
        if (mode == 1):
            return "voo_data.txt"
        elif (mode == 2):
            return "aoo_data.txt"
        elif (mode == 3):
            return "vvi_data.txt"
        elif (mode == 4):
            return "aai_data.txt"
        elif (mode == 5):
            return "doo_data.txt"
        elif (mode == 6):
            return "voor_data.txt"
        elif (mode == 7):
            return "aoor_data.txt"
        elif (mode == 8):
            return "vvir_data.txt"
        elif (mode == 9):
            return "aair_data.txt"
        elif (mode == 10):
            return "door_data.txt"
        else:
            return "ERROR! MODE DOESN'T EXIST!"     # this shouldn't be possible, but if the program
                                                    # ever reaches this point the error is traceable