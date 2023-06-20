import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        Segment(self).pack(expand=True, fill="both")
        Segment(self).pack(expand=True, fill="both")
        Segment(self).pack(expand=True, fill="both")
        Segment(self).pack(expand=True, fill="both")
        # run
        self.mainloop()


class Segment(ttk.Frame):
    def __init__(
        self, parent, label_text="label", button1_text="button1", button2_text="button2"
    ):
        super().__init__(parent)
        self.label = ttk.Label(master=self, text=label_text)
        self.button1 = ttk.Button(master=self, text=button1_text)
        self.frame = ttk.Frame(master=self)
        ttk.Button(master=self.frame, text="").pack(expand=True, fill="both")
        self.button2 = ttk.Button(master=self.frame, text=button2_text)

        self.create_layout()

    def create_layout(self):
        self.label.pack(side="left", expand=True, fill="both")
        self.button1.pack(side="left", expand=True, fill="both")
        self.button2.pack(expand=True, fill="both")
        self.frame.pack(side="left", expand=True, fill="both")


App()
