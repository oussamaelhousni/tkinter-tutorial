import tkinter as tk
import ttkbootstrap as ttk


# https://www.pythontutorial.net/tkinter/tkinter-event-binding/
def get_position(event):
    print(f"x:{event.x} , y:{event.y}")


def get_key(event):
    print(f"{event.char} is pressed")


# window
window = tk.Tk()

# widget 1
text = ttk.Text(master=window)
text.pack(pady=5)

# widget 2
entry = ttk.Entry(master=window)
entry.pack(pady=5)

# widget 3
button = ttk.Button(master=window, text="button")
button.pack(pady=5)
# run
window.bind("<Motion>", get_position)
# window.bind("<KeyPress>", get_key)
window.bind("<KeyPress-7>", lambda e: print("7 a asat"))
window.mainloop()
