import time
from unittest import TestCase

import numpy as np

from src.input_capture.ScreenCapture import ScreenCapture


class TestScreenCapture(TestCase):
    def setUp(self):
        self.capture = ScreenCapture()
        self.capture.show_screen_capture(np.load('ImageToShowScreenCapture.npy')[0])
        time.sleep(0.5)

    def test_capture_center_of_shown_screen(self):
        test_img = np.load('TestDataScreenCapture.npy')
        input_image = self.capture.get_screen_image(0.4, 0.6, 0.4, 0.6)
        self.assertFalse((np.array(input_image) - test_img).any(), 'An element is different in input ' + input_image.__str__() + ' and output' + test_img.__str__())