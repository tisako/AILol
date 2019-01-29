import win32api
from tkinter import Frame, Entry, Label, W, E, S, N, Button, Canvas

from PIL import Image, ImageTk
from cv2 import cv2

from src.input_capture.ScreenCapture import ScreenCapture


class PictureCaptureFrame(Frame):
    def __init__(self, y_position_value, x_position_value, y_size_value, x_size_value, master=None):
        Frame.__init__(self, master)
        self.y_position_value = y_position_value
        self.y_position_value.set(0)
        self.x_position_value = x_position_value
        self.x_position_value.set(0)
        self.y_size_value = y_size_value
        self.y_size_value.set(win32api.GetSystemMetrics(1))
        self.x_size_value = x_size_value
        self.x_size_value.set(win32api.GetSystemMetrics(0))
        self.img = None
        self.image = None
        self.canvas = None

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.create_snap_size_component()
        self.create_snap_picture_component()

    def create_snap_picture_component(self):
        take_picture = Button(self, text="take_picture", command=self.take_picture)
        take_picture.grid(in_=self, row=2, column=0, columnspan=4, sticky=N + S + E + W)
        self.canvas = Canvas(self)
        self.canvas.grid(in_=self, row=3, column=0, columnspan=4, sticky=N + S + E + W)
        self.canvas.bind('<Configure>', self.resize)

    def resize(self, event):
        if self.image is not None:
            self.draw_image_on_canvas(event.width, event.height)

    def draw_image_on_canvas(self, width, height):
        resize = cv2.resize(self.image, (width, height))
        from_array = Image.fromarray(resize)
        self.img = ImageTk.PhotoImage(image=from_array)
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

    def take_picture(self):
        capture = ScreenCapture()
        try:
            screen_image = capture.get_screen_image((self.x_position_value.get(), self.y_position_value.get()), (self.x_size_value.get(), self.y_size_value.get()))
            self.image = cv2.cvtColor(screen_image, cv2.COLOR_BGR2RGB)
            self.draw_image_on_canvas(self.canvas.winfo_width(), self.canvas.winfo_height())
        except ValueError as e:
            self.img = None
            self.canvas.delete('all')
            self.canvas.create_text(10, 10, anchor="nw", fill ='black', font='Times 10 bold', text=e.args[0])


    def create_snap_size_component(self):
        x_position_label = Label(self, text='x position')
        x_position = Entry(self, textvariable=self.x_position_value)
        x_position_label.grid(in_=self, row=0, column=0, sticky=N + S + E + W)
        x_position.grid(in_=self, row=1, column=0, sticky=N + S + E + W)

        y_position_label = Label(self, text='y position')
        y_position = Entry(self, textvariable=self.y_position_value)
        y_position_label.grid(in_=self, row=0, column=1, sticky=N + S + E + W)
        y_position.grid(in_=self, row=1, column=1, sticky=N + S + E + W)

        x_size_label = Label(self, text='x size')
        x_size = Entry(self, textvariable=self.x_size_value)
        x_size_label.grid(in_=self, row=0, column=2, sticky=N + S + E + W)
        x_size.grid(in_=self, row=1, column=2, sticky=N + S + E + W)

        y_size_label = Label(self, text='x size')
        y_size_label.grid(in_=self, row=0, column=3, sticky=N + S + E + W)
        y_size = Entry(self, textvariable=self.y_size_value)
        y_size.grid(in_=self, row=1, column=3, sticky=N + S + E + W)
