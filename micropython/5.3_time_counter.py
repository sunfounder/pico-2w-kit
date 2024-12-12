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
SDI = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input (DS)
RCLK = machine.Pin(19, machine.Pin.OUT)  # Register Clock (STCP)
SRCLK = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SHCP)

# Initialize digit select pins (common cathodes)
digit_pins = [
    machine.Pin(10, machine.Pin.OUT),  # Digit 1
    machine.Pin(11, machine.Pin.OUT),  # Digit 2
    machine.Pin(12, machine.Pin.OUT),  # Digit 3
    machine.Pin(13, machine.Pin.OUT)   # Digit 4
]

# Function to send data to 74HC595
def shift_out(data):
    RCLK.low()
    for bit in range(7, -1, -1):
        SRCLK.low()
        bit_val = (data >> bit) & 0x01
        SDI.value(bit_val)
        SRCLK.high()
    RCLK.high()

# Function to display a digit at a specific position
def display_digit(position, digit):
    # Turn off all digits
    for dp in digit_pins:
        dp.high()
    # Send segment data
    shift_out(SEGMENT_CODES[digit])
    # Activate the selected digit (common cathode is active low)
    digit_pins[position].low()
    # Small delay to allow the digit to be visible
    utime.sleep_ms(5)
    # Turn off the digit
    digit_pins[position].high()

# Function to display a number on the 4-digit display
def display_number(number):
    # Extract individual digits
    digits = [
        (number // 1000) % 10,
        (number // 100) % 10,
        (number // 10) % 10,
        number % 10
    ]
    # Display each digit rapidly
    for i in range(4):
        display_digit(i, digits[i])

# Main loop
counter = 0
last_update = utime.ticks_ms()

while True:
    # Update the counter every 1000 ms (1 second)
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, last_update) >= 1000:
        counter += 1
        if counter > 9999:
            counter = 0
        last_update = current_time

    # Continuously refresh the display
    display_number(counter)