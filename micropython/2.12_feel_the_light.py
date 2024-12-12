import machine
import utime

# Initialize ADC on GP28
photoresistor = machine.ADC(28)

while True:
    # Read the analog value (0-65535)
    light_value = photoresistor.read_u16()
    print("Light value:", light_value)
    utime.sleep(0.5)