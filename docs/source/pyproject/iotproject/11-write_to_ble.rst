8.11 Write data to bluetooth
=================================

In this project, the Raspberry Pi Pico 2 W acts as a peripheral device in a Bluetooth Low Energy (BLE) network. It provides a custom BLE service with a characteristic that supports both reading and notification. A central device, such as a phone, can connect to the Pico W to receive text messages sent via BLE.

The onboard LED shows the connection status: it lights up when a central device connects and turns off when the device disconnects. You can customize the device name or let the system generate it automatically based on its MAC address. The script continuously advertises the BLE service and lets users input text through the terminal, which it then sends to all connected central devices.

1. Build the circuit
+++++++++++++++++++++++++++++++++

This project does not require building any additional circuits. Simply use a USB data cable to connect the Raspberry Pi Pico 2 W to your computer.

2. Run the code
+++++++++++++++++++++++++++++++++

Copy the following code into your IDE. Alternatively, you can find it in our repository at the path: ``pico-2w-kit/micropython/iot/8.11-write_to_ble/8.11-write_to_ble.py``.

Note: This code depends on the ``ble_advertising.py`` file. Make sure to upload it to the Pico board before running the script.

.. code-block:: python

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

3. Read data from bluetooth
+++++++++++++++++++++++++++++++++

To interact with the services and characteristics defined in this code, use a generic Bluetooth® Low Energy central app, such as LightBlue (available for iOS and Android) or nRF Connect (for Android).

This section uses LightBlue as an example to demonstrate how to control the Pico 2 W’s features via Bluetooth. 

a. Install LightBlue

   Download the LightBlue app from the |link_lightblue_apple| (for iOS) or |link_lightblue_google| (for Android).

   .. image:: img/lightblue.png
      :width: 90%

b. Connect to Pico 2 W

   Launch LightBlue and enable location and Bluetooth permissions if prompted. On the **Peripherals** page, search for “pico” in the search bar, and tap to connect to the Pico 2 W device.

   .. image:: img/11-1-connect-pico.png
      :width: 60%
      :align: center

c. Read data form BLE

   After connecting, LightBlue displays detailed information about the Pico 2 W Bluetooth device. Scroll down to locate the **Service (3ec837af-b0c6-4e7e-a8c5-4b31311d98cf)** and **Characteristic (945c4d90-825d-452f-820a-0d8b0cc74a12)**.

   Tap the characteristic 945c4d90-825d-452f-820a-0d8b0cc74a12. The app shows the properties of this characteristic: it supports reading and notifications.

   .. image:: img/11-2-new.png
      :width: 100%

   In the top-right corner, select **"UTF-8 String"** as the data type.

   .. image:: img/11-4-new.png
      :width: 100%
    
   Tap Read to retrieve the current value. Since no data is defined yet, the value displays as “No Value”. Next, return to the computer and enter "hello" in the terminal. Switch back to LightBlue and tap **"Read"** again. The message "hello" now appears, sent from the Pico 2 W to the phone.

   .. image:: img/11-6-new.png
      :width: 100%

   .. image:: img/11-6-micropython.png
      :align: center
      :width: 80%

   To continuously monitor updates, you can also tap **"Subscribe"** to subscribe to this characteristic. When you send new characters from the terminal, they will automatically update and display on your phone.

   .. image:: img/11-8-new.png
      :width: 100%

   