const int switchPin = 14;   // GPIO pin connected to the micro switch
int switchState = 0;

void setup() {
  Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
  pinMode(switchPin, INPUT);  // Set the switch pin as input
}

void loop() {
  switchState = digitalRead(switchPin);  // Read the state of the switch

  if (switchState == HIGH) {
    Serial.println("The switch is pressed!");
  } else {
    Serial.println("The switch is not pressed.");
  }
  delay(200);  // Small delay to avoid flooding the Serial Monitor
}