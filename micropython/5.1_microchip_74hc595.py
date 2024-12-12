import machine
import utime

# Define the pins connected to the 74HC595
SDI = machine.Pin(0, machine.Pin.OUT)   # Serial Data Input (DS)
RCLK = machine.Pin(1, machine.Pin.OUT)  # Register Clock (STCP)
SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Register Clock (SHCP)

# Function to send data to 74HC595
def shift_out(data):
    for bit in range(8):
        # Extract the highest bit and send it first
        bit_val = (data & 0x80) >> 7
        SDI.value(bit_val)
        # Pulse the Shift Register Clock
        SRCLK.high()
        utime.sleep_us(1)
        SRCLK.low()
        utime.sleep_us(1)
        # Shift data left by 1 for the next bit
        data = data << 1
    # Pulse the Register Clock to latch the data
    RCLK.high()
    utime.sleep_us(1)
    RCLK.low()
    utime.sleep_us(1)

# Main loop to demonstrate shifting patterns
while True:
    # Light up LEDs one by one from Q0 to Q7
    for i in range(8):
        data = 1 << i
        shift_out(data)
        utime.sleep(0.2)
    # Light up LEDs one by one from Q7 to Q0
    for i in range(7, -1, -1):
        data = 1 << i
        shift_out(data)
        utime.sleep(0.2)
    # Create a moving bar effect
    for i in range(9):
        data = (1 << i) - 1
        shift_out(data)
        utime.sleep(0.2)
    # Turn off all LEDs
    shift_out(0x00)
    utime.sleep(0.5)