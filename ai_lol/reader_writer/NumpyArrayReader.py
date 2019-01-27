import sys
import numpy as np


class NumpyArrayReader:
    def __init__(self, file_name):
        self.file = open(file_name, 'rb')

    def load_data(self, nr_of_lines=sys.maxsize):
        array = None
        try:
            array = np.load(self.file)

        except OSError:
            return array
        for __ in range(0, nr_of_lines-1):
            try:
                array = np.append(array, np.load(self.file), axis=0)
            except OSError:
                break
        return array

    def close(self):
        self.file.close()

    def readable(self):
        try:
            return self.file.readable()
        except ValueError:
            return False

    def __del__(self):
        self.close()
# save_data('hoi.npy', [[1, 2, 3], [1, 2, 3]])
# save_data('hoi.npy', [[0, 2, 3], [3, 4, 5]])
# print('------')
# print(load_data('hoi.npy',2,5))
# print('------')
# print('------')
# print(np.load('hoi.npy'))
# print('------')

