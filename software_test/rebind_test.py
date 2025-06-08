import keyboard
import time

def on_key_event(event):
    # If it's a right shift key event, suppress it completely
    if event.name == 'right shift':
        return False
    
    # If it's a key press and right shift is being held
    if keyboard.is_pressed('right shift') and event.event_type == keyboard.KEY_DOWN:
        # First suppress the key completely
        keyboard.send('backspace')
        # Check if left shift or caps lock is pressed
        should_use_uppercase = keyboard.is_pressed('left shift') or keyboard.is_pressed('caps lock')
        # Write our bracketed version, using uppercase if left shift or caps lock is pressed
        key_to_write = event.name.upper() if should_use_uppercase else event.name.lower()
        keyboard.write('\mathcal{'+f"{key_to_write}"+'}')
        # Return False to suppress the original key event
        return False
    
    return True

print("Setting up keyboard hook...")
# Remove any existing hooks first
keyboard.unhook_all()
# Add our new hook
keyboard.hook(on_key_event)

print("Program is running. Right shift + key will wrap in brackets.")
print("If left shift or caps lock is pressed, the letter will be UPPERCASE.")
print("Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program...")
    keyboard.unhook_all()

    