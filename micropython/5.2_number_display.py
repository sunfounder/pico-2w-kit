import machine
import utime

# Define the binary codes for each digit (0-9)
SEGMENT_CODES = [
    0x3F,  # 0
    0x06,  # 1
    0x5B,  # 2
    0x4F,  # 3
    0x66,  # 4
    0x6D,  # 5
    0x7D,  # 6
    0x07,  # 7
    0x7F,  # 8
    0x6F   # 9
]

# Initialize the control pins for 74HC595
SDI = machine.Pin(0, machine.Pin.OUT)   # Serial Data Input (DS)
RCLK = machine.Pin(1, machine.Pin.OUT)  # Register Clock (STCP)
SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Register Clock (SHCP)

# Function to send data to 74HC595
def shift_out(data):
    RCLK.low()
    for bit in range(7, -1, -1):
        SRCLK.low()
        bit_val = (data >> bit) & 0x01
        SDI.value(bit_val)
        SRCLK.high()
    RCLK.high()

# Main loop to display numbers 0-9
while True:
    for num in range(10):
        shift_out(SEGMENT_CODES[num])
        utime.sleep(0.5)