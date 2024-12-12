#include <Servo.h>

Servo myServo;  // Create a servo object

void setup() {
  myServo.attach(15);  // Attach the servo to GPIO pin 15
}

void loop() {
  // Move the servo from 0 to 180 degrees
  for (int angle = 0; angle <= 180; angle += 1) {
    myServo.write(angle);
    delay(15);  // Wait 15 milliseconds for the servo to reach the position
  }
  // Move the servo from 180 to 0 degrees
  for (int angle = 180; angle >= 0; angle -= 1) {
    myServo.write(angle);
    delay(15);
  }
}