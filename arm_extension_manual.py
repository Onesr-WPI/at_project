import RPi.GPIO as GPIO
import time

# arm-extension.py

in1 = 17
in2 = 15
in3 = 27
in4 = 22

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.001
step_count = 1024 # 5.625*(1/64) per step, 4096 steps is 360°

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

# initializing
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )

motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0

def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()
    
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("ready to click button")

try:
    while True:
            GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            while GPIO.input(26) == 0:
                print("forward")
                for i in range(step_count):
                        for pin in range(0, len(motor_pins)):
                            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
                            # forwards
                        motor_step_counter = (motor_step_counter - 1) % 8
                        time.sleep( step_sleep )
                time.sleep(0.005)

            GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            while GPIO.input(16) == 0:
                print('backward')
                for i in range(step_count):
                        for pin in range(0, len(motor_pins)):
                            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
                            # backwards
                        motor_step_counter = (motor_step_counter + 1) % 8
                        time.sleep( step_sleep )
                time.sleep(0.005)

except KeyboardInterrupt:
        cleanup()
        exit(1)

exit(0)
