from machine import Pin
import utime

# Initialize the control pins for 74HC595
SDI = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input (DS)
RCLK = machine.Pin(19, machine.Pin.OUT)  # Register Clock (STCP)
SRCLK = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SHCP)

# 7-segment display segment codes for digits 0-9 (common cathode)
SEGMENT_CODES = [0x3F,  # 0
                0x06,  # 1
                0x5B,  # 2
                0x4F,  # 3
                0x66,  # 4
                0x6D,  # 5
                0x7D,  # 6
                0x07,  # 7
                0x7F,  # 8
                0x6F]  # 9

# Initialize digit select pins (common cathodes)
digit_pins = [
    machine.Pin(10, machine.Pin.OUT),  # Digit 1
    machine.Pin(11, machine.Pin.OUT),  # Digit 2
    machine.Pin(12, machine.Pin.OUT),  # Digit 3
    machine.Pin(13, machine.Pin.OUT)   # Digit 4
]


# Initialize the tilt switch
tilt_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Variables for timing
start_time = 0
elapsed_time = 0
counting = False

# Function to shift out data to the shift registers
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

# Function to display the elapsed time
def display_time(time_ms):
    # Convert time to centiseconds (hundredths of a second)
    centiseconds = int(time_ms / 10)
    # Limit to 9999 to fit the display
    if centiseconds > 9999:
        centiseconds = 9999

    # Extract individual digits
    digits = [
        (centiseconds // 1000) % 10,
        (centiseconds // 100) % 10,
        (centiseconds // 10) % 10,
        centiseconds % 10
    ]
    # Display each digit rapidly
    for i in range(4):
        display_digit(i, digits[i])

# Interrupt handler for the tilt switch
def tilt_handler(pin):
    global counting, start_time, elapsed_time
    if not counting:
        # Start counting
        counting = True
        start_time = utime.ticks_ms()
    else:
        # Stop counting
        counting = False
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

# Set up tilt switch interrupt
tilt_switch.irq(trigger=Pin.IRQ_RISING, handler=tilt_handler)

# Main loop
while True:
    if counting:
        # Calculate elapsed time
        current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
        display_time(current_time)
    else:
        # Display the final time
        display_time(elapsed_time)