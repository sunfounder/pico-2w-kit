const int ledPin = 15; // GPIO pin connected to the LED

void setup() {
  pinMode(ledPin, OUTPUT); // Initialize the GPIO pin as an output
}

void loop() {
  // Increase brightness
  for (int value = 0; value <= 255; value += 5) {
    analogWrite(ledPin, value); // Set the brightness
    delay(30);                  // Wait for 30 milliseconds
  }
  // Decrease brightness
  for (int value = 255; value >= 0; value -= 5) {
    analogWrite(ledPin, value);
    delay(30);
  }
}