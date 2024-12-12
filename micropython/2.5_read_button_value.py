import machine
import utime

# Initialize GP14 as an input pin
button = machine.Pin(14, machine.Pin.IN)

while True:
    if button.value() == 1:
        print("Button pressed!")
        utime.sleep(0.2)  # Debounce delay