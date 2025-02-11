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
            self.window, row=1, column=0, columnspan=6, rowspan=3, pady=5, padx=10, sticky="nswe"
        )
        self.window.row_resize_weight(2, weight=1)
        self.window.column_resize_weight(5, weight=1)

        self.video_view_label = Label("Display :")
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

        self.controls = Box(label="Image Source")
        # self.window.widget.grid_columnconfigure(1, weight=0)

        self.controls.grid_into(
            self.window, column=6, row=1, pady=5, padx=5, sticky="new"
        )
        # self.controls.widget.grid_rowconfigure(0, weight=0)
        # self.controls.widget.grid_rowconfigure(1, weight=0)

        self.start_button = Button("Start")
        self.start_button.grid_into(
            self.controls, column=1, row=0, pady=5, padx=5, sticky="e"
        )

        self.configure_button = Button("Configure...")
        self.configure_button.grid_into(
            self.controls, column=0, row=0, pady=5, padx=5, sticky="w"
        )

        self.devices = TableView(columns_labels={"streams":"Available video streams"})
        self.devices.grid_into(
            self.window, column=6, row=2, pady=5, padx=5, sticky="nwe"
        )

        self.save_box = Box(label="Save")
        self.save_box.grid_into(
            self.window, column=6, row=3, pady=5, padx=5, sticky="nwe"
        )

        self.save_text1 = Label("Average")
        self.save_text1.grid_into(
            self.save_box, column=0, row=0, pady=5, padx=0, sticky="e"
        )
        self.frames = IntEntry(100, maximum=300, width=3)
        self.frames.grid_into(
            self.save_box, column=1, row=0, pady=5, padx=0
        )
        self.save_text2 = Label("frames from")
        self.save_text2.grid_into(
            self.save_box, column=2, row=0, pady=5, padx=0, sticky="we"
        )
        self.frames_from = PopupMenu(menu_items=["main"])
        self.frames_from.grid_into(
            self.save_box, column=3, row=0, pady=5, padx=0, sticky="we"
        )
        self.frames_from.selection_changed(0)

        self.save_text3 = Label("with channels")
        self.save_text3.grid_into(
            self.save_box, column=0, row=1, pady=5, padx=0, sticky="we"
        )
        self.channel_select = PopupMenu(menu_items=["all", "red", "blue", "green"])
        self.channel_select.grid_into(
            self.save_box, column=1, row=1, pady=5, padx=0, sticky="w"
        )
        self.channel_select.selection_changed(0)

        self.save_button = Button(label="Save as...")
        self.save_button.grid_into(
            self.save_box, column=3, row=3, pady=5, padx=0, sticky="e"
        )

        self.zoomlevel_label = Label("Zoom level:")
        self.zoomlevel_label.grid_into(
            self.window, column=0, row=4, pady=5, padx=5, sticky="w"
        )
        self.zoom_level_control = IntEntry(value=3, width=2, minimum=1)
        self.zoom_level_control.grid_into(
            self.window, column=1, row=4, pady=5, padx=5, sticky="w"
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
