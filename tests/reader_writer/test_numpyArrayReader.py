from unittest import TestCase

import numpy.testing as npt
from testfixtures import TempDirectory

from src.reader_writer.numpy_array_reader import NumpyArrayReader
from src.reader_writer.numpy_array_writer import NumpyArrayWriter


class TestNumpyArrayReader(TestCase):
    input_array = [1, 2, 3, 4]

    def setUp(self):
        self.d = TempDirectory()
        NumpyArrayWriter.save_data(self.d.path + '\\test.npy', self.input_array)
        self.reader = NumpyArrayReader(self.d.path + '\\test.npy')

    def test_resource_should_close_it_self(self):
        self.assertTrue(self.reader.readable())

    def test_close(self):
        self.reader.close()

        self.assertFalse(self.reader.readable(), 'file is not closed')

    def test_read(self):
        data = self.reader.load_data()

        npt.assert_array_equal([self.input_array], data)

    def test_read_multiple_lines(self):
        second_input = [123, 4, 5, 6]
        NumpyArrayWriter.save_data(self.d.path + '\\test.npy', second_input)

        data = self.reader.load_data()

        npt.assert_array_equal([self.input_array, second_input], data)

    def test_read_one_line_multiple_times(self):
        second_input = [123, 4, 5, 6]
        NumpyArrayWriter.save_data(self.d.path + '\\test.npy', second_input)

        data = self.reader.load_data(nr_of_lines=1)

        npt.assert_array_equal([self.input_array], data)

        data = self.reader.load_data(nr_of_lines=1)

        npt.assert_array_equal([second_input], data)

        data = self.reader.load_data(nr_of_lines=1)

        self.assertIsNone(data)

    def tearDown(self):
        self.reader.__del__()
        self.d.cleanup()
