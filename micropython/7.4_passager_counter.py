from machine import Pin
import utime

# Define the PIR sensor pin
pir_sensor = Pin(16, Pin.IN)

# Initialize the counter
count = 0

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

# Interrupt handler for PIR sensor
def pir_handler(pin):
    global count
    count += 1
    if count > 9999:
        count = 0

# Set up PIR sensor interrupt
pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

# Main loop
while True:
    # Continuously refresh the display
    display_number(count)