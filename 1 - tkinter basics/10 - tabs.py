import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# tabs
notebook = ttk.Notebook(master=window)

# tab 1
tab1 = ttk.Frame(master=notebook, borderwidth=3, relief=tk.GROOVE)
label1 = ttk.Label(master=tab1, text="this is tab1")
label1.pack()

# tab2
tab2 = ttk.Frame(master=notebook, borderwidth=3, relief=tk.GROOVE)
label2 = ttk.Label(master=tab2, text="This tab 2")
label2.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()
# run
window.mainloop()
