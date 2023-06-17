import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()
window.geometry("300x300")

# checkbox button
check = tk.IntVar(value=0)
checkbox = ttk.Checkbutton(
    master=window,
    text="checkbox button",
    variable=check,
    command=lambda: print(check.get()),
    onvalue=1,
    offvalue=0,
)
checkbox.pack()


# radio button
radio_value = tk.IntVar(value=0)
radio_1 = ttk.Radiobutton(master=window, variable=radio_value, text="radio1", value=0)
radio_2 = ttk.Radiobutton(master=window, variable=radio_value, text="radio2", value=1)
radio_3 = ttk.Radiobutton(master=window, variable=radio_value, text="radio3", value=2)

for radio in (radio_1, radio_2, radio_3):
    radio.pack()
# run
window.mainloop()
