import time
from unittest import TestCase

import numpy as np
import numpy.testing as npt


from src.input_capture.ScreenCapture import ScreenCapture
from tests import FileHelper


class TestScreenCapture(TestCase):
    def setUp(self):

        self.current_dir = FileHelper.get_current_dir()
        self.capture = ScreenCapture()
        self.capture.show_screen_capture(np.load(self.current_dir + '/ImageToShowScreenCapture.npy')[0])
        time.sleep(0.5)

    def test_capture_center_of_shown_screen(self):
        test_img = np.load(self.current_dir + '/TestDataScreenCapture.npy')
        input_image = self.capture.get_screen_image_relative(0.4, 0.6, 0.4, 0.6)
        npt.assert_array_equal([input_image], test_img)
