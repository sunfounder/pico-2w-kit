const int buttonPin = 14;  // GPIO pin connected to the button

void setup() {
  Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
  pinMode(buttonPin, INPUT);  // Set the button pin as input
}

void loop() {
  int buttonState = digitalRead(buttonPin);  // Read the state of the button

  if (buttonState == HIGH) {
    Serial.println("You pressed the button!");
  }
  delay(100);  // Small delay to avoid reading the button too frequently
}