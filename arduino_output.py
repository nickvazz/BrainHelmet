# -*- coding: utf-8 -*-
"""
-Project Steve-
Arduino Import Script

Note: Nueral network noise filtering?
"""
import time
import sys
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
'''
port_list = serial.tools.list_ports.comports()
ard_index = [i for i, s in enumerate(port_list) if 'Arduino' in s]
print port_list
'''

port = '/dev/ttyACM0'
baudrate = 9600
ser = serial.Serial(port , baudrate)
time.sleep(2)

t_end = time.time() + 60 * 0.125 #15min (900s)
'''
while 1:
    sys.stdout.write(ser.readline())
    sys.stdout.flush()
'''
data = []
while time.time() < t_end:
    data.append(ser.readline())

data =  [x.rstrip('\r\n') for x in data]

tmp =[]
for z in data:
    try:
        f = float(z)
        tmp.append(f)
    except:
        pass
print tmp


plt.figure()
plt.plot(range(len(tmp)),tmp)
plt.show()
