from mfrc522 import SimpleMFRC522
from machine import Pin, SPI

# Initialize the RFID reader
reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

def write_to_tag():
    try:
        data = input("Enter data to write to the tag: ")
        print("Place your tag near the reader...")
        reader.write(data)
        print("Data written successfully!")
    finally:
        pass  # Cleanup actions if necessary

write_to_tag()