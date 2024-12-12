import machine
import utime

# Initialize the buzzer pin (GP15)
buzzer = machine.Pin(15, machine.Pin.OUT)

while True:
    # Loop to beep the buzzer 4 times
    for i in range(4):
        buzzer.value(1)  # Turn the buzzer on
        utime.sleep(0.3)  # Wait for 0.3 seconds
        buzzer.value(0)  # Turn the buzzer off
        utime.sleep(0.3)  # Wait for 0.3 seconds
    utime.sleep(1)  # Longer pause before the next cycle