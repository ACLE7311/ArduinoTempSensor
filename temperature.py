""" Temperature read from Arduino serial
The page I referred to for this was actually a "send email when there
is movement" type thing : https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector/python-code
"""


import serial
import time
import sys

print "Here we go"
ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout = 60)


while 1:
    sys.stdout.write(ser.readline())
    sys.stdout.flush()
    # print(temp)
    # time.sleep(1)

print "thats all she wrote"
