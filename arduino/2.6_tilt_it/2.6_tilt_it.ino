const int tiltPin = 14;  // GPIO pin connected to the tilt switch

void setup() {
  Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
  pinMode(tiltPin, INPUT);    // Set the tilt pin as input
}

void loop() {
  int tiltState = digitalRead(tiltPin);  // Read the state of the tilt switch

  if (tiltState == HIGH) {
    Serial.println("The switch works!");
  }
  delay(100);  // Small delay to avoid flooding the Serial Monitor
}