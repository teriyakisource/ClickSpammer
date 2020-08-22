
import threading
from pynput.keyboard import Listener, KeyCode, Controller
from pynput.mouse import Controller, Button
import time
 
f = open("hotkey.txt", "r")#opens hotkey file
hotkey = f.read()

print("hotkey: " + hotkey[0])

delay = 0.020
button = Button.left
ss_key = KeyCode(char=hotkey) #start stop key
 
class Click(threading.Thread): #threading to run the process simultaneously
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
 
    def start_click(self):
        self.running = True
 
    def stop_click(self):
        self.running = False
 
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(button) 
                time.sleep(delay)
 
print("Connecting...")
mouse = Controller()
keypress_thread = Click(delay)
keypress_thread.start() #starts thread (class with functions in)
 
def on_press(key):
    if key == ss_key: #checking key presses to start the function
        if keypress_thread.running:
            keypress_thread.stop_click()
 
        else:
            keypress_thread.start_click()
 
with Listener(on_press=on_press) as listener: #listening for key presses
    print("Connected!")
    listener.join()
