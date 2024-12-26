import bluetooth
import random
import struct
import time
from ble_example.ble_advertising import advertising_payload
from machine import Pin, PWM
import time

from micropython import const

buzzer = PWM(Pin(15)) 

NOTES = {
    'NOTE_C4': 262,
    'NOTE_D4': 294,
    'NOTE_E4': 330,
    'NOTE_F4': 349,
    'NOTE_G4': 392,
    'NOTE_A4': 440,
    'NOTE_B4': 494,
    'NOTE_C5': 523
}

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

_FLAG_READ = const(0x0002)
_FLAG_WRITE_NO_RESPONSE = const(0x0004)
_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

_PIANO_UUID = bluetooth.UUID("952cc3a7-1801-4c07-b141-e1e3964f54b5")
_NOTE_CHAR = (
    bluetooth.UUID("ea30277b-d7a5-4eeb-af70-6179c45d7ee6"),
    _FLAG_READ | _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
)
_PIANO_SERVICE = (
    _PIANO_UUID,
    (_NOTE_CHAR,),
)


class BLEPiano:
    def __init__(self, ble, name="ble-piano"):

        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)

        handles = self._ble.gatts_register_services((_PIANO_SERVICE,))
        # print("Registered handles:", handles)

        ((self._handle_note,),) = handles
        self._connections = set()

        self._write_callback = None

        self._payload = advertising_payload(name=name, services=[_PIANO_UUID])
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

def note_update(data):
    print("Receive:", data)

    decoded_data = data.decode('utf-8').rstrip('*\x00')

    buzzer.freq(NOTES[decoded_data])
    buzzer.duty_u16(32768)  
    time.sleep(0.15)
    buzzer.duty_u16(0)  

def demo():
    ble = bluetooth.BLE()
    piano = BLEPiano(ble,"pico2w")

    while True:
        if piano.is_connected():
            piano.on_write(note_update)
        # time.sleep_ms(100)

if __name__ == "__main__":
    demo()