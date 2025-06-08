import keyboard
import time

def on_key_event(event):
    # If it's a left alt key event, suppress it completely
    if event.name == 'left alt':
        return False
    
    # If it's a key press and left alt is being held
    if keyboard.is_pressed('left alt') and event.event_type == keyboard.KEY_DOWN:
        # Ignore if the key pressed is alt itself
        if event.name == 'alt':
            return False
            
        # First suppress the key completely
        keyboard.send('backspace')
        # Check if left alt or caps lock is pressed

        keyboard.write('\mathcal{'+f"{event.name.upper()}"+'}')
        # Return False to suppress the original key event
        return False

    return True

print("Setting up keyboard hook...")
# Remove any existing hooks first
keyboard.unhook_all()
# Add our new hook
keyboard.hook(on_key_event)

print("Program is running. Left Alt + key will wrap in brackets.")
print("If left alt or caps lock is pressed, the letter will be UPPERCASE.")
print("Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program...")
    keyboard.unhook_all()

    