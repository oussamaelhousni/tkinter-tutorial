import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# widgets

label1 = ttk.Label(master=window, background="red", text="label1")
label2 = ttk.Label(master=window, background="blue", text="label2")

# pack
# label1.pack(side="left", fill="both", expand=True)
# label2.pack(side="right", fill="both", expand=True)

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
# window.columnconfigure(3, weight=1)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)
# window.rowconfigure(3, weight=1)

# label1.grid(row=1, rowspan=1, column=1, columnspan=2, sticky="nsew")
# label2.grid(row=2, rowspan=1, column=1, columnspan=2, sticky="nsew")

# place
label1.place(x=20, y=20, width=100, height=100)
label2.place(relx=0.2, rely=0.2, relwidth=0.5, relheight=0.3)
# run
window.mainloop()
