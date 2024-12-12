from machine import I2C, Pin
import utime
from imu import MPU6050

# Initialize I2C interface (I2C0) with SDA on GP4 and SCL on GP5
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Initialize the MPU-6050 sensor
mpu = MPU6050(i2c)

def read_accelerometer():
   """Reads accelerometer data and returns it as a tuple (x, y, z)."""
   accel = mpu.accel
   return accel.x, accel.y, accel.z

def read_gyroscope():
   """Reads gyroscope data and returns it as a tuple (x, y, z)."""
   gyro = mpu.gyro
   return gyro.x, gyro.y, gyro.z

def main():
   """Main loop to read and print sensor data."""
   while True:
      # Read accelerometer data
      ax, ay, az = read_accelerometer()
      print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))

      # Pause for readability
      utime.sleep(0.5)

      # Read gyroscope data
      gx, gy, gz = read_gyroscope()
      print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))

      # Pause before the next set of readings
      utime.sleep(0.5)

# Run the main function
if __name__ == "__main__":
   main()