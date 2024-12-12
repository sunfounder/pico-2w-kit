import machine
import utime

# Initialize GP14 as an input pin
pir_sensor = machine.Pin(14, machine.Pin.IN)

def motion_detected(pin):
    print("Motion detected!")

# Set up an interrupt on the rising edge
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

# Main loop does nothing, interrupt handles motion detection
while True:
    utime.sleep(1)