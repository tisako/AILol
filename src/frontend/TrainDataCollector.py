import cv2
from tkinter import Frame, BOTH, Button, filedialog, LEFT, Canvas, RAISED, X

from PIL import ImageTk, Image

from src.input_capture.ScreenCapture import ScreenCapture


class TrainDataCollector(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.train_data_x_location = ''
        self.train_data_y_location = ''
        self.master = master

        self.iframe5 = Frame(self, bd=2, relief=RAISED)
        self.canvas = Canvas(self.iframe5, width=300, height=300)

        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        file_location_x_selector = Button(self, text="select file x location", command=self.select_file_x)
        file_location_y_selector = Button(self, text="select file y location", command=self.select_file_y)

        # placing the button on my window
        file_location_x_selector.pack(in_=self)
        file_location_y_selector.pack(in_=self)

        take_picture = Button(self, text="take_picture", command=self.take_picture)
        take_picture.pack(in_=self)

        self.iframe5.pack(expand=1, fill=X, pady=10, padx=5)
        self.canvas.pack()




    def select_file_y(self):
        self.train_data_x_location = filedialog.asksaveasfilename(initialdir='/', title='Select file')
        print(self.train_data_x_location)

    def select_file_x(self):
        self.train_data_y_location = filedialog.asksaveasfilename(initialdir='/', title='Select file')
        print(self.train_data_y_location)

    def take_picture(self):
        capture = ScreenCapture()
        image = cv2.cvtColor(capture.get_screen_image(), cv2.COLOR_BGR2RGB)
        cv2.resize(image, (100, 100))
        fromarray = Image.fromarray(image)
        img = ImageTk.PhotoImage(image=fromarray)
        self.canvas.create_image(100, 100, anchor="nw", image=img)
