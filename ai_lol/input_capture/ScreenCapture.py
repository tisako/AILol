import cv2

import numpy as np
from PIL import ImageGrab
import win32api


class ScreenCapture:

    def __init__(self):
        self.width = win32api.GetSystemMetrics(0)
        self.height = win32api.GetSystemMetrics(1)

    def get_screen_image(self, start_width_proportion=0, end_width_proportion=1, start_height_proportion=0, end_height_proportion=1):
        return np.array(ImageGrab.grab(bbox=(self.width * start_width_proportion, self.height * start_height_proportion, self.width * end_width_proportion, self.height * end_height_proportion)))

    @staticmethod
    def show_screen_capture(screen_capture):
        cv2.imshow('taken picture', cv2.cvtColor(screen_capture, cv2.COLOR_BGR2RGB))
