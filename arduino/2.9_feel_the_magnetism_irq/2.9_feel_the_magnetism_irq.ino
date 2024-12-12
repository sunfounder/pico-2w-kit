const int reedPin = 14;    // GPIO pin connected to the reed switch
int reedState = 0;

void setup() {
  Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
  pinMode(reedPin, INPUT);    // Set the reed pin as input
}

void loop() {
  reedState = digitalRead(reedPin);  // Read the state of the reed switch

  if (reedState == HIGH) {
    Serial.println("Magnet Detected!");
  } else {
    Serial.println("No Magnet.");
  }
  delay(500);  // Delay to avoid flooding the Serial Monitor
}