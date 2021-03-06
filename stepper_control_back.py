#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import stepper

ledPin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)

pins = [18,23,24,25]
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

motor = stepper.Stepper(pins[0], pins[1], pins[2], pins[3], ledPin)

print("start")
while True:
  with open("/home/pi/cgi/stepper_control.txt", 'r') as f:  
    values = f.read().split()
    print(values)
    target = int(values[0])
    change = str(values[1])
    zero = str(values[2])

    if zero == "Zero" and change == "None":
      motor.zero()
    if zero == "None" and change == "Change":
      motor.goAngle(target)
    time.sleep(0.1)

GPIO.cleanup() 
