from mytk import *
from tkinter import filedialog
import os
import csv
import re
import time
import gc
from collections import deque

import numpy as np
import scipy
import threading as Th
from queue import Queue, Empty


class MicroscopeApp(App):
    def __init__(self):
        App.__init__(self)

        self.window.widget.title("Microscope")

        self.camera = VideoView(device=0, zoom_level=3)
        self.camera.grid_into(
            self.window, row=1, column=0, columnspan=6, pady=5, padx=10, sticky="nw"
        )

        self.video_view_label = Label("Display : ")
        self.video_view_label.grid_into(
            self.window, row=0, column=0, pady=5, padx=0, sticky="w"
        )

        color_all, color_red, color_blue, color_green = RadioButton.linked_group(
            labels_values={"all": 0, "red": 1, "blue":2, "green":3}
        )
        color_all.grid_into(
            self.window,
            column=1,
            row=0,
            pady=5,
            padx=5,
            sticky="w",
        )
        color_red.grid_into(
            self.window,
            column=2,
            row=0,
            pady=5,
            padx=5,
            sticky="w",
        )
        color_blue.grid_into(
            self.window,
            column=3,
            row=0,
            pady=5,
            padx=5,
            sticky="w",
        )
        color_green.grid_into(
            self.window,
            column=4,
            row=0,
            pady=5,
            padx=5,
            sticky="w",
        )

        self.controls = Box(label="Controls", width=500, height=700)
        self.window.widget.grid_columnconfigure(1, weight=0)

        self.controls.grid_into(
            self.window, column=6, row=1, pady=0, padx=5, sticky="nsew"
        )
        self.controls.widget.grid_rowconfigure(0, weight=0)
        self.controls.widget.grid_rowconfigure(1, weight=0)

        self.start_button = Button("Start")
        self.start_button.grid_into(
            self.controls, column=0, row=0, pady=5, padx=5, sticky="w"
        )

        self.zoomlevel_label = Label("Zoom level:")
        self.zoomlevel_label.grid_into(
            self.window, column=0, row=2, pady=5, padx=5, sticky="w"
        )
        self.zoom_level_control = IntEntry(value=3, width=5, minimum=1)
        self.zoom_level_control.grid_into(
            self.window, column=1, row=2, pady=5, padx=5, sticky="w"
        )
        self.camera.bind_properties(
            "zoom_level", self.zoom_level_control, "value_variable"
        )

    def about(self):
        showinfo(
            title="About Microscope",
            message="An application created with myTk",
        )

    def help(self):
        webbrowser.open("https://www.dccmlab.ca/")


if __name__ == "__main__":
    app = MicroscopeApp()
    app.mainloop()
