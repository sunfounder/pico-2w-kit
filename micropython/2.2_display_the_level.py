import machine
import utime

# Define the GPIO pins connected to the LEDs
pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
leds = []

# Initialize each pin as an output and store it in the leds list
for pin_number in pins:
    led = machine.Pin(pin_number, machine.Pin.OUT)
    leds.append(led)

while True:
    # Turn on LEDs one by one to simulate increasing level
    for led in leds:
        led.value(1)  # Turn the LED on
        utime.sleep(0.2)
    # Turn off LEDs one by one to simulate decreasing level
    for led in leds:
        led.value(0)  # Turn the LED off
        utime.sleep(0.2)