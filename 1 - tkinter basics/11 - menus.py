import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# widget
menu = ttk.Menu(master=window)

file_menu = ttk.Menu(master=menu, tearoff=False)
file_menu.add_command(label="new", command=lambda: print("new File"))
file_menu.add_command(label="Open", command=lambda: print("open FIle"))
file_menu.add_separator()
file_menu.add_command(label="Close", command=lambda: print("Closing"))
menu.add_cascade(label="File", menu=file_menu)

window.configure(menu=menu)
# run
window.mainloop()
