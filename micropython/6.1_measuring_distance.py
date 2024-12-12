import machine
import utime

# Define the pins connected to the sensor
TRIG = machine.Pin(17, machine.Pin.OUT)
ECHO = machine.Pin(16, machine.Pin.IN)

def measure_distance():
    # Ensure the trigger pin is low
    TRIG.low()
    utime.sleep_us(2)
    # Send a 10µs pulse to trigger the measurement
    TRIG.high()
    utime.sleep_us(10)
    TRIG.low()

    # Wait for the echo pin to go high (start of echo pulse)
    while ECHO.value() == 0:
        pass
    start_time = utime.ticks_us()

    # Wait for the echo pin to go low (end of echo pulse)
    while ECHO.value() == 1:
        pass
    end_time = utime.ticks_us()

    # Calculate the duration of the echo pulse
    duration = utime.ticks_diff(end_time, start_time)

    # Calculate the distance (speed of sound is 34300 cm/s)
    distance = (duration * 0.0343) / 2
    return distance

while True:
    dist = measure_distance()
    print("Distance: {:.2f} cm".format(dist))
    utime.sleep(0.5)