from unittest import TestCase

import numpy as np
import numpy.testing as npt
from pathlib import Path
from testfixtures import TempDirectory

from src.reader_writer.NumpyArrayWriter import NumpyArrayWriter


class TestNumpyArrayWriter(TestCase):
    def setUp(self):
        self.d = TempDirectory()

        self.file_path = self.d.path + '\\test.npy'
        self.file = Path(self.file_path)
        self.assertFalse(self.file.is_file())

    def test_save_data(self):
        NumpyArrayWriter.save_data(self.file_path, [1, 2, 3, 4])

        self.assertTrue(self.file.is_file())
        
    def test_save_data_contains_saved_data(self):
        input_array = [1, 2, 3, 4]

        NumpyArrayWriter.save_data(self.file_path, input_array)

        data = np.load(self.file_path)
        npt.assert_array_equal([input_array], data)

    def test_save_multiple_data_points(self):
        input_array = [1, 2, 3, 4]
        second_input = [1, 2, 3, 4, 5]

        NumpyArrayWriter.save_data(self.file_path, input_array)
        NumpyArrayWriter.save_data(self.file_path, second_input)

        data = np.load(self.file_path)
        npt.assert_array_equal([input_array], data)

        second_data = np.load(self.file_path)
        npt.assert_array_equal([input_array], second_data)

    def tearDown(self):
        self.d.cleanup()
