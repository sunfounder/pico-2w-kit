import machine
import utime

# Initialize GP14 as an input
slide_switch = machine.Pin(14, machine.Pin.IN)

while True:
    switch_state = slide_switch.value()
    if switch_state == 1:
        print("Switch is toggled to the LEFT!")
    else:
        print("Switch is toggled to the RIGHT!")
    utime.sleep(0.5)