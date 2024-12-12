from lcd1602 import LCD
from machine import I2C, Pin
import utime
import urandom

# Initialize I2C communication for the LCD1602 display
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
lcd = LCD(i2c)

# Keypad character mapping for a 4x4 matrix keypad
keypad_map = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# Define row and column pins
row_pins = [Pin(pin_num, Pin.OUT) for pin_num in [21, 20, 19, 18]]  # R1-R4
col_pins = [Pin(pin_num, Pin.IN, Pin.PULL_DOWN) for pin_num in [13, 12, 11, 10]]  # C1-C4

# Function to scan the keypad
def read_keypad():
    for row_num, row_pin in enumerate(row_pins):
        row_pin.high()
        for col_num, col_pin in enumerate(col_pins):
            if col_pin.value() == 1:
                row_pin.low()
                return keypad_map[row_num][col_num]
        row_pin.low()
    return None

# Initialize game variables
def init_game():
    global target_number, lower_bound, upper_bound, guess
    target_number = urandom.randint(0, 99)
    lower_bound = 0
    upper_bound = 99
    guess = ""
    lcd.clear()
    lcd.message("Press A to Start")

# Display function
def update_display(message):
    lcd.clear()
    lcd.message(message)

# Main program
init_game()
game_started = False

while True:
    key = read_keypad()
    if key:
        utime.sleep(0.2)  # Debounce delay

        if not game_started:
            if key == "A":
                game_started = True
                update_display("Enter your guess:")
        else:
            if key in "0123456789":
                if len(guess) < 2:
                    guess += key
                    update_display("Guess: {}\n{} < ? < {}".format(guess, lower_bound, upper_bound))
            elif key == "D":
                if guess != "":
                    guess_number = int(guess)
                    if guess_number < lower_bound or guess_number > upper_bound:
                        update_display("Out of range!\n{} < ? < {}".format(lower_bound, upper_bound))
                    elif guess_number > target_number:
                        upper_bound = guess_number - 1
                        guess = ""
                        update_display("Too High!\n{} < ? < {}".format(lower_bound, upper_bound))
                    elif guess_number < target_number:
                        lower_bound = guess_number + 1
                        guess = ""
                        update_display("Too Low!\n{} < ? < {}".format(lower_bound, upper_bound))
                    else:
                        update_display("Correct!\nNumber is {}".format(target_number))
                        game_started = False
                        utime.sleep(2)
                        init_game()
                else:
                    update_display("Enter a number")
            elif key == "A":
                # Restart the game
                init_game()
                game_started = True
                update_display("Enter your guess:")
            elif key == "B":
                # Clear current guess
                guess = ""
                update_display("Guess cleared")
            elif key == "C":
                # Show hint or any other functionality
                update_display("Hint not available")
    utime.sleep(0.1)