// Define the connection pins
const int trigPin = 17;  // GPIO 17 -> Trig
const int echoPin = 16;  // GPIO 16 -> Echo

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);

  // Initialize the sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long duration;
  float distance;

  // Trigger the sensor by setting Trig HIGH for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the Echo pin, returns the duration in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  distance = duration * 0.034 / 2;

  // Print the distance to the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(500); // Wait for half a second before the next measurement
}