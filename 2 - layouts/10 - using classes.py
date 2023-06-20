import tkinter as tk
import ttkbootstrap as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Class Based App")
        self.geometry("600x600")
        self.minsize(600, 600)
        # frames
        self.left_frame = LeftFrame(self)
        self.right_frame = RightFrame(self)
        # self.right_frame = RightFrame(self)
        # run
        self.mainloop()


class LeftFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.entry_frame = ttk.Frame(master=self)
        self.button1 = ttk.Button(master=self, text="Button 1")
        self.button2 = ttk.Button(master=self, text="Button 2")
        self.button3 = ttk.Button(master=self, text="Button 3")

        self.progress1 = ttk.Scale(master=self, from_=0, to=100, orient="vertical")
        self.progress2 = ttk.Scale(master=self, from_=0, to=100, orient="vertical")

        self.check1 = ttk.Checkbutton(master=self.entry_frame, text="Check 1")
        self.check2 = ttk.Checkbutton(master=self.entry_frame, text="Check 2")
        self.entry = ttk.Entry(master=self.entry_frame)

    def create_layout(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 4), weight=1, uniform="b")
        self.rowconfigure(3, weight=3)

        self.button1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.button2.grid(row=0, column=2, columnspan=1, sticky="nsew")
        self.button3.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.progress1.grid(row=2, column=0, sticky="ns", pady=5)
        self.progress2.grid(row=2, column=2, sticky="ns", pady=4)

        self.check1.pack(side="left")
        self.check2.pack(side="right")
        self.entry.pack(side="bottom")
        self.entry_frame.grid(row=4, column=0, columnspan=3)

        self.place(x=0, y=0, relheight=1, relwidth=0.3)


class RightFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.label1 = ttk.Label(master=self, text="Label 1", background="yellow")
        self.button1 = ttk.Button(master=self, text="Button 1")
        self.label2 = ttk.Label(master=self, text="Label 2", background="orange")
        self.button2 = ttk.Button(master=self, text="Button 2")

    def create_layout(self):
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.label1.grid(row=0, column=0, sticky="nsew")
        self.button1.grid(row=1, column=0, sticky="nsew")
        self.label2.grid(row=0, column=1, sticky="nsew")
        self.button2.grid(row=1, column=1, sticky="nsew")
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)


App()
