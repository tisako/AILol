import numpy as np
import keyboard
from PIL import ImageGrab
import win32api


def get_screen_image(start_width_proportion=11.5 / 35, end_width_proportion=22.5 / 35, start_height_proportion=17.5 / 20.5, end_height_proportion=1):
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    left_mouse_button = win32api.GetKeyState(0x01)

    return np.array(ImageGrab.grab(bbox=(width * start_width_proportion, height * start_height_proportion, width * end_width_proportion, height * end_height_proportion))), np.array([
        keyboard.is_pressed('q'),
        keyboard.is_pressed('w'),
        keyboard.is_pressed('e'),
        keyboard.is_pressed('r'),
        keyboard.is_pressed('d'),
        keyboard.is_pressed('f'),
        keyboard.is_pressed('1'),
        keyboard.is_pressed('2'),
        keyboard.is_pressed('3'),
        keyboard.is_pressed('4'),
        keyboard.is_pressed('5'),
        keyboard.is_pressed('6'),
        keyboard.is_pressed('space')
    ]), np.array([win32api.GetCursorPos(), left_mouse_button != 0 and left_mouse_button != 1])

