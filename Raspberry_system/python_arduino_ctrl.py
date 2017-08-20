#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time
import urllib3.request as ur

def main ():
    # def main : serial communication, per 2s , count 100, print
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while (True):
        time.sleep(1)
        tmp = ser.readline()
        print tmp
        ur.urlopen('http://192.168.2.101:8080/input_temp?temp=' + str(temperture))
    ser.close()

if __name__ == '__main__':
    main()
