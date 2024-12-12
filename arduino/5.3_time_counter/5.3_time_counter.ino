// Define the GPIO pins connected to the 74HC595 shift registers
const int DS = 18;    // GPIO 18 -> DS (Pin 14) of first 74HC595
const int SHCP = 20;  // GPIO 20 -> SHCP (Pin 11) of both 74HC595s
const int STCP = 19;  // GPIO 19 -> STCP (Pin 12) of both 74HC595s

// Array to hold the 'X' pattern for the 8x8 LED matrix
const byte pattern[] = {
  0b10000001, // Row 0
  0b01000010, // Row 1
  0b00100100, // Row 2
  0b00011000, // Row 3
  0b00011000, // Row 4
  0b00100100, // Row 5
  0b01000010, // Row 6
  0b10000001  // Row 7
};

void setup() {
  // Initialize the control pins as outputs
  pinMode(DS, OUTPUT);
  pinMode(SHCP, OUTPUT);
  pinMode(STCP, OUTPUT);
}

void loop() {
  for (int i = 0; i < 8; i++) {
    // Set STCP to LOW to prepare for data
    digitalWrite(STCP, LOW);

    // Shift out the row data
    shiftOut(DS, SHCP, MSBFIRST, pattern[i]);

    // Shift out the column data (activating one column at a time)
    shiftOut(DS, SHCP, MSBFIRST, 0x80 >> i);

    // Set STCP to HIGH to latch the data to the output pins
    digitalWrite(STCP, HIGH);

    delay(2); // Short delay for persistence of vision
  }
}