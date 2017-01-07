#
# Using Python 3.3 and pySerial for serial communications.
#
# I'm trying to write a command to my COM PORT but the write method won't take my string. (Most of the code is from here Full examples of using Pyserial package
#
# What's going on?

import time
import serial


ser = serial.Serial(
    port='\\\\.\\COM8',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()

ser.write("C0 25 00 00 C0".encode())
out = ''
# let's wait one second before reading output (let's give device time to answer)
time.sleep(5)
while ser.inWaiting() > 0:
    out += ser.read(40)

if out != '':
    print(">>" + out)


ser.close()
