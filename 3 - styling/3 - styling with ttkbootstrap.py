import ttkbootstrap as ttk
import customtkinter as ctk

# window
window = ttk.Window()
window.geometry("500x500")
# create widgets
button = ttk.Button(master=window, text="a button", bootstyle="info-outline")
button.pack()
# run
window.mainloop()
