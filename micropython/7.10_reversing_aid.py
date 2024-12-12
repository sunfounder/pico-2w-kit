import machine
import utime

# Set up pins
trigger = machine.Pin(17, machine.Pin.OUT)
echo = machine.Pin(16, machine.Pin.IN)
buzzer = machine.Pin(15, machine.Pin.OUT)
led = machine.Pin(14, machine.Pin.OUT)

# Function to measure distance
def measure_distance():
    # Ensure trigger is low
    trigger.low()
    utime.sleep_us(2)
    # Send 10us pulse to trigger
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    # Measure the duration of the echo pulse
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()

    timepassed = utime.ticks_diff(signalon, signaloff)
    distance = (timepassed * 0.0343) / 2  # Convert to cm
    return distance

# Function to control buzzer and LED
def alert(interval):
    buzzer.high()
    led.high()
    utime.sleep(0.1)
    buzzer.low()
    led.low()
    utime.sleep(interval)

# Main loop
try:
    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        if dist < 0:
            print("Out of range")
            utime.sleep(1)
        elif dist <= 10:
            alert(0.2)  # Very close, alert rapidly
        elif dist <= 20:
            alert(0.5)  # Close, alert moderately
        elif dist <= 50:
            alert(1)    # Not too close, alert slowly
        else:
            alert(2)    # Far away, alert infrequently
except KeyboardInterrupt:
    print("Measurement stopped by User")