import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

btn = DigitalInOut(board.D12)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

# create a PWMOut object on Pin A8.
pwm = pwmio.PWMOut(board.D8, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)


while True:
    if not btn.value:
      for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
        print("BTN is down")
    else:
        print("BTN is up")
        pass

    time.sleep(0.1) # sleep for debounce

    if not btn2.value:
      for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
          my_servo.angle = angle
          time.sleep(0.05)
      print("BTN2 is down")
    else:
        print("BTN2 is up")
        pass

    time.sleep(0.1) # sleep for debounce






while True:
    
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)