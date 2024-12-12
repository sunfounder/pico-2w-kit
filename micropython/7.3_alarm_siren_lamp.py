import machine
import utime

# Initialize PWM for buzzer and LED
buzzer = machine.PWM(machine.Pin(15))
led = machine.PWM(machine.Pin(16))
led.freq(1000)  # Set LED PWM frequency

# Initialize the slide switch
switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Function to map values from one range to another
def interval_mapping(x, in_min, in_max, out_min, out_max):
    # Ensure in_min != in_max to avoid division by zero
    if in_max - in_min == 0:
        return out_min
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Main loop
try:
    while True:
        if switch.value() == 1:
            # Alarm is ON
            # Increase frequency and brightness
            for i in range(0, 100, 2):
                # Map 'i' to LED brightness and buzzer frequency
                brightness = interval_mapping(i, 0, 100, 0, 65535)
                frequency = interval_mapping(i, 0, 100, 500, 2000)

                # Set LED brightness
                led.duty_u16(brightness)

                # Set buzzer frequency and duty cycle
                buzzer.freq(frequency)
                buzzer.duty_u16(32768)  # 50% duty cycle

                utime.sleep(0.01)

            # Decrease frequency and brightness
            for i in range(100, 0, -2):
                brightness = interval_mapping(i, 0, 100, 0, 65535)
                frequency = interval_mapping(i, 0, 100, 500, 2000)

                led.duty_u16(brightness)
                buzzer.freq(frequency)
                buzzer.duty_u16(32768)

                utime.sleep(0.01)
        else:
            # Alarm is OFF
            # Turn off LED and buzzer
            led.duty_u16(0)
            buzzer.duty_u16(0)
            utime.sleep(0.1)
except KeyboardInterrupt:
    # Clean up
    buzzer.deinit()
    led.deinit()
    print("Program stopped.")