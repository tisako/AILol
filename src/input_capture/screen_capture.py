import sys

import cv2

import numpy as np
import screeninfo as screeninfo

if sys.platform != 'win32':  # pragma: no cover
    # This import was only included for CI
    import pyscreenshot as ImageGrab
else:  # pragma: no cover
    # This import will not be covered by the CI
    from PIL import ImageGrab


class ScreenCapture:

    @staticmethod
    def show_screen_capture(screen_capture):
        cv2.imshow('taken picture', cv2.cvtColor(screen_capture, cv2.COLOR_BGR2RGB))

    @staticmethod
    def get_screen_width():
        return screeninfo.get_monitors()[0].width

    @staticmethod
    def get_screen_height():
        return screeninfo.get_monitors()[0].height

    def __init__(self):
        self.width = self.get_screen_width()
        self.height = self.get_screen_height()

    def get_screen_image_relative(self, start_width_proportion=0, end_width_proportion=1, start_height_proportion=0, end_height_proportion=1):
        grab = ImageGrab.grab(bbox=(self.width * start_width_proportion, self.height * start_height_proportion, self.width * end_width_proportion, self.height * end_height_proportion))
        return np.array(grab)

    def get_screen_image(self, position, size):
        print(position)
        if position[0]+size[0] > self.width or position[1]+size[1] > self.height:
            raise ValueError('total width or heigth is bigger than screensize ' + repr(self.width) + 'x' + repr(self.height))
        return np.array(ImageGrab.grab(bbox=(position[0], position[1], position[0] + size[0], position[1] + size[1])))


