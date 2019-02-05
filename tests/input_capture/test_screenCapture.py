import cv2
import sys
from unittest import TestCase

import numpy as np
import numpy.testing as npt
from testfixtures import mock

from src.input_capture.ScreenCapture import ScreenCapture


class TestScreenCapture(TestCase):
    def setUp(self):
        if sys.platform != 'win32':
            patcher = mock.patch('pyscreenshot.grab')
            self.mock_image_grab = patcher.start()
            self.addCleanup(patcher.stop)
            super(TestScreenCapture, self).setUp()
        else:
            patcher = mock.patch('PIL.ImageGrab.grab')
            self.mock_image_grab = patcher.start()
            self.addCleanup(patcher.stop)
            super(TestScreenCapture, self).setUp()

        self.mock_image_grab.return_value = [1, 2, 3]

        monitor_patcher = mock.patch('screeninfo.Monitor')
        monitor = monitor_patcher.start()
        monitor.width = 1920
        monitor.height = 1080
        patcher = mock.patch('screeninfo.get_monitors')
        self.mock_screen_info = patcher.start()
        self.mock_screen_info.return_value = [monitor]
        self.addCleanup(patcher.stop)
        self.addCleanup(monitor_patcher.stop)

        self.capture = ScreenCapture()

    def test_capture_center_of_shown_screen(self):
        input_image = self.capture.get_screen_image_relative(0.4, 0.6, 0.4, 0.6)
        npt.assert_array_equal(input_image, [1, 2, 3])
        self.mock_image_grab.assert_called_once_with(bbox=(768.0, 432.0, 1152.0, 648.0))

    def test_capture_part_of_screen(self):
        input_image = self.capture.get_screen_image((0.4, 0.6), (0.4, 0.6))
        npt.assert_array_equal(input_image, [1, 2, 3])
        self.mock_image_grab.assert_called_once_with(bbox=(0.4, 0.6, 0.8, 1.2))

    def test_error_raised_if_size_to_big(self):
        self.assertRaises(ValueError, self.capture.get_screen_image, (0.4, 0.6), (1920, 1080))

    def test_show_image(self):
        patch = mock.patch('cv2.imshow')
        patch1 = mock.patch('cv2.cvtColor')
        mocked1 = patch1.start()
        mocked1.return_value = [2, 3, 1]
        mocked = patch.start()

        self.capture.show_screen_capture([1, 2, 3])

        mocked1.assert_called_with([1, 2, 3], cv2.COLOR_BGR2RGB)
        mocked.assert_called_with('taken picture', [2, 3, 1])
        patch1.stop()
        patch.stop()

