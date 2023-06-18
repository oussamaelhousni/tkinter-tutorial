import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()
window.title("Manipulating window")
window.geometry("600x400+100+200")

# minsize and resizeable
window.minsize(200, 100)
window.resizable(True, False)
window.bind("<Escape>", lambda e: window.quit())
# screen sizes
print(f"My screen width : {window.winfo_screenwidth()}")
print(f"My screen width : {window.winfo_screenheight()}")

# window attributes
window.attributes("-topmost", True)
window.attributes("-fullscreen", True)
# run
window.mainloop()
