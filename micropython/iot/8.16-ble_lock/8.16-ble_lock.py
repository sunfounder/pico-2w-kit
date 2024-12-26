import bluetooth
import random
import struct
import time
from ble_example.ble_advertising import advertising_payload
from machine import Pin
import time

import struct
from micropython import const

servo = machine.PWM(machine.Pin(15))
servo.freq(50)

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

_FLAG_READ = const(0x0002)
_FLAG_WRITE_NO_RESPONSE = const(0x0004)
_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

_LOCK_UUID = bluetooth.UUID("f3ac7f80-5045-47b0-88fe-24d858e2e92f")
_SWITCH_CHAR = (
    bluetooth.UUID("808b6a74-8d38-4114-8cb7-0ac9465db42d"),
    _FLAG_READ | _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
)
_LOCK_SERVICE = (
    _LOCK_UUID,
    (_SWITCH_CHAR,),
)


class BLELock:
    def __init__(self, ble, name="PICO-LOCK"):

        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)

        handles = self._ble.gatts_register_services((_LOCK_SERVICE,))
        # print("Registered handles:", handles)

        ((self._handle_note,),) = handles
        self._connections = set()

        self._write_callback = None

        self._payload = advertising_payload(name=name, services=[_LOCK_UUID])
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

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    pin.duty_u16(duty)

def lock_update(data):
    print("Receive:", data)

    decoded_data = struct.unpack('I', data)[0]

    if decoded_data == 1:
        servo_write(servo,90)
    else:
        servo_write(servo,0)


def demo():
    ble = bluetooth.BLE()
    piano = BLELock(ble,"pico2w")

    while True:
        if piano.is_connected():
            piano.on_write(lock_update)
        # time.sleep_ms(100)

if __name__ == "__main__":
    demo()