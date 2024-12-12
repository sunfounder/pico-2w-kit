import machine
import utime

# Initialize PWM for red, green, and blue pins
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

# Set the PWM frequency
red.freq(1000)
green.freq(1000)
blue.freq(1000)

def map_value(x, in_min, in_max, out_min, out_max):
    # Map a value from one range to another
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def set_color(r, g, b):
    # Set the color by adjusting duty cycles
    red.duty_u16(map_value(r, 0, 255, 0, 65535))
    green.duty_u16(map_value(g, 0, 255, 0, 65535))
    blue.duty_u16(map_value(b, 0, 255, 0, 65535))

# Example: Set the color to orange
set_color(255, 165, 0)