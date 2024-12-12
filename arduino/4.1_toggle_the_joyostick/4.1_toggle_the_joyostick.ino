// Define the pins
const int joystickX = 26;  // GP26 (ADC0) connected to VRx
const int joystickY = 27;  // GP27 (ADC1) connected to VRy
const int joystickSW = 22; // GP22 connected to SW (button)

void setup() {
  // Initialize serial communication at 115200 baud
  Serial.begin(115200);

  // Initialize the joystick switch pin as input
  pinMode(joystickSW, INPUT_PULLUP);

}

void loop() {
  // Read analog values from the joystick
  int xValue = analogRead(joystickX);
  int yValue = analogRead(joystickY);

  // Read the joystick button state
  int buttonState = digitalRead(joystickSW);

  // Print the joystick values to the Serial Monitor
  Serial.print("X: ");
  Serial.print(xValue);
  Serial.print(" | Y: ");
  Serial.print(yValue);
  Serial.print(" | Button: ");
  Serial.println(buttonState == LOW ? "Pressed" : "Released");

  delay(500); // Wait for half a second before the next reading
}