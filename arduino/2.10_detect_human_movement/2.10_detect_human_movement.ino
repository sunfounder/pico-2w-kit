const int pirPin = 14;  // PIR sensor output pin connected to GP14
int pirState = LOW;     // Current state of PIR sensor
int val = 0;            // Variable to store the PIR reading

void setup() {
  Serial.begin(115200);    // Initialize Serial Monitor
  pinMode(pirPin, INPUT);  // Set the PIR pin as input
  Serial.println("PIR Sensor Test");
  delay(2000);  // Allow the PIR sensor to stabilize
}

void loop() {
  val = digitalRead(pirPin);  // Read the PIR sensor

  if (val == HIGH) {
    if (pirState == LOW) {
      Serial.println("Motion detected!");
      pirState = HIGH;
    }
  } else {
    if (pirState == HIGH) {
      Serial.println("Motion ended!");
      pirState = LOW;
    }
  }
  delay(500);  // Wait half a second before checking again
}