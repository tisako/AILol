from tkinter import Tk

from src.frontend.train_data_collector import TrainDataCollector

root = Tk()
root.geometry("500x500")
app = TrainDataCollector(root)

root.mainloop()

