.. _py_iot_adafruitio:

8.3 Temperature and Humidity Monitoring via @AdafruitIO
==========================================================

In this project, you'll explore Adafruit IO, a powerful and user-friendly IoT platform. Using MicroPython, your Raspberry Pi Pico W connects to Wi-Fi and integrates with Adafruit IO to demonstrate its real-time communication and control capabilities.

The project features a DHT11 sensor that measures temperature and humidity, sending data to the Adafruit IO dashboard using the MQTT protocol. Additionally, the status of a virtual switch on the dashboard allows remote control of an LED. The code also utilizes the Adafruit IO REST API during setup to synchronize the LED’s state with the hardware, ensuring smooth operation.

By combining MQTT for real-time data exchange and REST APIs for setup synchronization, this project provides an excellent introduction to IoT programming concepts.

1. Build the circuit
+++++++++++++++++++++++++++++++++

.. image:: img/wiring/8.13_bb.png
   :width: 90%

.. raw:: html

   <br/>

2. Setting up the Adafruit IO Dashboard
+++++++++++++++++++++++++++++++++++++++++

#. Visit |link_adafruit_io| and click **Start for Free** to create a free account.

   .. image:: img/3-1_get_start.png
      :width: 90%

#. Fill out the sign-up form to create your account.

   .. image:: img/3-2_sign_up.png
      :width: 90%

#. Once your account is created, navigate back to Adafruit IO. Click on **Dashboards**, then select **New Dashboard**.

   .. image:: img/3-3_create_dashboard.png
      :width: 90%

#. Create a **New Dashboard**.

   .. image:: img/3-4_create_dashboard_2.png
      :width: 75%

#. Enter the newly created **Dashboard** and create a new block.

   .. image:: img/3-5_create_block.png
      :width: 90%

   .. image:: img/3-6_create_block_2.png
      :width: 90%

#. Add a **Toggle Block** to your dashboard.

   .. image:: img/3-7_toggle_block.png
      :width: 90%

#. Create a new feed for this block. This feed will control the LED, so name it LED.

   .. image:: img/3-8_connect_feed.png
      :width: 90%

#. Select the **LED** feed and proceed to the next step.

   .. image:: img/3-9_connect_feed_2.png
      :width: 90%

#. Complete the block settings (mainly Block Title, On Text, and Off Text), then click on the **Create block** button at the bottom right to finish.

   .. image:: img/3-10_create_block_2.png
      :width: 90%

#. Create two additional **Text Blocks** to display temperature and humidity. For these blocks, create feeds named **temperature** and **humidity**.

   .. image:: img/3-11_text_block.png
      :width: 90%

   .. image:: img/3-12_connect_feed.png
      :width: 90%

#. After creating the blocks, your dashboard should look similar to this:

   .. image:: img/3-13_connect_feed.png
      :width: 90%

#. Adjust the layout as needed using the **Edit Layout** option.

   .. image:: img/3-14_edit_layout.png
      :width: 50%

#. Click on **API Key** to view your username and API key. Make a note of these credentials, as they will be required in your code.

   .. image:: img/3-15_api_key.png
      :width: 90%

   .. image:: img/3-16_api_key.png
      :width: 90%


3. Run the Code
+++++++++++++++++++++++++++++++++

#. Then, connect pico 2 w board to the computer using the USB cable.

