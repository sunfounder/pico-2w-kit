  // Define the pins connected to the 74HC595
  const int DS = 0;   // GPIO 0 -> DS (Pin 14)
  const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
  const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

  // Array of binary patterns to control LEDs
  int datArray[] = {
    0b00000000, // All LEDs off
    0b00000001, // LED 0 on
    0b00000011, // LEDs 0 and 1 on
    0b00000111, // LEDs 0, 1, and 2 on
    0b00001111, // LEDs 0, 1, 2, and 3 on
    0b00011111, // LEDs 0 to 4 on
    0b00111111, // LEDs 0 to 5 on
    0b01111111, // LEDs 0 to 6 on
    0b11111111  // All LEDs on
  };

  void setup() {
    // Initialize the control pins as outputs
    pinMode(DS, OUTPUT);
    pinMode(SHCP, OUTPUT);
    pinMode(STCP, OUTPUT);
  }

  void loop() {
    // Iterate through each pattern in datArray
    for (int num = 0; num < 9; num++) {
      // Set STCP to LOW to prepare for data
      digitalWrite(STCP, LOW);

      // Shift out the data to the shift register
      shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

      // Set STCP to HIGH to latch the data to the output pins
      digitalWrite(STCP, HIGH);

      delay(500); // Wait for half a second before the next pattern
    }

    // Turn off all LEDs after the sequence
    digitalWrite(STCP, LOW);
    shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
    digitalWrite(STCP, HIGH);
    delay(500);
  }