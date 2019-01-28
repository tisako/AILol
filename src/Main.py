from tkinter import Tk

import cv2
import time

from src.frontend.TrainDataCollector import TrainDataCollector
from src.input_capture.ScreenCapture import ScreenCapture

root = Tk()
root.geometry("400x300")
app = TrainDataCollector(root)

root.mainloop()

# last_time = time.time()
# stopTime = time.time()
# timeout_time = 0
# show_picture = True
# capture = ScreenCapture()
#
# while True:
#     print_screen = capture.get_screen_image()
#     print('loop took {} seconds'.format(time.time() - last_time))
#     last_time = time.time()
#     if show_picture:
#         capture.show_screen_capture(print_screen)
#     if 0 < timeout_time < time.time() - stopTime or cv2.waitKey(25) & 0xFF == ord('q'):
#         break
#
# while True:
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
