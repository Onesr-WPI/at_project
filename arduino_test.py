#!/usr/bin/env python3

import serial
import time
import sys

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    time.sleep(2)
    print(sys.argv[1])
    if sys.argv[1] == "forward":
        ser.write(b'1')
    if sys.argv[1] == "backward":
        ser.write(b'0')
    # ser.write(b'0')
    time.sleep(5)
    # ser.write(b'1')
    # time.sleep(15)
    # ser.write(b'0')
    # time.sleep(8)
    #while True:
     #   if ser.in_waiting > 0:
      #      line = ser.readline().decode('utf-8').rstrip()
       #     print(line)

ser.close()
