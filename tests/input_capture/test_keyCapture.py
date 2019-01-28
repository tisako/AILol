from unittest import TestCase

import keyboard
import numpy.testing as npt
from keyboard import KeyboardEvent, KEY_DOWN, KEY_UP

from src.input_capture.KeyCapture import KeyCapture

# code needed to mock keyboard data input
dummy_keys = {
    'space': [(0, [])],

    'a': [(1, [])],
    'b': [(2, [])],
    'c': [(3, [])],
    'A': [(1, ['shift']), (-1, [])],
    'B': [(2, ['shift']), (-2, [])],
    'C': [(3, ['shift']), (-3, [])],

    'alt': [(4, [])],
    'left alt': [(4, [])],

    'left shift': [(5, [])],
    'right shift': [(6, [])],

    'left ctrl': [(7, [])],

    'backspace': [(8, [])],
    'caps lock': [(9, [])],

    '+': [(10, [])],
    ',': [(11, [])],
    '_': [(12, [])],

    'none': [],
    'duplicated': [(20, []), (20, [])],
}

input_events = []
output_events = []


def make_event(event_type, name, scan_code=None, time=0):
    return KeyboardEvent(event_type=event_type, scan_code=scan_code or dummy_keys[name][0][0], name=name, time=time)


def send_instant_event(event):
    if keyboard._listener.direct_callback(event):
        output_events.append(event)


# Mock out side effects.
keyboard._os_keyboard.init = lambda: None
keyboard._os_keyboard.listen = lambda callback: None
keyboard._os_keyboard.map_name = dummy_keys.__getitem__
keyboard._os_keyboard.press = lambda scan_code: send_instant_event(make_event(KEY_DOWN, None, scan_code))
keyboard._os_keyboard.release = lambda scan_code: send_instant_event(make_event(KEY_UP, None, scan_code))
keyboard._os_keyboard.type_unicode = lambda char: output_events.append(KeyboardEvent(event_type=KEY_DOWN, scan_code=999, name=char))


class TestKeyCapture(TestCase):
    # setup needed to link keyboard mock to key presses
    def setUp(self):
        del input_events[:]
        del output_events[:]
        keyboard._recording = None
        keyboard._pressed_events.clear()
        keyboard._physically_pressed_keys.clear()
        keyboard._logically_pressed_keys.clear()
        keyboard._hotkeys.clear()
        keyboard._listener.init()
        keyboard._word_listeners = {}

    def test_capture_space(self):
        capture = KeyCapture(['space'])
        send_instant_event(make_event(KEY_DOWN, 'space'))

        captured_keys = capture.capture_keys()

        npt.assert_array_equal(captured_keys, [1.], 'Space was not captured')

    def test_capture_only_space(self):
        capture = KeyCapture(['space', 'a'])
        send_instant_event(make_event(KEY_DOWN, 'space'))

        captured_keys = capture.capture_keys()

        npt.assert_array_equal(captured_keys, [1., 0.], 'More than the space was captured')

    def test_capture_both_space_and_a(self):
        capture = KeyCapture(['space', 'a'])
        send_instant_event(make_event(KEY_DOWN, 'space'))
        send_instant_event(make_event(KEY_DOWN, 'a'))

        captured_keys = capture.capture_keys()

        npt.assert_array_equal(captured_keys, [1., 1.], 'Not both keys are captured')