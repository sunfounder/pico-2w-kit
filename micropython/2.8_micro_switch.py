import machine
import utime

# Initialize GP14 as an input pin
switch = machine.Pin(14, machine.Pin.IN)

while True:
    if switch.value() == 1:
        print("The switch is pressed!")
        utime.sleep(0.5)  # Debounce delay