import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

servo_pin = 2
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, 500)

servo_pwm.start(1)

time.sleep(0.5)

servo_pwm.ChangeDutyCycle(5)

time.sleep(0.5)

servo_pwm.ChangeDutyCycle(25)

time.sleep(0.5)

servo_pwm.ChangeDutyCycle(100)

time.sleep(0.5)

servo_pwm.stop()

GPIO.cleanup()
