import tkinter as tk
import ttkbootstrap as ttk


def set_label():
    entry_text = entry.get()
    label["text"] = entry_text
    entry["state"] = "disabled"


def reset():
    label["text"] = "Some text"
    entry["state"] = "normal"


# create a window
window = tk.Tk()
window.title("window title")
window.geometry("500x500")  # width x height of the window

# create widgets
label = ttk.Label(master=window, text="Some text")
label.pack()

text = tk.Text(master=window)
text.pack()  # add the widget to master

entry = tk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="button", command=set_label)
button.pack()

reset_btn = ttk.Button(master=window, text="reset", command=reset)
reset_btn.pack()
# run
window.mainloop()
