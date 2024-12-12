const int sensorPin = 28;  // Photoresistor connected to GP28 (ADC2)

void setup() {
  Serial.begin(115200);  // Initialize Serial Monitor
}

void loop() {
  // Read the analog value from the photoresistor
  int sensorValue = analogRead(sensorPin);
  // Print the sensor value to the Serial Monitor
  Serial.println(sensorValue);
  delay(500);  // Wait half a second before reading again
}