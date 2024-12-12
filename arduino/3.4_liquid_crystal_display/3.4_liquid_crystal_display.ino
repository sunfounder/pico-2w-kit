#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD I2C address (usually 0x27 or 0x3F)
#define LCD_ADDRESS 0x27
#define LCD_COLUMNS 16
#define LCD_ROWS    2

// Initialize the library with the I2C address and dimensions
LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

void setup() {
  // Initialize the LCD
  lcd.init();
  lcd.backlight();  // Turn on the backlight

  // Print messages to the LCD
  lcd.setCursor(0, 0);  // Column 0, Row 0
  lcd.print("Hello, World!");
  lcd.setCursor(0, 1);  // Column 0, Row 1
  lcd.print("LCD1602 with I2C");
}

void loop() {
  // Nothing to do here
}