#include <DHT.h>

// Define the connection pins
#define DHTPIN 16      // GPIO 16 -> Data pin of DHT11
#define DHTTYPE DHT11  // Define the sensor type

// Create a DHT object
DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0;  // Stores the last time the display was updated
const long interval = 2000;        // Interval at which to read sensor (milliseconds)

void setup() {
  // Initialize serial communication at 115200 baud
  Serial.begin(115200);
  Serial.println(F("DHT11 Sensor Test!"));

  // Initialize the DHT sensor
  dht.begin();
}

void loop() {
  unsigned long currentMillis = millis();

  // Update the sensor reading every 'interval' milliseconds
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Read humidity and temperature
    float humidity = dht.readHumidity();
    float temperatureC = dht.readTemperature();
    float temperatureF = dht.readTemperature(true);

    // Check if any reads failed
    if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
      Serial.println(F("Failed to read from DHT sensor!"));
      return;
    }

    // Calculate heat index
    float heatIndexC = dht.computeHeatIndex(temperatureC, humidity, false);
    float heatIndexF = dht.computeHeatIndex(temperatureF, humidity);

    // Print the results to the Serial Monitor
    Serial.print(F("Humidity: "));
    Serial.print(humidity);
    Serial.print(F("%  Temperature: "));
    Serial.print(temperatureC);
    Serial.print(F("°C "));
    Serial.print(temperatureF);
    Serial.print(F("°F  Heat index: "));
    Serial.print(heatIndexC);
    Serial.print(F("°C "));
    Serial.print(heatIndexF);
    Serial.println(F("°F"));
  }
}