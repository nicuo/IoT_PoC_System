#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time

def main ():
    # def main : serial communication, per 2s , count 100, print
    ser = serial.Serial('/dev/ttyACM0', 9600)
    cnt = 0
    while (cnt<100):
        time.sleep(2)
        tmp = ser.readline()
        print tmp
        cnt +=1
    ser.close()

if __name__ == '__main__':
    main()
