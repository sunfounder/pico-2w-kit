import machine
import utime
import math

# Constants
BETA = 3950  # Beta coefficient of the thermistor
T0 = 298.15  # Reference temperature (25°C in Kelvin)
R0 = 10000   # Resistance at T0 (10 kΩ)

# Initialize ADC on GP28
thermistor = machine.ADC(28)

while True:
    # Read the analog value (0-65535)
    analog_value = thermistor.read_u16()

    # Convert analog value to voltage
    voltage = analog_value * 3.3 / 65535

    # Calculate thermistor resistance
    Rt = (voltage * R0) / (3.3 - voltage)

    # Calculate temperature in Kelvin using the Beta formula
    tempK = 1 / ( (1 / T0) + (1 / BETA) * math.log(Rt / R0) )

    # Convert Kelvin to Celsius
    tempC = tempK - 273.15

    # Convert Celsius to Fahrenheit
    tempF = tempC * 9 / 5 + 32

    # Print the results
    print('Temperature: {:.2f}°C  {:.2f}°F'.format(tempC, tempF))

    # Wait before the next reading
    utime.sleep(2)