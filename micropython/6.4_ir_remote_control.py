import time
from machine import Pin
from ir_rx.nec import NEC_8  # Adjust based on your remote's protocol
from ir_rx.print_error import print_error

# Initialize the IR receiver pin
ir_pin = Pin(17, Pin.IN)

# Callback function to handle received data
def ir_callback(data, addr, ctrl):
    if data < 0:  # Repeat code or error
        pass
    else:
        key = decode_key(data)
        print("Received Key:", key)

# Function to decode the received data into key presses
def decode_key(data):
    key_codes = {
        0x45: "POWER",
        0x46: "MODE",
        0x47: "MUTE",
        0x44: "PLAY/PAUSE",
        0x40: "BACKWARD",
        0x43: "FORWARD",
        0x07: "EQ",
        0x15: "-",
        0x09: "+",
        0xD: "U/SD",
        0x16: "0",
        0x19: "cycle",
        0xC: "1",
        0x5E: "3",
        0x18: "2",
        0x8: "4",
        0x1C: "5",
        0x5A: "6",
        0x42: "7",
        0x52: "8",
        0x4A: "9",
        0x0: "ERROR",
        # Add more key codes based on your remote
    }
    return key_codes.get(data, "UNKNOWN")

# Instantiate the IR receiver
ir = NEC_8(ir_pin, ir_callback)
ir.error_function(print_error)  # Optional: to print errors

try:
    while True:
        time.sleep(1)  # Keep the main thread alive
except KeyboardInterrupt:
    ir.close()
    print("Program terminated")