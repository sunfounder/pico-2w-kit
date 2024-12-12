#include "Adafruit_Keypad.h"

// Define the number of rows and columns
const byte ROWS = 4;
const byte COLS = 4;

// Define the keymap for the keypad
char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

// Connect to the row pinouts of the keypad
byte rowPins[ROWS] = { 2, 3, 4, 5 };

// Connect to the column pinouts of the keypad
byte colPins[COLS] = { 6, 7, 8, 9 };

// Create the Keypad object
Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  // Initialize Serial communication
  Serial.begin(115200);

  // Initialize the keypad
  myKeypad.begin();
}

void loop() {
  // Update the state of keys
  myKeypad.tick();

  // Check if there are any new keypad events
  while (myKeypad.available()) {
    // Read the keypad event
    keypadEvent e = myKeypad.read();

    // Check if the event is a key press
    if (e.bit.EVENT == KEY_JUST_PRESSED) {
      // Print the key value to the Serial Monitor
      Serial.println((char)e.bit.KEY);
    }
  }

  delay(10); // Short delay to improve stability
}