from tkinter import Frame, BOTH, Button, filedialog, N, S, E, W, DoubleVar, StringVar, Label

from src.frontend.key_capture_frame import KeyCaptureFrame
from src.frontend.picture_capture_frame import PictureCaptureFrame


class TrainDataCollector(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.thread = None
        self.test_capture_keys = False
        self.test_captured_keys = StringVar()
        self.keys_to_capture_value = StringVar()
        self.y_position_value = DoubleVar()
        self.x_position_value = DoubleVar()
        self.y_size_value = DoubleVar()
        self.x_size_value = DoubleVar()

        self.train_data_x_location = StringVar()
        self.train_data_y_location = StringVar()
        self.master = master

        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Training data collector")
        self.pack(fill=BOTH, expand=1)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.create_file_location_buttons()

        picture_capture_frame = PictureCaptureFrame(self.y_position_value, self.x_position_value, self.y_size_value, self.x_size_value, self)
        picture_capture_frame.grid(row=2, column=0, columnspan=4, sticky=N + S + E + W)

        key_capture_frame = KeyCaptureFrame(self.keys_to_capture_value, self)
        key_capture_frame.grid(row=3, column=0, columnspan=4, sticky=N + S + E + W)

    def create_file_location_buttons(self):
        # creating a button instance
        file_location_x_selector = Button(self, text="select file x location", command=self.select_file_x)
        file_location_x_label = Label(self, textvariable=self.train_data_x_location)

        file_location_y_selector = Button(self, text="select file y location", command=self.select_file_y)
        file_location_y_label = Label(self, textvariable=self.train_data_y_location)
        # placing the button on my window
        file_location_x_selector.grid(in_=self, row=0, column=0, columnspan=2, sticky=N + S + E + W)
        file_location_x_label.grid(in_=self, row=1, column=0, columnspan=2, sticky=N + S + E + W)

        file_location_y_selector.grid(in_=self, row=0, column=2, columnspan=2, sticky=N + S + E + W)
        file_location_y_label.grid(in_=self, row=1, column=2, columnspan=2, sticky=N + S + E + W)

    def select_file_y(self):
        self.train_data_y_location.set(filedialog.asksaveasfilename(initialdir='/', title='Select file'))

    def select_file_x(self):
        self.train_data_x_location.set(filedialog.asksaveasfilename(initialdir='/', title='Select file'))
