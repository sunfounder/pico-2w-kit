import bluetooth
import struct
import time
import machine
import ubinascii
from ble_advertising import advertising_payload
from micropython import const
from machine import Pin 

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_INDICATE_DONE = const(20)

_FLAG_READ = const(0x0002)
_FLAG_NOTIFY = const(0x0010)

# Custom Service and Characteristic UUIDs
# Modify these as needed.
_SERVICE_UUID = bluetooth.UUID("3ec837af-b0c6-4e7e-a8c5-4b31311d98cf")
_CHAR_UUID = (
    bluetooth.UUID("945c4d90-825d-452f-820a-0d8b0cc74a12"),
    _FLAG_READ | _FLAG_NOTIFY,
)

_SERVICE = (
    _SERVICE_UUID,
    (_CHAR_UUID,),
)

led = Pin("LED", Pin.OUT)

class BLEText:
    def __init__(self, ble, name=""):
        # Initialize the BLE interface and register the custom service
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._handle,),) = self._ble.gatts_register_services((_SERVICE,))
        self._connections = set()

        # If no name is provided, generate one based on the MAC address
        if len(name) == 0:
            name = 'Pico %s' % ubinascii.hexlify(self._ble.config('mac')[1], ':').decode().upper()
        print('Device name: %s' % name)

        # Create the advertising payload with the custom service
        self._payload = advertising_payload(
            name=name, services=[_SERVICE_UUID]
        )
        self._advertise()

    def _irq(self, event, data):
        # Handle BLE events
        if event == _IRQ_CENTRAL_CONNECT:
            # A central has connected
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
            print("New connection", conn_handle)
            led.value(1)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            # A central has disconnected
            conn_handle, _, _ = data
            self._connections.remove(conn_handle)
            print("Disconnected", conn_handle)
            led.value(0)
            # Start advertising again to allow a new connection
            self._advertise()
        elif event == _IRQ_GATTS_INDICATE_DONE:
            # Indication confirmation received (not used here)
            conn_handle, value_handle, status = data

    def send_text(self, text):
        # Write the given text to the characteristic value
        self._ble.gatts_write(self._handle, text.encode('utf-8'))
        # Notify all connected centrals about the new value
        for conn_handle in self._connections:
            self._ble.gatts_notify(conn_handle, self._handle)

    def _advertise(self, interval_us=500000):
        print("Starting advertising")
        # Start BLE advertising with the given interval
        self._ble.gap_advertise(interval_us, adv_data=self._payload)
    
    def is_connected(self):
        return len(self._connections) > 0

def demo():
    # Create a BLE instance and a BLEText peripheral
    ble = bluetooth.BLE()
    ble_text = BLEText(ble,"pico2w")

    # Continuously read input from the terminal and send it via BLE
    while True:
        if ble_text.is_connected():
            line = input("Enter text to send via BLE (Ctrl+C to exit): ")
            ble_text.send_text(line)


if __name__ == "__main__":
    demo()
