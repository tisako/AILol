import GrabScreenByRatios
import cv2
import time


last_time = time.time()
stopTime = time.time()
timeout_time = 0
show_picture = True

while True:
    print_screen, keyboard, mouse = GrabScreenByRatios.get_screen_image(0, 1, 0, 1)
    print('loop took {} seconds'.format(time.time() - last_time))
    print(keyboard)
    last_time = time.time()
    if show_picture:
        cv2.imshow('taken picture', cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
    if 0 < timeout_time < time.time() - stopTime or cv2.waitKey(25) & 0xFF == ord('q'):
        break

while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
