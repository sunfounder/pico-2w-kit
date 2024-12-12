import machine
import utime

# Define motor control pins
motor1A = machine.Pin(14, machine.Pin.OUT)  # Motor control pin 1 configured as an output
motor2A = machine.Pin(15, machine.Pin.OUT)  # Motor control pin 2 configured as an output

# Function to rotate the motor clockwise
def clockwise():
    motor1A.high()  # Set motor1A to HIGH (activates one side of the motor)
    motor2A.low()   # Set motor2A to LOW (deactivates the opposite side of the motor)

# Function to rotate the motor counterclockwise
def anticlockwise():
    motor1A.low()   # Set motor1A to LOW (deactivates one side of the motor)
    motor2A.high()  # Set motor2A to HIGH (activates the opposite side of the motor)

# Function to stop the motor
def stopMotor():
    motor1A.low()   # Set motor1A to LOW
    motor2A.low()   # Set motor2A to LOW

# Infinite loop to alternate motor rotation and stopping
while True:
    clockwise()        # Rotate the motor clockwise
    utime.sleep(1)     # Keep the motor running clockwise for 1 second
    stopMotor()        # Stop the motor
    utime.sleep(1)     # Pause for 1 second
    anticlockwise()    # Rotate the motor counterclockwise
    utime.sleep(1)     # Keep the motor running counterclockwise for 1 second
    stopMotor()        # Stop the motor
    utime.sleep(1)     # Pause for 1 second
