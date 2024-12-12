import machine
import utime

# Initialize GP14 as an input pin
tilt_switch = machine.Pin(14, machine.Pin.IN)

while True:
    if tilt_switch.value() == 0:
        print("Tilt detected!")
        utime.sleep(1)  # Delay to avoid multiple rapid detections