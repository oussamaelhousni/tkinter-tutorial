import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("500x500")

style = ttk.Style()

style.configure("btn.TButton", foreground="red", background="green")
style.map("btn.TButton", foreground=[("pressed", "orange")])

label = ttk.Label(
    master=window,
    text="A label",
    background="yellow",
    foreground="blue",
    font=("Calibri", 21),
)
label.pack()

button = ttk.Button(master=window, text="A button", style="btn.TButton")
button.pack()
# run
window.mainloop()
