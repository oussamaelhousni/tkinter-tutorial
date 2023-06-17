import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()
window.geometry("500x500")

# widgets
frame = ttk.Frame(master=window, borderwidth=3, relief=tk.GROOVE)

label = ttk.Label(master=frame, text="Hello from label")
button = ttk.Button(master=frame, text="Child button")
label.pack()
button.pack()
frame.pack()

label_out = ttk.Label(master=window, text="label outside the frame")
label_out.pack()

# run
window.mainloop()
