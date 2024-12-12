from mfrc522 import SimpleMFRC522
from machine import Pin, SPI

# Initialize the RFID reader
reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

def read_from_tag():
    try:
        print("Place your tag near the reader...")
        id, text = reader.read()
        print("Tag ID: {}".format(id))
        print("Data: {}".format(text.strip()))
    finally:
        pass  # Cleanup actions if necessary

read_from_tag()