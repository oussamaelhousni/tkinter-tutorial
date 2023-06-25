import tkinter as tk
from tkinter import ttk
import random

# window
window = tk.Tk()

# widgets
canvas = tk.Canvas(master=window, scrollregion=(0, 0, 2000, 5000))
canvas.pack(expand=True, fill="both")

for _ in range(100):
    l = random.randint(0, 2000)
    t = random.randint(0, 5000)
    w = random.randint(0, 2000)
    h = random.randint(0, 5000)
    color = random.choice(["red", "blue", "green", "orange"])
    canvas.create_rectangle(l, t, w, h, fill=color)

canvas.bind(
    "<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units")
)
# scrollbar
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
# run
window.mainloop()
