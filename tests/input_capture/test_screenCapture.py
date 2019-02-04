from unittest import TestCase

import numpy.testing as npt
from testfixtures import mock

from src.input_capture.ScreenCapture import ScreenCapture


class TestScreenCapture(TestCase):
    def setUp(self):
        self.capture = ScreenCapture()

    @mock.patch('PIL.ImageGrab.grab')
    def test_capture_center_of_shown_screen(self, mock_image_grab):
        mock_image_grab.return_value = [1, 2, 3]
        input_image = self.capture.get_screen_image_relative(0.4, 0.6, 0.4, 0.6)
        npt.assert_array_equal(input_image, [1, 2, 3])
        mock_image_grab.assert_called_once_with(bbox=(768.0, 432.0, 1152.0, 648.0))
