const int switchPin = 14;   // GPIO pin connected to the slide switch
int switchState = 0;

void setup() {
  Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
  pinMode(switchPin, INPUT);  // Set the switch pin as input
}

void loop() {
  switchState = digitalRead(switchPin);  // Read the state of the switch

  if (switchState == HIGH) {
    Serial.println("ON");   // Switch toggled to the left
  } else {
    Serial.println("OFF");  // Switch toggled to the right
  }
  delay(200);  // Small delay to avoid flooding the Serial Monitor
}