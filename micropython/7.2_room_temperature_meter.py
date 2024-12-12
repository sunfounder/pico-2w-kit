from lcd1602 import LCD
from machine import I2C, Pin, ADC
import utime
import math

# Initialize the thermistor (ADC on pin 28)
thermistor = ADC(28)  # Analog input from the thermistor

# Initialize I2C communication for the LCD1602 display
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# Create an LCD object for controlling the LCD1602 display
lcd = LCD(i2c)

# Constants for the Steinhart-Hart equation
BETA = 3950  # Beta coefficient of the thermistor
R0 = 10000   # Resistance at 25 degrees Celsius
T0 = 298.15  # Reference temperature in Kelvin (25°C)

def read_temperature():
    # Read raw ADC value from the thermistor
    adc_value = thermistor.read_u16()

    # Convert the raw ADC value to voltage
    voltage = adc_value * 3.3 / 65535

    # Calculate the resistance of the thermistor
    Rt = (voltage * R0) / (3.3 - voltage)

    # Apply the Steinhart-Hart equation to calculate temperature in Kelvin
    tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

    # Convert temperature from Kelvin to Celsius
    tempC = tempK - 273.15

    return tempC

def main():
    while True:
        temperature = read_temperature()
        # Format the temperature to two decimal places
        temp_str = "{:.2f} C".format(temperature)

        # Display the temperature on the LCD
        lcd.clear()
        lcd.write(0, 0, "Room Temp:")
        lcd.write(4, 1, temp_str)

        # Optional: Print the temperature to the console
        print("Temperature:", temp_str)

        utime.sleep(1)

if __name__ == "__main__":
    main()