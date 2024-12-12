#include <Adafruit_NeoPixel.h>

#define PIXEL_PIN    0    // Digital IO pin connected to the NeoPixels
#define PIXEL_COUNT  8    // Number of NeoPixels

// Declare our NeoPixel strip object
Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();           // Initialize the NeoPixel library
  strip.show();            // Turn OFF all pixels ASAP
}

void loop() {
  // Set the color of each pixel
  strip.setPixelColor(0, strip.Color(255, 0, 0));   // Red
  strip.setPixelColor(1, strip.Color(0, 255, 0));   // Green
  strip.setPixelColor(2, strip.Color(0, 0, 255));   // Blue
  strip.setPixelColor(3, strip.Color(255, 255, 0)); // Yellow
  strip.setPixelColor(4, strip.Color(0, 255, 255)); // Cyan
  strip.setPixelColor(5, strip.Color(255, 0, 255)); // Magenta
  strip.setPixelColor(6, strip.Color(255, 255, 255)); // White
  strip.setPixelColor(7, strip.Color(0, 0, 0));     // Off

  strip.show();  // Update the strip with new contents
  delay(1000);   // Wait for a second

  // Turn off all pixels
  strip.clear();
  strip.show();
  delay(1000);   // Wait for a second
}