# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin,PWM
from lib.dcmotor import DCMotor
import time
from lib.servo import Servo
from ultrasonic import HCSR04
in1 = Pin(4, Pin.OUT)
in2 = Pin(5, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(21, Pin.OUT)
enA = PWM(Pin(26), freq=15000)
enB = PWM(Pin(27), freq=15000)

l_motor = DCMotor(in1, in2, enA, 450, 1023)
r_motor = DCMotor(in3, in4, enB, 450, 1023)

r_s = Pin(32, Pin.IN)
r_r_s = Pin(34, Pin.IN)
l_s = Pin(33, Pin.IN)
l_l_s = Pin(23, Pin.IN)
c_s = Pin(35, Pin.IN)


def TurnLeft():
    
    # Make Robot To Go To Left Drive
    r_motor.forward(70)
    l_motor.stop()
    
def TurnRight():

    # Make Robot To Go To Right Drive
    l_motor.forward(70)
    r_motor.stop()
    
def TurnForward():
    # Make Robot To Go To Forward
    l_motor.forward(70)
    r_motor.forward(70)

def TurnStop():
    # Make Robot To Stop From Motion		+
    l_motor.stop()
    r_motor.stop()


while True:

    if (r_s.value() == 1 and l_s.value() == 1 and c_s.value() == 0 and l_l_s.value() == 1 and r_r_s.value() == 1):
        
            TurnForward()
    elif (r_s.value() == 1 and l_s.value() == 0 and c_s.value() == 1 and l_l_s.value() == 1 and r_r_s.value() == 1):
            TurnLeft()
    elif (l_s.value() == 1 and r_s.value() == 0 and c_s.value() == 1 and l_l_s.value() == 1 and r_r_s.value() == 1):
            TurnRight()
    elif (l_l_s.value() == 0 and c_s.value() == 1 and r_s.value() == 1 and l_s.value() == 1 and r_r_s.value() == 1):
            TurnLeft()
    elif (r_r_s.value() == 0 and c_s.value() == 1 and r_s.value() == 1 and l_s.value() == 1 and l_l_s.value() == 1):
            TurnRight()
    elif (l_s.value() == 0 and c_s.value() == 0 and l_l_s.value() == 1 and r_s.value() == 1 and r_r_s.value() == 1):
            TurnLeft()
    elif (l_s.value() == 0 and c_s.value() == 0 and l_l_s.value() == 0 and r_s.value() == 1 and r_r_s.value() == 1):
        TurnLeft()
    elif (r_s.value() == 0 and c_s.value() == 0  and l_s.value() == 1 and l_l_s.value() == 1 and r_r_s.value() == 1):
          TurnRight()
    elif (r_s.value() == 0 and c_s.value() == 0 and r_r_s.value() == 0 and l_s.value() == 1 and l_l_s.value() == 1):
        TurnRight()
    elif (r_s.value() == 0 and l_s.value() == 0 and  r_r_s.value() == 0 and l_l_s.value() == 0 and c_s.value() == 0):
        TurnStop()
        time.sleep(2)
        TurnForward()

        
   
        
    time.sleep(0.000000001)






