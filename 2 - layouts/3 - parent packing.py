import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# widget
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="green")

frame = ttk.Frame(master=window)
button1 = ttk.Button(master=frame, text="Button 1")
button2 = ttk.Button(master=frame, text="Button 2")
button3 = ttk.Button(master=frame, text="Button 3")
button4 = ttk.Button(master=frame, text="Button 4")
button5 = ttk.Button(master=frame, text="Button 5")
button6 = ttk.Button(master=frame, text="Button 6")

# layout
label1.pack(side="top", expand=True, fill="both")
label2.pack(side="top", expand=True, fill="both")
label3.pack(side="top", expand=True)

button1.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")
button3.pack(side="left", expand=True, fill="both")

button4.pack(side="top", expand=True, fill="both", padx=2, pady=2)
button5.pack(side="top", expand=True, fill="both", padx=2, pady=2)
button6.pack(side="top", expand=True, fill="both", padx=2, pady=2)
frame.pack(side="top", expand=True, fill="both")
# run
window.mainloop()
