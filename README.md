# at_project


This is the code that was written for the STEM 2 Assistive Technology Project at Mass Academy. These programs are used on the Raspberry Pi to communicate to and control each of the motors. For most programs, there is an automatic and manual version.


Arm Extension:

The arm extension system uses a Vex motor that is controlled by an arduino. The Raspberry Pi establishes serial communication with the Arduino, then instructs the Arduino to move the Vex motor in either direction in order to either extend or retract the feeding arm. The relevant programs are:

./arduino_test.py
./arduino_test2.py
./arm-extesnion.py
./arm_extension_manual.py
./vex.py

Height:

Modifying the height of the system is accomplished by communicating to the stepper motor(s) through a WaveShare motor hat, giving as input the number of steps that the motor must turn in each direction. The relevant programs are:

./height_manual.py

Spoon Mechanism:

The spoon is operated by a single servo motor, which is the easiest to control from all of the motors. The angle is given to the motor, and it is adjusted accordingly. The relevant programs are:

./Scoopy-1.py


Taken together, these created the feeding_cycle.sh and feeding_button.py scripts, which allow the user to manually start the entire feeding cycle with the click of the "initiate feeding cycle" button on the wiring diagram in the instructions.




To install to your project, clone the repo and move all files to the root directory. 

Rename all occurences of "kammvaibes" to the name of the user on your Raspberry Pi.

Perform the following commands:

```
sudo mv listen_for_shutdown.sh /etc/init.d/
sudo chmod +x /etc/init.d/listen_for_shutdown.sh

sudo mv listen_for_shutdown.py /usr/local/bin
sudo chmod +x /usr/local/bin/listen_for_shutdown.py

# set up other files

sudo chmod +x feeding_cycle.sh feeding_button.py height_manual.py arduino_test.py Scoop-1.py

sudo listen_for_shutdown.sh start
```

Restart the Raspberry Pi, and if all components are wired correctly, the installation is complete.
