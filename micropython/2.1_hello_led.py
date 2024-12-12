import machine
import utime
    
led = machine.Pin(15, machine.Pin.OUT)
while True:
    led.value(1)      # Turn the LED on
    utime.sleep(2)    # Wait for 2 second
    led.value(0)      # Turn the LED off
    utime.sleep(2)    # Wait for 2 second