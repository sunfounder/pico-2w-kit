from mpr121 import MPR121
from machine import Pin, I2C, PWM
import time
import urandom

# Initialize I2C connection for MPR121 capacitive touch sensor
i2c = I2C(1, sda=Pin(6), scl=Pin(7))
mpr = MPR121(i2c)

# Define note frequencies (in Hertz)
NOTE_FREQUENCIES = [
    220,  # A3
    247,  # B3
    262,  # C4
    294,  # D4
    330,  # E4
    349,  # F4
    392,  # G4
    440,  # A4
    494,  # B4
    523,  # C5
    587,  # D5
    659   # E5
]

# Initialize PWM for buzzer on GP15
buzzer = PWM(Pin(15))

# Initialize PWM for RGB LED on GP13 (Red), GP12 (Green), GP11 (Blue)
red = PWM(Pin(13))
green = PWM(Pin(12))
blue = PWM(Pin(11))

# Set PWM frequency for LEDs
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Function to play a tone
def play_tone(frequency):
    if frequency == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)  # 50% duty cycle

# Function to stop the tone
def stop_tone():
    buzzer.duty_u16(0)

# Function to set a random color on the RGB LED
def set_random_color():
    red.duty_u16(urandom.getrandbits(16))
    green.duty_u16(urandom.getrandbits(16))
    blue.duty_u16(urandom.getrandbits(16))

# Function to turn off the RGB LED
def turn_off_led():
    red.duty_u16(0)
    green.duty_u16(0)
    blue.duty_u16(0)

# Main loop
try:
    last_touched = mpr.touched()
    while True:
        current_touched = mpr.touched()
        for i in range(12):
            pin_bit = 1 << i
            if current_touched & pin_bit and not last_touched & pin_bit:
                # Electrode i was just touched
                print("Pin {} touched".format(i))
                play_tone(NOTE_FREQUENCIES[i])
                set_random_color()
            if not current_touched & pin_bit and last_touched & pin_bit:
                # Electrode i was just released
                print("Pin {} released".format(i))
                stop_tone()
                turn_off_led()
        last_touched = current_touched
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
finally:
    stop_tone()
    turn_off_led()