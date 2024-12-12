import machine
import utime

# Initialize PWM on GP15
buzzer = machine.PWM(machine.Pin(15))

def play_tone(frequency, duration):
    # Set the frequency of the PWM signal
    buzzer.freq(frequency)
    # Set duty cycle to 50%
    buzzer.duty_u16(32768)
    # Play the tone for the specified duration
    utime.sleep_ms(duration)
    # Turn off the buzzer
    buzzer.duty_u16(0)

# Play some tones
play_tone(440, 500)  # A4 note for 500ms
utime.sleep_ms(200)
play_tone(494, 500)  # B4 note for 500ms
utime.sleep_ms(200)
play_tone(523, 500)  # C5 note for 500ms