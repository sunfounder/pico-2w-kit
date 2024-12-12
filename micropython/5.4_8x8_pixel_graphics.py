import machine
import time

# Define the pins connected to the 74HC595 shift register
sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
rclk = machine.Pin(19, machine.Pin.OUT)  # Storage Register Clock (RCLK)
srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SRCLK)

# Define the glyph data for the letter 'X' with lit pixels and background off
glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

def hc595_in(dat):
    """
    Shifts 8 bits of data into the 74HC595 shift register.
    """
    for bit in range(7, -1, -1):
        srclk.low()
        sdi.value((dat >> bit) & 1)  # Output data bit by bit
        srclk.high()
        time.sleep_us(1)  # Short delay to ensure proper timing

def hc595_out():
    """
    Latches the data from the shift register to the storage register,
    updating the outputs.
    """
    rclk.high()
    rclk.low()

while True:
    for i in range(8):
        hc595_in(glyph[i])       # Send the column data for the current row
        hc595_in(1 << i)         # Activate the current row
        hc595_out()              # Update the display
        time.sleep_ms(1)         # Delay for visual persistence
