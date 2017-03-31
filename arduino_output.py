# -*- coding: utf-8 -*-
"""
-Project Steve-
Arduino Import Script
"""
import time
import sys
import serial
import serial.tools.list_ports
'''
port_list = serial.tools.list_ports.comports()
ard_index = [i for i, s in enumerate(port_list) if 'Arduino' in s]
print port_list
'''

port = '/dev/ttyACM0'
baudrate = 9600
ser = serial.Serial(port , baudrate)

while 1:
    sys.stdout.write(ser.readline())
    sys.stdout.flush()
