from mpr121 import MPR121
from machine import Pin, I2C
import utime

i2c = I2C(0, sda=Pin(4), scl=Pin(5))
mpr = MPR121(i2c)

# check all keys
while True:
    value = mpr.get_all_states()
    if len(value) != 0:
        print(value)
    utime.sleep_ms(100)