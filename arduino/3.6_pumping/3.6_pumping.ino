// Define the pins connected to the motor driver
const int motor1A = 14; // Motor control pin 1
const int motor2A = 15; // Motor control pin 2

void setup() {
  // Set motor control pins as OUTPUT
  pinMode(motor1A, OUTPUT); // Configure motor1A as an output pin
  pinMode(motor2A, OUTPUT); // Configure motor2A as an output pin
}

void loop() {
  // Rotate the motor in a clockwise direction
  digitalWrite(motor1A, HIGH); // Set motor1A to HIGH (activates one side of the motor)
  digitalWrite(motor2A, LOW);  // Set motor2A to LOW (deactivates the opposite side of the motor)
}

