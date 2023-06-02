
import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo
from lib.PID import PID

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D7)

# Assume we have a system we want to control in controlled_system
# this will be our sensor value to be used as input for the PID controller
# v = controlled_system.update(0)
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
# start angle 180 degrees
my_servo.angle = 180
time.sleep(.5)
# then change  start angle to 45 degreese
my_servo.angle = 60
time.sleep(.5)
setpoint= 17.5

pid = PID(8, 10, 0.05, setpoint=setpoint)
pid.output_limits = (0, 180)
# my_servo.angle = 180
# print("angle: ",x180) 
# time.sleep(10)
while True:
        dist = sonar.distance
        output = pid(dist)
        
        
    # # Feed the PID output to the system and get its current value
   
        if dist < 5 or dist > 35:
            output = 175
            time.sleep(0.1)            
        
        print('dist: ', dist, 'PID Output: ', output)
        p,i,d = pid.components
        print(p, i, d)
        my_servo.angle = (180-output)
        time.sleep(0.1)