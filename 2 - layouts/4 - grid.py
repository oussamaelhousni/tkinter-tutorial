import tkinter as tk
import ttkbootstrap as ttk


# window
window = tk.Tk()
window.geometry("500x500")

label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="green")
label4 = ttk.Label(master=window, text="Label 4", background="yellow")

button1 = ttk.Button(master=window, text="Button 1")
button2 = ttk.Button(master=window, text="Button 2")

entry = ttk.Entry(master=window)

# layout
window.columnconfigure((0, 1, 2), weight=1, uniform="a")
window.columnconfigure(3, weight=2)
window.rowconfigure((0, 1, 2, 3), weight=1, uniform="b")

label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=1, column=1, rowspan=3, sticky="nsew")
label3.grid(row=1, column=0, columnspan=3, sticky="snew")
label4.grid(row=3, column=3, sticky="se")

button1.grid(row=0, column=3, sticky="nsew")
button2.grid(column=2, row=2, sticky="nsew")
# run
window.mainloop()
