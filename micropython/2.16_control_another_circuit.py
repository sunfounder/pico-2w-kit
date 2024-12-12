import machine
import utime

# Initialize the relay pin on GP15
relay = machine.Pin(15, machine.Pin.OUT)

while True:
    relay.value(1)  # Turn the relay on
    utime.sleep(2)  # Wait for 2 seconds
    relay.value(0)  # Turn the relay off
    utime.sleep(2)  # Wait for 2 seconds