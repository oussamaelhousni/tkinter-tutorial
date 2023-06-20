import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()
window.geometry("500x500")

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="green")
label3 = ttk.Label(master=window, text="Label 3", background="blue")

button1 = ttk.Button(master=window, text="raise label 1", command=lambda: label1.lift())
button2 = ttk.Button(master=window, text="raise label 2", command=lambda: label2.lift())
button3 = ttk.Button(
    master=window, text="raise label 3", command=lambda: label3.lift(aboveThis=label2)
)

# layout

label1.place(x=100, y=20, width=50, height=100)
label2.place(x=50, y=35, width=250, height=150)
label3.place(x=75, y=45, width=200, height=200)

button1.place(relx=0.2, rely=0.9, width=100, height=30)
button2.place(relx=0.5, rely=0.9, width=100, height=30)
button3.place(relx=0.8, rely=0.9, width=100, height=30)

# run
window.mainloop()
