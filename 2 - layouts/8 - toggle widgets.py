import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()


def toggle_label():
    global toggle_label
    if toggle_label:
        toggle_label = False
        label.place_forget()
    else:
        label.place(x=0, y=0, relheight=1, relwidth=1)
        toggle_label = True


# widgets
button = ttk.Button(master=window, text="toggle label", command=toggle_label)
label = ttk.Label(master=window, text="toggled label", background="red")
toggle_label = True
button.lift()
button.place(x=0, y=0)
label.place(x=0, y=0, relheight=1, relwidth=1)

# run
window.mainloop()
