import board
import analogio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


TMP36_PIN = board.A0  # Analog input connected to TMP36 output.

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16) #0x27 or 0x3f

# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)
desired_temp_min = 69
desired_temp_max = 80

while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a  few seconds before looping again.
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(3.0)
    if temp_F >= desired_temp_min and temp_F <= desired_temp_max:
        lcd.clear()
        lcd.print("Its yummy in my tummy time")
    if temp_F < desired_temp_min:
        lcd.clear()
        lcd.print("Turn the fricken heat on")
    if temp_F > desired_temp_max:
        lcd.clear()
        lcd.print("Turn the fucking Ac on")
    time.sleep(2.0)