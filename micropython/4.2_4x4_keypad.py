import machine
import time

# Define the characters on the keypad
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Define the GPIO pins connected to the rows and columns
row_pins = [2, 3, 4, 5]   # GP2-GP5
col_pins = [6, 7, 8, 9]   # GP6-GP9

# Initialize row pins as outputs
rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

# Initialize column pins as inputs with pull-down resistors
cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

def scan_keypad():
    for i, row in enumerate(rows):
        # Set all rows low
        for r in rows:
            r.value(0)
        # Set the current row high
        row.value(1)
        # Check columns for a high signal
        for j, col in enumerate(cols):
            if col.value() == 1:
                # Key detected
                return keys[i][j]
    return None

last_key = None

while True:
    key = scan_keypad()
    if key != last_key:
        if key is not None:
            print("Key pressed:", key)
        last_key = key
    time.sleep(0.1)