import tkinter as tk

# window
window = tk.Tk()
window.title("Tkinter variables")
window.geometry("300x300")
# widgets

string_var = tk.StringVar()

label = tk.Label(master=window, textvariable=string_var)
string = tk.StringVar()
entry = tk.Entry(master=window, textvariable=string_var)
button = tk.Button(
    master=window, text="button", command=lambda: string_var.set("button pressed")
)
label.pack()
entry.pack()
button.pack()
# run
window.mainloop()
