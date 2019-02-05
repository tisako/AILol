import sys
from unittest import TestCase

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

        monitor_patcher = mock.patch('screeninfo.Monitor')
        monitor = monitor_patcher.start()
        monitor.width = 1920
        monitor.height = 1080
        patcher = mock.patch('screeninfo.get_monitors')
        self.mock_screeninfo = patcher.start()
        self.mock_screeninfo.return_value = [monitor]
        self.addCleanup(patcher.stop)
        self.addCleanup(monitor_patcher.stop)

        self.capture = ScreenCapture()

    def test_capture_center_of_shown_screen(self):
        print(self.capture.get_screen_height())
        self.mock_image_grab.return_value = [1, 2, 3]
        input_image = self.capture.get_screen_image_relative(0.4, 0.6, 0.4, 0.6)
        npt.assert_array_equal(input_image, [1, 2, 3])
        self.mock_image_grab.assert_called_once_with(bbox=(768.0, 432.0, 1152.0, 648.0))