#. Open the ``8.3_adafruitio.py`` file under the path of ``pico-2w-kit/micropython/iot/8.3_adafruitio``, or copy this code into your IDE.
      
   .. note::
      This code depends on the ``lib/umqtt/simple.mpy`` file. Make sure to upload it to the Pico board before running the script.

   .. note::
      Before running the code, ensure you have updated the Wi-Fi credentials and Adafruit IO configuration (as mentioned in Step 2.13).

   .. code-block:: python
      :emphasize-lines: 10,11,16,17

      import network
      import time
      from umqtt.simple import MQTTClient
      from machine import Pin
      import utime
      import dht
      import urequests
      
      # Wi-Fi configuration
      SSID = "your_wifi_ssid"            # modify this
      PASSWORD = "your_password"         # modify this
      
      # Adafruit IO configuration
      AIO_SERVER = "io.adafruit.com"
      AIO_PORT = 1883
      AIO_USER = "your_name_adafruitIO"  # modify this
      AIO_KEY = "aio_xxxxxxxxx"          # modify this
      AIO_FEED_HUM = "humidity"
      AIO_FEED_TEMP = "temperature"
      AIO_FEED_LED = "led"
      
      # DHT11 and LED configuration
      sensor = dht.DHT11(Pin(15))
      led = Pin("LED", Pin.OUT)
      
      # Timestamp for periodic tasks
      last_update = time.ticks_ms()
      
      # Connect to Wi-Fi
      def connect_wifi():
         wlan = network.WLAN(network.STA_IF)
         wlan.active(True)
         wlan.connect(SSID, PASSWORD)
         while not wlan.isconnected():
            print("Connecting to WiFi...")
            time.sleep(1)
         print("WiFi Connected:", wlan.ifconfig())
      
      # Handle received MQTT messages
      def message_callback(topic, msg):
         global led
         message = msg.decode()
         print("Received message on topic {}: {}".format(topic, message))
         if message.lower() == "on":
            led.value(1)  # Turn LED on
         elif message.lower() == "off":
            led.value(0)  # Turn LED off
      
      # Connect to Adafruit IO
      def connect_adafruit():
         client = MQTTClient("pico", AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
         client.set_callback(message_callback)
         client.connect()
         print("Connected to Adafruit IO")
         return client
      
      # Fetch the last value from a feed
      def get_feed_value(feed_name):
         url = f"https://io.adafruit.com/api/v2/{AIO_USER}/feeds/{feed_name}/data/last"
         headers = {"X-AIO-Key": AIO_KEY}
         try:
            response = urequests.get(url, headers=headers)
            if response.status_code == 200:
                  data = response.json()
                  print(f"Feed {feed_name} last value: {data['value']}")
                  return data["value"]
            else:
                  print(f"Failed to get feed value: {response.status_code}")
                  return None
         except Exception as e:
            print("Error fetching feed value:", e)
            return None
      
      # Main program
      def main():
         global last_update
      
         connect_wifi()
         client = connect_adafruit()
      
         # Subscribe to LED feed
         led_topic = f"{AIO_USER}/feeds/{AIO_FEED_LED}"
         client.subscribe(led_topic)
         print(f"Subscribed to {led_topic}")
      
         # Sync initial LED state
         led_state = get_feed_value(AIO_FEED_LED)
         if led_state:
            if led_state.lower() == "on":
                  led.value(1)
            elif led_state.lower() == "off":
                  led.value(0)
      
         while True:
            # Check for new MQTT messages
            client.check_msg()
      
            # Update DHT11 data every 10 seconds
            if time.ticks_diff(time.ticks_ms(), last_update) > 10000:
                  try:
                     sensor.measure()
                     temperature = str(sensor.temperature)  # Temperature
                     humidity = str(sensor.humidity)        # Humidity
      
                     print("Temperature: {}C   Humidity: {}%".format(temperature, humidity))
      
                     # Publish data to Adafruit IO
                     client.publish(f"{AIO_USER}/feeds/{AIO_FEED_TEMP}", temperature)
                     client.publish(f"{AIO_USER}/feeds/{AIO_FEED_HUM}", humidity)
      
                     last_update = time.ticks_ms()  # Update timestamp
                  except Exception as e:
                     print("Error:", e)
      
      try:
         main()
      except Exception as e:
         print("Error:", e)

#. Once the code is successfully saved to the Pico and executed, you will see the following message in the serial monitor, confirming successful communication with Adafruit IO.
   
   .. image:: img/3-17_micropython.png
      :width: 90%

#. Navigate back to Adafruit IO. You can now view the temperature and humidity readings on the dashboard or use the LED toggle switch to control the on/off state of the external LED connected to the circuit.

   .. image:: img/3-18_adafruitio.png
      :width: 90%