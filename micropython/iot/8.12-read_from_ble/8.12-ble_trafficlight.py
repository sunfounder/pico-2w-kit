# Import necessary modules
from machine import Pin 
import bluetooth
from ble_example.ble_simple_peripheral import BLESimplePeripheral

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble,"pico2w")

# Create a Pin object for the onboard LED, configure it as an output
led = Pin("LED", Pin.OUT)

red = machine.Pin(13, machine.Pin.OUT)
yellow = machine.Pin(12, machine.Pin.OUT)
green = machine.Pin(11, machine.Pin.OUT)

def update_traffic(data):
    
    decoded_data = data.decode('utf-8').rstrip('\r\n')
    
    red.off()
    green.off()
    yellow.off()
    
    if decoded_data == "R" or decoded_data == "r":
        red.on()
    elif decoded_data == "G" or decoded_data == "g":
        green.on()
    elif decoded_data == "Y" or decoded_data == "y":
        yellow.on()
    

# Define a callback function to handle received data
def on_rx(data):
    print("Data received: ", data)  # Print the received data
    
    update_traffic(data)

# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  # Set the callback function for data reception
