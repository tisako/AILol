import sys
from threading import Thread
from tkinter import Frame, Entry, Label, StringVar, Button, DISABLED, W, E, S, N, NORMAL

import numpy as np

from src.input_capture.KeyCapture import KeyCapture


class KeyCaptureFrame(Frame):
    def __init__(self, keys_to_capture, master=None):
        Frame.__init__(self, master)
        self.test_capture_keys = False
        self.keys_to_capture_value = keys_to_capture
        self.master = master
        self.thread = None
        self.test_captured_keys = StringVar()
        self.start_test_capture = Button(self, text="start test capture", command=self.start_test_capture_m)
        self.end_test_capture = Button(self, text='end test capture', command=self.end_test_capture_m, state=DISABLED)
        self.create_key_to_capture()

    def create_key_to_capture(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        keys_to_capture_label = Label(self, text='keys to capture (comma separated)')
        test_keys_output = Label(self, textvariable=self.test_captured_keys)
        keys_to_capture = Entry(self, textvariable=self.keys_to_capture_value)

        self.start_test_capture.grid(in_=self, row=0, column=2, sticky=N + S + E + W)
        self.end_test_capture.grid(in_=self, row=0, column=3, sticky=N + S + E + W)

        keys_to_capture_label.grid(in_=self, row=0, column=0, columnspan=2, sticky=N + S + E + W)
        test_keys_output.grid(in_=self, row=2, column=0, columnspan=4, sticky=N + S + E + W)
        keys_to_capture.grid(in_=self, row=1, column=0, columnspan=4, sticky=N + S + E + W)

    def start_test_capture_m(self):
        self.start_test_capture['state'] = DISABLED
        self.end_test_capture['state'] = NORMAL
        self.thread = Thread(target=self.capture_and_print_keys)
        self.test_capture_keys = True
        self.thread.start()

    def capture_and_print_keys(self):
        value_get = self.keys_to_capture_value.get()
        if len(value_get) <= 0:
            self.test_captured_keys.set('Choose at least one key to capture')
            self.start_test_capture['state'] = NORMAL
            self.end_test_capture['state'] = DISABLED
            self.test_capture_keys = False
            sys.exit()
        split = value_get.split(',')
        capture = KeyCapture(split)
        last_keys = np.empty(len(split))
        self.test_captured_keys.set('')
        while self.test_capture_keys:
            try:
                keys = capture.capture_keys()
                if (keys - last_keys).any():
                    get = self.test_captured_keys.get()
                    self.test_captured_keys.set(get + keys.__str__())
                last_keys = keys
            except ValueError as e:
                self.test_captured_keys.set(e.args[0])
                self.start_test_capture['state'] = NORMAL
                self.end_test_capture['state'] = DISABLED
                self.test_capture_keys = False
                sys.exit()

    def end_test_capture_m(self):
        self.start_test_capture['state'] = NORMAL
        self.end_test_capture['state'] = DISABLED
        self.test_capture_keys = False
        self.thread.join()
