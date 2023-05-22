#!/usr/bin/env python3

import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    time.sleep(5)
    ser.write(b'0')
    time.sleep(5)
    ser.write(b'1')
    time.sleep(5)
    ser.write(b'2')
    ser.write(b'0')
    time.sleep(5)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

ser.close()
