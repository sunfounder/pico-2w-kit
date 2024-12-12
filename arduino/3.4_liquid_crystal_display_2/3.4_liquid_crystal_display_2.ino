#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define LCD_ADDRESS 0x27
#define LCD_COLUMNS 16
#define LCD_ROWS 2

LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

void setup() {
  lcd.init();
  lcd.backlight();

  Serial.begin(115200);
  lcd.setCursor(0, 0);
  lcd.print("Enter text:");
}

void loop() {
  if (Serial.available() > 0) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("You typed:");

    String inputText = Serial.readStringUntil('\n');
    lcd.setCursor(0, 1);
    lcd.print(inputText);
  }
}