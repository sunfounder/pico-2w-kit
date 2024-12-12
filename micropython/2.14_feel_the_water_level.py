import machine
import utime

# Initialize ADC on GP28
sensor = machine.ADC(28)

while True:
    # Read the analog value from the sensor
    value = sensor.read_u16()
    print("Water level reading:", value)
    utime.sleep(0.2)  # Delay to avoid flooding the console with data