#include <Wire.h>
#include <Adafruit_MPR121.h>

// Create an instance of the MPR121 sensor
Adafruit_MPR121 cap = Adafruit_MPR121();

// Array to hold the touch states of each electrode
bool touchStates[12] = { false };

// Variables to store current and last touch states
uint16_t currtouched = 0;
uint16_t lasttouched = 0;

void setup() {
  Serial.begin(115200);  // Initialize serial communication at 115200 baud
  while (!Serial)
    ;  // Wait for Serial Monitor to open

  // Initialize the MPR121 sensor with I2C address 0x5A
  if (!cap.begin(0x5A)) {
    Serial.println("MPR121 not found, check wiring?");
    while (1)
      ;
  }
  Serial.println("MPR121 found!");
}

void loop() {
  // Get the currently touched pads
  currtouched = cap.touched();

  // Check if there is a change in touch state
  if (currtouched != lasttouched) {
    // Update the last touched state
    lasttouched = currtouched;

    // Iterate through each electrode
    for (int i = 0; i < 12; i++) {
      // Check if the electrode is touched
      if (currtouched & (1 << i)) {
        touchStates[i] = true;
      } else {
        touchStates[i] = false;
      }
    }

    // Print the touch states as a binary string
    for (int i = 0; i < 12; i++) {
      Serial.print(touchStates[i] ? "1" : "0");
    }
    Serial.println();
  }

  delay(100);  // Small delay to stabilize readings
}