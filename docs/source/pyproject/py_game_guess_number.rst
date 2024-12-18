.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_guess_number:

7.7 Creating a "Guess the Number" Game
=============================================================

In this project, we'll build an interactive **Guess the Number** game using the Raspberry Pi Pico 2, a 4x4 matrix keypad, and an I2C LCD1602 display. The game generates a random number between 0 and 99, and players take turns guessing the number. After each guess, the game narrows down the range based on whether the guess was too high or too low, until someone guesses the correct number.


**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Understanding the Components**

* **4x4 Matrix Keypad**: A keypad with 16 buttons arranged in a 4-row by 4-column matrix. We'll use it to input numbers and commands.
* **I2C LCD1602 Display**: A 16x2 character LCD display with an I2C interface, simplifying wiring by using only two data lines (SDA and SCL).

**Schematic**


|sch_guess_number|

This circuit is based on :ref:`py_keypad` with the addition of an I2C LCD1602 to display the pressed keys.


**Wiring**

|wiring_game_guess_number| 

To make the wiring easier, in the above diagram, the column row of the matrix keyboard and the 10K resistors are inserted into the holes where G10 ~ G13 are located at the same time.


**Writing the Code**

We'll write a MicroPython program that:

* Generates a random number between 0 and 99.
* Reads input from the keypad.
* Updates the LCD display with hints and player inputs.
* Narrows down the range after each guess.

.. note::

    * Open the ``7.7_game_guess_number.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the library called ``lcd1602.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

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

After the code runs, follow these steps to play the game:

* Start the Game:

  Press the 'A' key on the keypad.

* Enter Guesses:

  * Use the number keys to input your guess (0-99).
  * Press 'D' to submit your guess.

* Receive Feedback:

  * The LCD will indicate if your guess is too high, too low, or correct.
  * The range will adjust accordingly.

* Winning the Game:

  * When you guess the correct number, the LCD will display "Correct! Number is XX".
  * The game resets automatically after a short delay.

**Understanding the Code**

#. Imports and Initialization:

   * ``lcd1602.LCD``: For controlling the LCD display.
   * ``machine.Pin``: For interacting with GPIO pins.
   * ``urandom``: For generating random numbers.
   * Initialize I2C communication for the LCD1602 display.

#. Keypad Scanning Function (``read_keypad``):

   * Sets each row high one at a time.
   * Checks if any column reads high, indicating a button press.
   * Returns the character corresponding to the pressed key.

   .. code-block:: python

        def read_keypad():
            for row_num, row_pin in enumerate(row_pins):
                row_pin.high()
                for col_num, col_pin in enumerate(col_pins):
                    if col_pin.value() == 1:
                        row_pin.low()
                        return keypad_map[row_num][col_num]
                row_pin.low()
            return None

#. Game Variables and Initialization (``init_game``):

   * ``target_number``: Random number between 0 and 99.
   * ``lower_bound and upper_bound``: Start at 0 and 99 respectively.
   * ``guess``: String to store the current guess input.

   .. code-block:: python

        def init_game():
            global target_number, lower_bound, upper_bound, guess
            target_number = urandom.randint(0, 99)
            lower_bound = 0
            upper_bound = 99
            guess = ""
            lcd.clear()
            lcd.message("Press A to Start")

#. Display Update Function (``update_display``):

   Clears the LCD and displays the provided message.

   .. code-block:: python

        # Display function
        def update_display(message):
            lcd.clear()
            lcd.message(message)

#. Main Program Loop:

   * Waits for key presses and handles game logic.
   * Key ``A``: Starts or restarts the game.
   * Digits ``0``-``9``: Builds the current guess number.
   * Key ``D``: Submits the guess and updates the range.
   * Checks if the guess is within the current bounds.
   * Updates ``lower_bound`` or ``upper_bound`` based on the guess.
   * Resets guess for the next input.
   * If the guess is correct, displays a success message and resets the game.
   * Key ``B``: Clears the current guess.
   * Key ``C``: Reserved for additional functionality (e.g., hints).

   .. code-block:: python

        while True:
            key = read_keypad()
            if key:
                utime.sleep(0.2)  # Debounce delay

                if not game_started:
                    if key == "A":
                        game_started = True
                        update_display("Enter your guess:")
        ...
        ...
            utime.sleep(0.1)

#. Debouncing and Delays:

   * ``utime.sleep(0.2)``: Short delay after a key press to debounce.
   * ``utime.sleep(0.1)``: Small delay in the main loop to reduce CPU usage.

**Troubleshooting**

* LCD Not Displaying Text:

  * Verify SDA and SCL connections (GP6 and GP7).
  * Check that the LCD is powered correctly.
  * Adjust the contrast potentiometer on the back of the LCD module.

* Keypad Not Responding:

  * Check all row and column connections.
  * Ensure that pull-down resistors are connected if not using internal pull-downs.
  * Verify that the keypad is functioning properly.

* Random Number Not Changing:

  * Ensure that ``urandom`` is properly imported and used.
  * The random seed may need to be initialized for better randomness.

* Game Logic Issues:

  * Double-check the conditions and bounds when processing guesses.
  * Ensure that the upper and lower bounds are updated correctly.

**Enhancements and Extensions**

* Add Multiplayer Support:

  * Keep track of the number of guesses each player makes.
  * Rotate turns between players.

* Implement Scoring System:

  * Award points based on how quickly the number is guessed.
  * Display scores on the LCD.

* Provide Hints:

  Use the 'C' key to give hints, such as "Number is even" or "Number is a multiple of 5".

* Increase Range:

  * Modify the game to guess numbers between 0 and 999.
  * Adjust the display and input methods accordingly.

* Visual and Audio Feedback:

  Add LEDs or a buzzer to provide additional feedback.

**Conclusion**

You've successfully built an interactive Guess the Number game using the Raspberry Pi Pico 2 W! This project combines user input, random number generation, and display output to create a fun and engaging game. It's an excellent way to practice working with keypads, LCD displays, and game logic in MicroPython.

Feel free to enhance the game further by adding new features or improving the interface. This project can serve as a foundation for more complex interactive applications.