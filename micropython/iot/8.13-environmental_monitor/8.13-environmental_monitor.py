# This example demonstrates a simple temperature sensor peripheral.
#
# The sensor's local value is updated, and it will notify
# any connected central every 10 seconds.

import bluetooth
import random
import struct
import time
import machine
import ubinascii
import dht
from ble_example.ble_advertising import advertising_payload
from micropython import const
from machine import Pin

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_INDICATE_DONE = const(20)

_FLAG_READ = const(0x0002)
_FLAG_NOTIFY = const(0x0010)
_FLAG_INDICATE = const(0x0020)

# org.bluetooth.service.environmental_sensing
_ENV_SENSE_UUID = bluetooth.UUID(0x181A)
# org.bluetooth.characteristic.temperature
_TEMP_CHAR = (
    bluetooth.UUID(0x2A6E),
    _FLAG_READ | _FLAG_NOTIFY | _FLAG_INDICATE,
)
_HUM_CHAR = (
    bluetooth.UUID(0x2A6F),
    _FLAG_READ | _FLAG_NOTIFY | _FLAG_INDICATE,
)
_ENV_SENSE_SERVICE = (
    _ENV_SENSE_UUID,
    (_TEMP_CHAR,_HUM_CHAR),
)

# org.bluetooth.characteristic.gap.appearance.xml
_ADV_APPEARANCE_GENERIC_THERMOMETER = const(768)

class BLETempHumidity:
    def __init__(self, ble, name=""):

        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        
        ((self._temp_handle, self._hum_handle),) = self._ble.gatts_register_services((_ENV_SENSE_SERVICE,))
        self._connections = set()

        # If no name is provided, it will be automatically generated based on the MAC address.
        if len(name) == 0:
            name = 'Pico %s' % ubinascii.hexlify(self._ble.config('mac')[1],':').decode().upper()
        print('Sensor name %s' % name)

        self._payload = advertising_payload(
            name=name, services=[_ENV_SENSE_UUID]
        )
        self._advertise()

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_INDICATE_DONE:
            conn_handle, value_handle, status = data

    def update_values(self, temperature_c, humidity_perc, notify=False, indicate=False):
        # Write the temperature to the temperature characteristic (unit: 0.01°C)
        temp_int = int(temperature_c * 100)
        self._ble.gatts_write(self._temp_handle, struct.pack("<h", temp_int))

        # Write the humidity to the humidity characteristic (unit: 0.01%RH)
        hum_int = int(humidity_perc * 100)
        self._ble.gatts_write(self._hum_handle, struct.pack("<H", hum_int))

        if notify or indicate:
            for conn_handle in self._connections:
                if notify:
                    self._ble.gatts_notify(conn_handle, self._temp_handle)
                    self._ble.gatts_notify(conn_handle, self._hum_handle)
                if indicate:
                    self._ble.gatts_indicate(conn_handle, self._temp_handle)
                    self._ble.gatts_indicate(conn_handle, self._hum_handle)

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)

    def is_connected(self):
        return len(self._connections) > 0

def demo():
    sensor = dht.DHT11(machine.Pin(15))
    led = Pin('LED', Pin.OUT)

    ble = bluetooth.BLE()
    temp_hum = BLETempHumidity(ble,"pico2w")

    counter = 0
    while True:

        if temp_hum.is_connected():
            led.on()
        else:
            led.off()

        try:
            if counter % 10 == 0:
                sensor.measure()
                temperature_c = sensor.temperature
                humidity = sensor.humidity
                
                print("Temp: %.2f C, Hum: %.2f %%" % (temperature_c, humidity))
                temp_hum.update_values(temperature_c, humidity, notify=True, indicate=False)
        except Exception as e:
            print(f"Error: {e}") 
        
        time.sleep_ms(1000)
        counter += 1

if __name__ == "__main__":
    demo()
