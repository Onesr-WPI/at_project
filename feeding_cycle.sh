#!/bin/bash

/home/kammvaibes/arduino_test.py backward
python3 /home/kammvaibes/Scoopy-1.py open
python3 /home/kammvaibes/height_automatic.py down
# python3 /home/kammvaibes/Scoopy-1.py open
# /home/kammvaibes/arduino_test.py forward
python3 /home/kammvaibes/Scoopy-1.py close
# /home/kammvaibes/arduino_test.py backward
python3 /home/kammvaibes/height_automatic.py up
/home/kammvaibes/arduino_test.py forward
echo "feeding cycle complete"
