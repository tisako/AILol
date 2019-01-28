import numpy as np
import keyboard


class KeyCapture:
    def __init__(self, keys):
        self.keys = np.array(keys)

    def capture_keys(self):
        is_key_pressed = np.empty(self.keys.shape)
        for idx, key in enumerate(self.keys):
            is_key_pressed[idx] = keyboard.is_pressed(key);

        return is_key_pressed
