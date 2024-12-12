// Define the pins
const int buttonPin = 14;  // Button connected to GP14
const int transistorPin = 15;  // Transistor base connected to GP15

int buttonState = 0;  // Variable to hold the button state

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(transistorPin, OUTPUT);
}

void loop() {
  // Read the state of the button
  buttonState = digitalRead(buttonPin);

  // control the transistor
  digitalWrite(transistorPin, buttonState);

  delay(10);  // Small delay for debouncing
}