#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("ready to click button")

try:
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        state_18 = GPIO.input(18)
        if state_18 == 0:
                print("running")
                subprocess.Popen(["/home/kammvaibes/feeding_cycle.sh"]).wait()
                print("complete")
                state_18 = True


except:
    print ("\nFinished with the feeding cycle button control")
    for i in range(20):
         subprocess.Popen(["sudo", "pkill", "python3"]).wait()
GPIO.cleanup()
exit()
