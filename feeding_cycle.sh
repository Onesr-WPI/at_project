#!/bin/bash

sudo python3 /home/kammvaibes/arm-extension.py backward
sudo python3 /home/kammvaibes/Stepper_Motor_HAT_V2_Code/Raspberry\ PI/python/multi_process_steppers.py down
sudo python3 /home/kammvaibes/Scoopy-1.py open
sudo python3 /home/kammvaibes/arm-extension.py forward
sudo python3 /home/kammvaibes/Scoopy-1.py close
sudo python3 /home/kammvaibes/arm-extension.py backward
sudo python3 /home/kammvaibes/Stepper_Motor_HAT_V2_Code/Raspberry\ PI/python/multi_process_steppers.py up
sudo python3 /home/kammvaibes/arm-extension.py forward
echo "feeding cycle complete"
