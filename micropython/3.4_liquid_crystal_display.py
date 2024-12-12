from machine import I2C, Pin
from lcd1602 import LCD
import utime

# Initialize I2C communication (I2C0)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Create an LCD object
lcd = LCD(i2c)

# Display the first message
lcd.clear()
lcd.message("Hello, World!")
utime.sleep(2)

# Move to the second line and display another message
lcd.write(0, 1,"LCD1602 with I2C")  # Column 0, Line 1
utime.sleep(5)

# Clear the display
lcd.clear()