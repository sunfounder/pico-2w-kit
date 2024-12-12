import machine
import utime

# Initialize PWM on pin GP15
servo = machine.PWM(machine.Pin(15))
servo.freq(50)  # Set the frequency to 50Hz

# Function to map angle to duty cycle
def angle_to_duty(angle):
    min_duty = 1638  # Corresponds to 0.5ms pulse (0°)
    max_duty = 8192  # Corresponds to 2.5ms pulse (180°)
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    return duty

while True:
    # Move servo from 0° to 180°
    for angle in range(0, 181, 1):
        servo.duty_u16(angle_to_duty(angle))
        utime.sleep_ms(20)
    # Move servo from 180° back to 0°
    for angle in range(180, -1, -1):
        servo.duty_u16(angle_to_duty(angle))
        utime.sleep_ms(20)