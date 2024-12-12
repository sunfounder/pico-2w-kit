// Define the pins
const int thermistorPin = 28;  // Thermistor connected to GP28 (ADC2)

// Constants for the thermistor and calculations
const float BETA = 3950;                 // Beta value of the thermistor (provided by manufacturer)
const float SERIES_RESISTOR = 10000;     // 10KΩ resistor
const float NOMINAL_RESISTANCE = 10000;  // Resistance at 25°C (provided by manufacturer)
const float NOMINAL_TEMPERATURE = 25.0;  // 25°C in Celsius

void setup() {
  Serial.begin(115200);  // Initialize Serial Monitor
}

void loop() {
  // Read the analog value from the thermistor
  int adcValue = analogRead(thermistorPin);
  // Convert the ADC value to voltage
  float voltage = adcValue * (3.3 / 1023.0);
  // Calculate the resistance of the thermistor
  float resistance = (voltage * SERIES_RESISTOR) / (3.3 - voltage);
  // Calculate the temperature in Kelvin using the Beta formula
  float temperatureK = 1 / ((1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE));
  // Convert Kelvin to Celsius
  float temperatureC = temperatureK - 273.15;
  // Convert Celsius to Fahrenheit
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

  // Print the temperature readings
  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.print(" °C, ");
  Serial.print(temperatureF);
  Serial.println(" °F");

  delay(1000);  // Wait a second before the next reading
}