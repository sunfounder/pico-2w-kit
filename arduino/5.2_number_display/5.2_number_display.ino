// Define the pins connected to the 74HC595
const int DS = 0;    // GPIO 0 -> DS (Pin 14)
const int SHCP = 2;  // GPIO 2 -> SHCP (Pin 11)
const int STCP = 1;  // GPIO 1 -> STCP (Pin 12)

// Array of hexadecimal codes for digits 0-9 on a common cathode 7-segment display
const byte numArray[] = {
  0x3F,  // 0: 00111111
  0x06,  // 1: 00000110
  0x5B,  // 2: 01011011
  0x4F,  // 3: 01001111
  0x66,  // 4: 01100110
  0x6D,  // 5: 01101101
  0x7D,  // 6: 01111101
  0x07,  // 7: 00000111
  0x7F,  // 8: 01111111
  0x6F   // 9: 01101111
};

void setup() {
  // Initialize the control pins as outputs
  pinMode(DS, OUTPUT);
  pinMode(SHCP, OUTPUT);
  pinMode(STCP, OUTPUT);
}

void loop() {
  // Iterate through each number 0-9
  for (int num = 0; num < 10; num++) {
    // Set STCP to LOW to prepare for data
    digitalWrite(STCP, LOW);

    // Shift out the data to the shift register
    shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

    // Set STCP to HIGH to latch the data to the output pins
    digitalWrite(STCP, HIGH);

    delay(1000);  // Wait for one second before displaying the next number
  }

  // Turn off all segments after displaying 0-9
  digitalWrite(STCP, LOW);
  shiftOut(DS, SHCP, MSBFIRST, 0x00);
  digitalWrite(STCP, HIGH);
  delay(1000);
}