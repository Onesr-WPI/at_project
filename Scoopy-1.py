import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import sys

direction = sys.argv[1]

def set_servo_angle(angle):
    duty_cycle = 2.5 + (angle / 18)
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)  # Allow time for the servo to reach the position

try:
    # Define the pin number for the servo
    servo_pin = 27
    GPIO.setup(servo_pin, GPIO.OUT)
    servo_pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (adjust if needed)
    servo_pwm.start(2)  # Adjust the duty cycle as needed

    if direction == "open":
        set_servo_angle(0)    # Move servo to 0 degrees
        time.sleep(1)         # Pause for 1 second
        servo_pwm.stop()
        GPIO.cleanup()

    elif direction == "close":
        set_servo_angle(180)  # Move servo to 180 degrees
        time.sleep(1)         # Pause for 1 second
        servo_pwm.stop()
        GPIO.cleanup()

    else:
        print("Use either 'open' or 'close' as an argument")
        servo_pwm.stop()
        GPIO.cleanup()
        exit(1)

except:
    print ("\nMotor no work")
