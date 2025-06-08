import keyboard
import time

# Track the state of left ctrl
left_ctrl_pressed = False

def on_key_event(event):
    global left_ctrl_pressed
    
    # Handle left ctrl key events
    if event.name == 'left ctrl':
        if event.event_type == keyboard.KEY_DOWN:
            left_ctrl_pressed = True
        elif event.event_type == keyboard.KEY_UP:
            left_ctrl_pressed = False
        return False  # Suppress ctrl key
    
    # If left ctrl is held and a key is pressed
    if left_ctrl_pressed and event.event_type == keyboard.KEY_DOWN:
        # Ignore if it's a modifier key
        if event.name in {'left ctrl', 'right ctrl', 'left shift', 'right shift', 'left alt', 'right alt', 'caps lock'}:
            return True
            
        # Get the actual key being pressed
        key = event.name
        print(f"Detected key press with ctrl: {key}")  # Debug print
        
        # Suppress the original key
        keyboard.send('backspace')
        # Write the LaTeX command
        keyboard.write('\\mathcal{' + key.upper() + '}')
        return False  # Suppress the original key
    
    return True

print("Setting up keyboard hook...")
# Remove any existing hooks first
keyboard.unhook_all()
# Add our new hook
keyboard.hook(on_key_event)

print("Program is running. Left ctrl + key will type \\mathcal{KEY}.")
print("Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program...")
    keyboard.unhook_all()