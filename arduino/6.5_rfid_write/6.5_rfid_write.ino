#include <SPI.h>
#include <MFRC522.h>

// Define the connection pins for the RFID module
#define SS_PIN 17    // SDA pin connected to GPIO 17 (SPI SS)
#define RST_PIN 9    // RST pin connected to GPIO 9

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  while (!Serial); // Wait for serial port to connect

  // Initialize SPI bus
  SPI.begin();

  // Initialize RFID reader
  mfrc522.PCD_Init();
  Serial.println("RFID Reader Initialized!");
}

void loop() {
  // Look for new RFID cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  // Read the UID of the card
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) {
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println(content);

  // Print the associated user data
  if (userData.length() > 0) {
    Serial.print("Associated Data: ");
    Serial.println(userData);
  } else {
    Serial.println("No data associated with this UID.");
  }
}