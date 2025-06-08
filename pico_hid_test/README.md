# Pico HID Keyboard Test

A simple test program for the Raspberry Pi Pico that demonstrates USB HID keyboard functionality.

## Hardware Setup

1. Connect a button to GPIO 15 and ground (with a 10kΩ pull-up resistor if not using internal pull-up)
2. The built-in LED on GPIO 25 will be used as an indicator

## Software Setup

1. Install the latest MicroPython firmware on your Pico
2. Install the required libraries:
   ```
   mpremote mip install adafruit-circuitpython-hid
   ```
3. Copy `main.py` to your Pico

## Usage

1. Connect the Pico to your computer via USB
2. Press the button connected to GPIO 15
3. The Pico will send the sequence "ABC" as keyboard input
4. The built-in LED will light up while sending keystrokes

## Notes

- The program uses the internal pull-up resistor on GPIO 15
- The button should be connected between GPIO 15 and ground
- The built-in LED is on GPIO 25
- The program includes debouncing through software delays 