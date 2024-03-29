import time
import threading
from pynput.mouse import Button, Controller as MouseCountroller
from pynput.keyboard import (
    Listener,
    KeyCode,
    Key,
    Controller as KeyboardController)
import random

mouse_delay = random.randint(3, 12)
keyboard_delay = random.uniform(0.05, 3)

button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

clicked_count = 0
keyboard_count = 0


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.mouse_delay = delay
        self.button = button
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        global clicked_count
        while self.program_run:
            while self.running:
                mouse.click(self.button)

                clicked_count = clicked_count + 1

                time.sleep(self.mouse_delay)
            time.sleep(0.1)


class KeyboardInput(threading.Thread):
    def __init__(self, delay):
        super(KeyboardInput, self).__init__()
        self.keyboard_delay = delay
        self.running = False
        self.program_run = True

    def start_input(self):
        self.running = True

    def stop_input(self):
        self.running = False

    def exit(self):
        self.stop_input()
        self.program_run = False

    def run(self):
        global keyboard_count
        while self.program_run:
            while self.running:
                # random_key = random.choice(list(Key))
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                # Use a random key so we don't press the same key all the time.
                # keyboard.press(random_key)
                # keyboard.release(random_key)

                keyboard_count = keyboard_count + 1
                time.sleep(self.keyboard_delay)
            time.sleep(0.1)


mouse = MouseCountroller()
mouse_thread = ClickMouse(mouse_delay, button)
mouse_thread.start()

keyboard = KeyboardController()
keyboard_thread = KeyboardInput(keyboard_delay)
keyboard_thread.start()


def on_press(key):
    if key == start_stop_key:

        if mouse_thread.running:
            mouse_thread.stop_clicking()
        else:
            mouse_thread.start_clicking()

        if keyboard_thread.running:
            keyboard_thread.stop_input()
        else:
            keyboard_thread.start_input()

    elif key == exit_key:
        mouse_thread.exit()
        keyboard_thread.exit()
        listener.stop()
        print('M Count: ', clicked_count)
        print('K Count: ', keyboard_count)
        print('Exited')


if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        print("Start")
        listener.join()
        print("End")