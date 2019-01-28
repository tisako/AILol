import cv2
from tkinter import Frame, BOTH, Button, filedialog, LEFT, Canvas, RAISED, X, N, S, E, W

from PIL import ImageTk, Image

from src.input_capture.ScreenCapture import ScreenCapture


class TrainDataCollector(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.img = None
        self.image = None
        self.canvas = None
        self.train_data_x_location = ''
        self.train_data_y_location = ''
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

        self.create_file_location_buttons()

        self.create_snap_picture_component()

    def create_snap_picture_component(self):
        take_picture = Button(self, text="take_picture", command=self.take_picture)
        take_picture.grid(in_=self, row=1, column=0, columnspan=2, sticky=N+S+E+W)
        self.canvas = Canvas(self)
        self.canvas.grid(in_=self, row=2, column=0, columnspan=2, sticky=N+S+E+W)
        self.canvas.bind('<Configure>', self.resize)

    def create_file_location_buttons(self):
        # creating a button instance
        file_location_x_selector = Button(self, text="select file x location", command=self.select_file_x)
        file_location_y_selector = Button(self, text="select file y location", command=self.select_file_y)
        # placing the button on my window
        file_location_x_selector.grid(in_=self, row=0, column=0, sticky=N+S+E+W)
        file_location_y_selector.grid(in_=self, row=0, column=1, sticky=N+S+E+W)

    def select_file_y(self):
        self.train_data_x_location = filedialog.asksaveasfilename(initialdir='/', title='Select file')
        print(self.train_data_x_location)

    def select_file_x(self):
        self.train_data_y_location = filedialog.asksaveasfilename(initialdir='/', title='Select file')

    def resize(self, event):
        if self.image is not None:
            self.draw_image_on_cavas(event.width, event.height)

    def draw_image_on_cavas(self, width, height):
        resize = cv2.resize(self.image, (width, height))
        fromarray = Image.fromarray(resize)
        self.img = ImageTk.PhotoImage(image=fromarray)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

    def take_picture(self):
        capture = ScreenCapture()
        self.image = cv2.cvtColor(capture.get_screen_image(), cv2.COLOR_BGR2RGB)
        self.draw_image_on_cavas(self.canvas.winfo_width(), self.canvas.winfo_height())
