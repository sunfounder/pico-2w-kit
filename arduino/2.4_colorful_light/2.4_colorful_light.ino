// Define the GPIO pins connected to the RGB LED
const int redPin = 13;   // Red pin
const int greenPin = 14; // Green pin
const int bluePin = 15;  // Blue pin

void setup() {
  // Initialize each RGB LED pin as an output
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

// Function to set the color
void setColor(unsigned char red, unsigned char green, unsigned char blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

void loop() {
  // Red color
  setColor(255, 0, 0);
  delay(1000);

  // Green color
  setColor(0, 255, 0);
  delay(1000);

  // Blue color
  setColor(0, 0, 255);
  delay(1000);

  // Yellow color (Red + Green)
  setColor(255, 255, 0);
  delay(1000);

  // Cyan color (Green + Blue)
  setColor(0, 255, 255);
  delay(1000);

  // Magenta color (Red + Blue)
  setColor(255, 0, 255);
  delay(1000);

  // White color (Red + Green + Blue)
  setColor(255, 255, 255);
  delay(1000);

  // Turn off
  setColor(0, 0, 0);
  delay(1000);
}