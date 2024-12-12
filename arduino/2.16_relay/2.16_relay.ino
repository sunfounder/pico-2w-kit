const int relayPin = 15;  // GPIO pin connected to the transistor base

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
}

void loop() {
  // Turn the relay on
  digitalWrite(relayPin, HIGH);
  Serial.println("Relay ON");
  delay(2000);  // Wait for 2 seconds

  // Turn the relay off
  digitalWrite(relayPin, LOW);
  Serial.println("Relay OFF");
  delay(2000);  // Wait for 2 seconds
}