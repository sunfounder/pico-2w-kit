from imu import MPU6050
from machine import I2C, Pin, PWM
import utime
import math

# Initialize I2C communication for MPU6050
i2c = I2C(1, scl=Pin(7), sda=Pin(6))
mpu = MPU6050(i2c)

# Initialize PWM for the servo motor on GP15
servo = PWM(Pin(15))
servo.freq(50)  # Set frequency to 50Hz for servo

# Function to map angle to PWM duty cycle
def angle_to_duty(angle):
    # Convert angle (0-180) to duty cycle (0.5ms - 2.5ms pulse width)
    # Duty cycle range is from 2% to 12% for 0.5ms to 2.5ms at 50Hz
    duty_cycle = (angle / 18) + 2
    duty_u16 = int(duty_cycle / 100 * 65535)
    return duty_u16

# Function to get the tilt angle from accelerometer data
def get_tilt_angle():
    accel = mpu.accel
    x = accel.x
    y = accel.y
    z = accel.z
    angle = math.atan2(y, z) * (180 / math.pi)
    return angle + 90  # Adjust angle to range from 0 to 180

# Main loop
try:
    while True:
        angle = get_tilt_angle()
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180
        duty = angle_to_duty(angle)
        servo.duty_u16(duty)
        utime.sleep(0.1)
except KeyboardInterrupt:
    servo.deinit()
    print("Program stopped.")