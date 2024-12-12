const int buzzerPin = 15;  // GPIO pin connected to the transistor base

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  digitalWrite(buzzerPin, HIGH);  // Turn the buzzer on
  delay(1000);                    // Wait for 1 second
  digitalWrite(buzzerPin, LOW);   // Turn the buzzer off
  delay(1000);                    // Wait for 1 second
}