import machine
import utime

# Initialize GP14 as an input pin
reed_switch = machine.Pin(14, machine.Pin.IN)

while True:
    if reed_switch.value() == 0:
        print("Magnet detected!")
        utime.sleep(1)  # Delay to avoid multiple detections