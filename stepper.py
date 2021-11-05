import RPi.GPIO as GPIO
import time
import math

class Stepper:

  def __init__(self, pin1, pin2, pin3, pin4, led):
    self.pins = [pin1, pin2, pin3, pin4]

    self.ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0], [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
    self.cw = self.ccw[:]
    self.cw.reverse() 
    self.angle = 0
    self.led = led

  def goAngle(self, target):
    dir = self.ccw
    if math.sin(self.angle - target) >= 0:
      dir = self.cw
    dist = 512 * abs(self.angle - target) // 360

    for i in range(dist):
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(self.pins[pin], dir[halfstep][pin])
        time.sleep(0.001)
    self.angle = target

  def zero(self):
    GPIO.output(self.led, 1)
    self.goAngle(0)
    GPIO.output(self.led, 0)