from machine import Pin
import utime
import dht

# Initialize the DHT11 sensor
sensor = dht.DHT11(Pin(16))

while True:
   try:
      # Trigger measurement
      sensor.measure()
      # Read values
      temperature = sensor.temperature  # In Celsius
      humidity = sensor.humidity        # In Percent
      # Print values
      print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
   except OSError as e:
      print("Failed to read sensor.")
   # Wait before the next reading
   utime.sleep(2)