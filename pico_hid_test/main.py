import time
from machine import Pin
from hid import Keyboard, Keycode

# Initialize the keyboard
keyboard = Keyboard()

# Set up the button (GPIO 15) with internal pull-up
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Set up the LED (GPIO 25, built-in LED)
led = Pin(25, Pin.OUT)

print("Pico HID Keyboard Test")
print("Press the button to send test keystrokes")

while True:
    if button.value() == 0:  # Button is pressed (active low)
        led.value(1)  # Turn on LED
        
        # Send some test keystrokes
        keyboard.press(Keycode.A)
        time.sleep(0.1)
        keyboard.release(Keycode.A)
        
        time.sleep(0.1)
        
        keyboard.press(Keycode.B)
        time.sleep(0.1)
        keyboard.release(Keycode.B)
        
        time.sleep(0.1)
        
        keyboard.press(Keycode.C)
        time.sleep(0.1)
        keyboard.release(Keycode.C)
        
        # Wait for button release
        while button.value() == 0:
            time.sleep(0.1)
        
        led.value(0)  # Turn off LED
    
    time.sleep(0.1)  # Small delay to prevent CPU hogging 