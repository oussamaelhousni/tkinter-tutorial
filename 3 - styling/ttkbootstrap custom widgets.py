import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification

# window
window = ttk.Window(themename="journal")
# scrollable frame
scroll = ScrolledFrame(master=window)

for i in range(20):
    button = ttk.Button(scroll, text=f"button {i}")
    button.pack()

scroll.pack(expand=True, fill="both")

# taost
toast = ToastNotification(
    title="toast title",
    message="this is actual message",
    duration=2000,
    position=(0, 0, "ne"),
)

# tooltip

ttk.Button(window, text="show notification", command=lambda: toast.show_toast()).pack()
# run
window.mainloop()
