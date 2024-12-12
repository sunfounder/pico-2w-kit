const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)

void setup() {
  Serial.begin(115200);  // Initialize Serial Monitor
}

void loop() {
  // Read the analog value from the water sensor
  int sensorValue = analogRead(waterSensorPin);
  // Print the sensor value to the Serial Monitor
  Serial.print("Water Sensor Value: ");
  Serial.println(sensorValue);
  delay(500);  // Wait half a second before reading again
}