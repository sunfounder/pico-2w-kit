import machine
import utime

# Initialize ADC for X and Y axes
x_adc = machine.ADC(27)  # GP27
y_adc = machine.ADC(26)  # GP26

# Initialize digital input for the switch
z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    # Read the analog values (0-65535)
    x_value = x_adc.read_u16()
    y_value = y_adc.read_u16()

    # Read the button state (0 or 1)
    z_state = z_button.value()

    # Print the values
    print("X:", x_value, "Y:", y_value, "Button:", z_state)

    # Small delay to make the output readable
    utime.sleep(0.2)