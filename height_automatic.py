import RPi.GPIO as GPIO
import time
from multiprocessing import Process
from DRV8825 import DRV8825
import sys

def turnSingleMotor(motor, direction):
    Motor = motor
    """thread worker function"""
    Motor.SetMicroStep('softward', 'fullstep')
    time.sleep(0.5)
    Motor.TurnStep(Dir=direction, steps=15000, stepdelay = 0.001)
    time.sleep(0.5)
    Motor.Stop()
    return

def down_omar(Motor1, Motor2):
    p1 = Process(target = turnSingleMotor, args=(Motor1, 'forward'))
    p1.start()
    p2 = Process(target = turnSingleMotor, args=(Motor2, 'forward'))
    p2.start()
    p1.join()
    p2.join()
    print("Down Ran")

def up_omar(Motor1, Motor2):
    p1 = Process(target = turnSingleMotor, args=(Motor1, 'backward'))
    p1.start()
    p2 = Process(target = turnSingleMotor, args=(Motor2, 'backward'))
    p2.start()
    p1.join()
    p2.join()
    print("Up Ran")

GPIO.setmode(GPIO.BCM)

try: #motors are 0 and 1
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

    if sys.argv[1] == "up":
           print("going up!")
           # up_omar(Motor1, Motor2)
           turnSingleMotor(Motor1, 'forward')

    elif sys.argv[1] == "down":
           print("going down!")
           # up_omar(Motor1, Motor2)
           turnSingleMotor(Motor1, 'backward')
    else:
           print("use forward or backward as an argument!")
except:
    print ("\nMotor stop")

Motor1.Stop()
Motor2.Stop()
GPIO.cleanup()
exit()

