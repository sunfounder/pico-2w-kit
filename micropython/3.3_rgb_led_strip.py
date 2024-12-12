import machine
from ws2812 import WS2812

# Initialize the LED strip
led_strip = WS2812(machine.Pin(0), 8)  # Using GP0, 8 LEDs

# Set colors for each LED
led_strip[0] = [255, 0, 0]     # Red
led_strip[1] = [0, 255, 0]     # Green
led_strip[2] = [0, 0, 255]     # Blue
led_strip[3] = [255, 255, 0]   # Yellow
led_strip[4] = [0, 255, 255]   # Cyan
led_strip[5] = [255, 0, 255]   # Magenta
led_strip[6] = [255, 255, 255] # White
led_strip[7] = [128, 128, 128] # Gray

# Update the LED strip to show the colors
led_strip.write()