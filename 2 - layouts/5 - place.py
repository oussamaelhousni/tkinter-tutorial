import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="green")
label4 = ttk.Label(master=window, text="Label 4", background="yellow")

# layout
label1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
label2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
label3.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.5)
label4.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)
# run
window.mainloop()
