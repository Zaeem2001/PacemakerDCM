import serial
from serial.tools.list_ports import comports

class serialcom():

    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ports = list(comports())
        print(self.ports)