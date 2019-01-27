import numpy as np


class NumpyArrayWriter:
    @staticmethod
    def save_data(file_name, array):
        file = open(file_name, 'ab')
        np.save(file, [array])
        file.close()
