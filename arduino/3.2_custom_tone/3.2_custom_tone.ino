const int buzzerPin = 15;  // GPIO pin connected to the transistor base

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Play a tone at 440 Hz (A4 note) for 1 second
  tone(buzzerPin, 440, 1000);
  delay(1000);  // Wait for the tone to finish
  // Wait for 1 second before playing again
  delay(1000);
}