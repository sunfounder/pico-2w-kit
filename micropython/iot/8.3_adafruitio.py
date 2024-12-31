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
