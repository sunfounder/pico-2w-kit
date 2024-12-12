// Define the GPIO pins connected to the LED Bar Graph
const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

void setup() {
  // Initialize each pin as an output
  for (int i = 0; i < 10; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // Turn on LEDs sequentially
  for (int i = 0; i < 10; i++) {
    digitalWrite(ledPins[i], HIGH); // Turn on LED
    delay(500);                     // Wait 500 milliseconds
    digitalWrite(ledPins[i], LOW);  // Turn off LED
    delay(500);                     // Wait 500 milliseconds
  }
}