import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="yellow")
button = ttk.Button(master=window, text="button")

label1.pack(side="top", expand=True, fill="both")
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="left", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")
# run
window.mainloop()
