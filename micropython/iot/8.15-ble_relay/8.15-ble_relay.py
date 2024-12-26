import bluetooth
import random
import struct
import time
from ble_example.ble_advertising import advertising_payload
from machine import Pin
import time

from micropython import const

relay = machine.Pin(15, machine.Pin.OUT)

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

_FLAG_READ = const(0x0002)
_FLAG_WRITE_NO_RESPONSE = const(0x0004)
_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

_RELAY_UUID = bluetooth.UUID("46719f98-3141-4bbb-aede-47a7630d024b")
_SWITCH_CHAR = (
    bluetooth.UUID("08b82cd0-6877-4308-b08d-a32520c327a2"),
    _FLAG_READ | _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
)
_RELAY_SERVICE = (
    _RELAY_UUID,
    (_SWITCH_CHAR,),
)


class BLERelay:
    def __init__(self, ble, name="ble-relay"):

        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)

        handles = self._ble.gatts_register_services((_RELAY_SERVICE,))
        # print("Registered handles:", handles)

        ((self._handle_note,),) = handles
        self._connections = set()

        self._write_callback = None

        self._payload = advertising_payload(name=name, services=[_RELAY_UUID])
        self._advertise()

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            print("New connection", conn_handle)
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            print("Disconnected", conn_handle)
            self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            conn_handle, value_handle = data
            value = self._ble.gatts_read(value_handle)
            # print("Write event: conn_handle={}, value_handle={}, value={}".format(conn_handle, value_handle, value))
            if value_handle == self._handle_note and self._write_callback:
                self._write_callback(value)
                

    def is_connected(self):
        return len(self._connections) > 0

    def _advertise(self, interval_us=500000):
        print("Starting advertising")
        self._ble.gap_advertise(interval_us, adv_data=self._payload)

    def on_write(self, callback):
        self._write_callback = callback

def relay_update(data):
    print("Receive:", data)

    decoded_data = int(data.decode('utf-8').rstrip('\x00'))

    # print(decoded_data)

    relay.value(decoded_data)


def demo():
    ble = bluetooth.BLE()
    relay = BLERelay(ble,"pico2w")

    while True:
        if relay.is_connected():
            relay.on_write(relay_update)
        # time.sleep_ms(100)

if __name__ == "__main__":
    demo()