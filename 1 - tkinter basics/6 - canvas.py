import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()
window.geometry("800x600")

# canvas
canvas = tk.Canvas(master=window, bg="white")
canvas.pack()

# create line
canvas.create_line((0, 0), (200, 200), width=4, fill="red")

# create rectangle
canvas.create_rectangle((100, 100), (200, 200), fill="yellow", width=3)
# run
window.mainloop()
