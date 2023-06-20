import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")

        # create widgets
        self.size_notifier = SizeNotifier(
            self,
            {
                300: self.create_small_layout,
                600: self.create_medium_layout,
                1200: self.create_large_layout,
            },
        )
        self.create_widgets()
        self.create_medium_layout()
        # run
        self.mainloop()

    def create_widgets(self):
        self.frame = ttk.Frame(master=self)
        self.label1 = ttk.Label(master=self.frame, text="Label 1", background="red")
        self.label2 = ttk.Label(master=self.frame, text="Label 2", background="yellow")
        self.label3 = ttk.Label(master=self.frame, text="Label 3", background="orange")
        self.label4 = ttk.Label(master=self.frame, text="Label 4", background="pink")

    def create_small_layout(self):
        self.forget()
        self.create_widgets()
        for label in (self.label1, self.label2, self.label3, self.label4):
            label.pack(expand=True, fill="both")
        self.frame.pack(expand=True, fill="both")

    def create_medium_layout(self):
        self.forget()
        self.create_widgets()
        self.frame.columnconfigure((0, 1), weight=1)
        self.frame.rowconfigure((0, 1), weight=1)
        self.label1.grid(row=0, column=0, sticky="nsew")
        self.label2.grid(row=0, column=1, sticky="nsew")
        self.label3.grid(row=1, column=0, sticky="nsew")
        self.label4.grid(row=1, column=1, sticky="nsew")
        self.frame.pack(expand=True, fill="both")

    def create_large_layout(self):
        self.forget()
        self.create_widgets()
        for label in (self.label1, self.label2, self.label3, self.label4):
            label.pack(expand=True, fill="both", side="left")
        self.frame.pack(expand=True, fill="both")

    def forget(self):
        self.frame.pack_forget()


class SizeNotifier:
    def __init__(self, window, size_dict):
        self.size_dict = size_dict
        self.window = window
        self.current_min_size = 600
        self.window.bind("<Configure>", self.check_size)

    def check_size(self, _):
        width = int(self.window.winfo_width())
        checked_minsize = 300
        for size in self.size_dict:
            delta = width - size
            if delta >= 0:
                checked_minsize = size
        if self.current_min_size != checked_minsize:
            self.current_min_size = checked_minsize
            self.size_dict[self.current_min_size]()


App()
