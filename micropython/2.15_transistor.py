import machine

# Initialize the button and signal pins
button = machine.Pin(14, machine.Pin.IN)
signal = machine.Pin(15, machine.Pin.OUT)

while True:
    button_status = button.value()
    if button_status == 1:
        signal.value(1)  # Send high signal to the transistor
    else:
        signal.value(0)  # Send low signal to the transistor