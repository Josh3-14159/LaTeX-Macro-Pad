import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)

# Set up pin 15 as an input with a pull-up resistor
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Wait for USB to initialize
time.sleep(2)

while True:
    if not button.value:  # Button is pressed (pin is low)
        keyboard.press(Keycode.SHIFT)
        time.sleep(0.1)  # Small delay to prevent multiple triggers
    if button.value:
        keyboard.release(Keycode.SHIFT)

    time.sleep(0.01)  # Small delay to prevent CPU hogging