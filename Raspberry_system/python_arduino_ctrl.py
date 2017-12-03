#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time
from urllib import urlopen

def test_temp():
    return 26.50

def main ():
    # def main : serial communication, per 1s
    ser = serial.Serial('/dev/ttyACM0', 9600)
    try:
        while (True):
            time.sleep(1)
            temp = ser.readline()
            #temp = test_temp()
            print('temerature: {}'.format(temp).rstrip())
            response = urlopen('http://192.168.2.103:8080/input_temp?device_id=1&temperature='+ str(temp))
            data = response.read()
            print('response: {}'.format(data))

    except KeyboardInterrupt:
        ser.close()
        print("\nGood bye")

if __name__ == '__main__':
    main()
