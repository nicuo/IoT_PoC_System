#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time
from urllib import urlopen

def main ():
    # def main : serial communication, per 1s
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while (True):
        time.sleep(1)
        temp = ser.readline()
        print temp
        respose = urlopen('http://192.168.2.101:8080/input_temp?temp=' + str(temp))
        data = response.read()
        print (data)
    ser.close()

if __name__ == '__main__':
    main()
