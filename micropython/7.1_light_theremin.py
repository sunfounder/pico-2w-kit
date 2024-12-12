import machine
import utime

# Initialize components
led = machine.Pin(16, machine.Pin.OUT)  # LED on GP16
photoresistor = machine.ADC(28)         # Photoresistor connected to ADC0 (GP28)
buzzer = machine.PWM(machine.Pin(15))   # Buzzer connected to GP15

# Variables for calibration
light_low = 65535
light_high = 0

# Function to map values from one range to another
def interval_mapping(x, in_min, in_max, out_min, out_max):
    # Ensure in_min != in_max to avoid division by zero
    if in_max - in_min == 0:
        return out_min
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Function to play a tone on the buzzer
def play_tone(pin, frequency):
    if frequency <= 0:
        pin.duty_u16(0)
    else:
        pin.freq(frequency)
        pin.duty_u16(32768)  # 50% duty cycle

# Calibration process
def calibrate():
    global light_low, light_high
    print("Calibrating... Move your hand over the sensor.")
    led.value(1)  # Turn on LED to indicate calibration
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 seconds calibration
        light_value = photoresistor.read_u16()
        if light_value > light_high:
            light_high = light_value
        if light_value < light_low:
            light_low = light_value
        utime.sleep_ms(10)
    led.value(0)  # Turn off LED after calibration
    print("Calibration complete.")
    print("Light Low:", light_low)
    print("Light High:", light_high)

# Main function
def main():
    calibrate()
    try:
        while True:
            light_value = photoresistor.read_u16()
            # Map the light value to a frequency range (e.g., 200 Hz to 2000 Hz)
            frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
            play_tone(buzzer, frequency)
            utime.sleep_ms(20)
    except KeyboardInterrupt:
        buzzer.deinit()
        print("Program stopped.")

# Run the main function
if __name__ == "__main__":
    main()