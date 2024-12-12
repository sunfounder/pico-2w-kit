// Define the pins connected to the motor driver
const int motor1A = 14; // Motor control pin 1
const int motor2A = 15; // Motor control pin 2

void setup() {
  // Initialize the motor control pins as OUTPUT
  pinMode(motor1A, OUTPUT); 
  pinMode(motor2A, OUTPUT); 
}

void loop() {
    // Rotate the motor clockwise
    clockwise();
    delay(1000); // Keep the motor running clockwise for 1 second
    
    // Stop the motor
    stopMotor();
    delay(1000); // Pause for 1 second
    
    // Rotate the motor counterclockwise
    anticlockwise();
    delay(1000); // Keep the motor running counterclockwise for 1 second
    
    // Stop the motor
    stopMotor();
    delay(1000); // Pause for 1 second
}

// Function to rotate the motor clockwise
void clockwise()
{
  digitalWrite(motor1A, HIGH); // Set motor1A to HIGH
  digitalWrite(motor2A, LOW);  // Set motor2A to LOW
  // This combination causes the motor to rotate in the clockwise direction
}

// Function to rotate the motor counterclockwise
void anticlockwise()
{
  digitalWrite(motor1A, LOW);  // Set motor1A to LOW
  digitalWrite(motor2A, HIGH); // Set motor2A to HIGH
  // This combination causes the motor to rotate in the counterclockwise direction
}

// Function to stop the motor
void stopMotor()
{
  digitalWrite(motor1A, LOW);  // Set motor1A to LOW
  digitalWrite(motor2A, LOW);  // Set motor2A to LOW
  // Setting both pins LOW stops the motor
}
