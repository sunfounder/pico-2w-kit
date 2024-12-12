// Define the pins
const int potPin = 28;  // Potentiometer connected to GP28 (ADC2)
const int ledPin = 15;  // LED connected to GP15 (PWM capable)

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Set up the LED pin as output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Read the analog value from the potentiometer (0-1023)
  int sensorValue = analogRead(potPin);
  // Print the sensor value for debugging
  Serial.println(sensorValue);

  // Map the sensor value to a PWM value (0-255)
  int brightness = map(sensorValue, 0, 1023, 0, 255);
  // Set the brightness of the LED
  analogWrite(ledPin, brightness);

  // Small delay for stability
  delay(10);
}