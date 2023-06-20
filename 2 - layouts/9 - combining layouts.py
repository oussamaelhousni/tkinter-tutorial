import tkinter as tk
import ttkbootstrap as ttk

# window
window = tk.Tk()

# frames
left_frame = ttk.Frame(master=window)
right_frame = ttk.Frame(master=window)

# left widgets
entry_frame = ttk.Frame(master=left_frame)
lbutton1 = ttk.Button(master=left_frame, text="Button 1")
lbutton2 = ttk.Button(master=left_frame, text="Button 2")
lbutton3 = ttk.Button(master=left_frame, text="Button 3")

progress1 = ttk.Scale(master=left_frame, from_=0, to=100, orient="vertical")
progress2 = ttk.Scale(master=left_frame, from_=0, to=100, orient="vertical")

check1 = ttk.Checkbutton(master=entry_frame, text="Check 1")
check2 = ttk.Checkbutton(master=entry_frame, text="Check 2")
entry = ttk.Entry(master=entry_frame)

# right widgets
label1 = ttk.Label(master=right_frame, text="Label 1", background="yellow")
rbutton1 = ttk.Button(master=right_frame, text="Button 1")
label2 = ttk.Label(master=right_frame, text="Label 2", background="orange")
rbutton2 = ttk.Button(master=right_frame, text="Button 2")

# left layout
left_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
left_frame.rowconfigure((0, 1, 4), weight=1, uniform="b")
left_frame.rowconfigure(3, weight=3)

lbutton1.grid(row=0, column=0, columnspan=2, sticky="nsew")
lbutton2.grid(row=0, column=2, columnspan=1, sticky="nsew")
lbutton3.grid(row=1, column=0, columnspan=3, sticky="nsew")
progress1.grid(row=2, column=0, sticky="ns", pady=5)
progress2.grid(row=2, column=2, sticky="ns", pady=4)

check1.pack(side="left")
check2.pack(side="right")
entry.pack(side="bottom")
entry_frame.grid(row=4, column=0, columnspan=3)

left_frame.place(x=0, y=0, relheight=1, relwidth=0.3)

# right frame
right_frame.rowconfigure((0, 1), weight=1)
right_frame.columnconfigure((0, 1), weight=1)

label1.grid(row=0, column=0)
rbutton1.grid(row=1, column=0)
label2.grid(row=0, column=1)
rbutton2.grid(row=1, column=1)
right_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
# run
window.mainloop()
