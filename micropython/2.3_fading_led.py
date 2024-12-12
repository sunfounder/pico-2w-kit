import machine
import utime

# Set up PWM on pin GP15
led = machine.PWM(machine.Pin(15))
led.freq(1000)  # Set frequency to 1000Hz

# Gradually increase brightness
for duty in range(0, 65536, 64):
    led.duty_u16(duty)  # Set duty cycle (16-bit value)
    utime.sleep(0.01)   # Wait 10ms

# Turn off the LED
led.duty_u16(0)