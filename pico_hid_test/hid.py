from machine import Pin
import struct
import time

class Keyboard:
    def __init__(self):
        self.keyboard_report = bytearray(8)
        self.keyboard_report[0] = 0x01  # Report ID for keyboard
        self._send_report(self.keyboard_report)

    def _send_report(self, report):
        # This is a simplified version that just prints what would be sent
        print(f"Sending report: {report.hex()}")
        time.sleep(0.01)  # Small delay to simulate USB communication

    def press(self, keycode):
        self.keyboard_report[2] = keycode
        self._send_report(self.keyboard_report)

    def release(self, keycode):
        self.keyboard_report[2] = 0
        self._send_report(self.keyboard_report)

    def release_all(self):
        self.keyboard_report[2] = 0
        self._send_report(self.keyboard_report)

class Keycode:
    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0A
    H = 0x0B
    I = 0x0C
    J = 0x0D
    K = 0x0E
    L = 0x0F
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1A
    X = 0x1B
    Y = 0x1C
    Z = 0x1D
    SPACE = 0x2C
    ENTER = 0x28
    ESCAPE = 0x29
    BACKSPACE = 0x2A
    TAB = 0x2B 