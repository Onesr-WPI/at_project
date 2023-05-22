import RPi.GPIO as GPIO
import subprocess


def bash_command(cmd):
	subprocess.Popen(['sudo', '/bin/bash', '-c', cmd])

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("ready to click button")
GPIO.wait_for_edge(18, GPIO.FALLING)
bash_command('/home/kammvaibes/feeding_cycle.sh')
print("running")

GPIO.cleanup()
print("complete")
