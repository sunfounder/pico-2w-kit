import machine
import utime

# Initialize ADC on GP28
potentiometer = machine.ADC(28)

# Initialize PWM on GP15
led = machine.PWM(machine.Pin(15))
led.freq(1000)  # Set PWM frequency to 1000Hz

while True:
    # Read the analog value (0-65535)
    value = potentiometer.read_u16()
    print("Potentiometer value:", value)

    # Set the LED brightness
    led.duty_u16(value)

    # Small delay to stabilize readings
    utime.sleep_ms(200)