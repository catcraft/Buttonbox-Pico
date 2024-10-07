from machine import Pin
import time
import sys

# Define the pins
pin_2 = Pin(2, Pin.IN, Pin.PULL_UP)  # Input pin with pull-up resistor
led = Pin(25, Pin.OUT)  # Internal LED on GPIO 25

# Function to blink the LED
def blink_led(times, interval):
    for _ in range(times):
        led.on()  # Turn on the LED
        time.sleep(interval)  # Wait for the specified interval
        led.off()  # Turn off the LED
        time.sleep(interval)  # Wait for the specified interval

# Function to handle the handshake
def handshake():
    while True:
        # Wait for the "SYN" message
        v = sys.stdin.readline().strip()
        if "syn" in v.lower():
            print('syn-ack\n')  # Send SYN-ACK response
            time.sleep(0.2)
            v = sys.stdin.readline().strip()
            if "ack" in v.lower():
                blink_led(3, 0.2)  # Blink twice on successful handshake
                return True
        time.sleep(0.1)  # Avoid busy waiting

# Start the handshake process
handshake()

# Main loop to check pin state (if needed)
while True:
    v = sys.stdin.readline().strip()
    if "syn" in v.lower():
        handshake()
    current_state = pin_2.value()
    if not current_state:
        led.on()
    else:
        led.off()
    time.sleep(0.1)

