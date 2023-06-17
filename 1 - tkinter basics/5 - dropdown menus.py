import tkinter as tk
import ttkbootstrap as ttk


def combobox(event):
    print(combo_value.get())


# window
window = tk.Tk()
window.geometry("300x300")
# combobox
items = ("Java", "C", "C++", "Python")
combo_value = tk.StringVar(value=items[0])
combo = ttk.Combobox(master=window, textvariable=combo_value)
combo["values"] = items
combo.pack()
combo.bind("<<ComboboxSelected>>", combobox)

# spinbox
value = tk.IntVar(value=1)
spin = ttk.Spinbox(master=window, from_=1, to=20, textvariable=value)

spin.bind("<<Increment>>", lambda e: print(value.get()))
spin.bind("<<Decrement>>", lambda e: print(value.get()))
spin.pack()
#  run
window.mainloop()
