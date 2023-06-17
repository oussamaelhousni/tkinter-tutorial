import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.geometry("500x500")

# Sliders
scale_int = tk.IntVar(value=10)
scale = ttk.Scale(
    master=window,
    from_=0,
    to=30,
    length=350,
    command=lambda e: print(scale_int.get()),
    variable=scale_int,
)
scale.pack()

# Progress bar
progress = ttk.Progressbar(
    master=window,
    variable=scale_int,
    maximum=30,
    orient="vertical",
)
progress.pack(pady=10)

# scrolled text
scrolled_txt = scrolledtext.ScrolledText(master=window)
scrolled_txt.pack()
# run
window.mainloop()
