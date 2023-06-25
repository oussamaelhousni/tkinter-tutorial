import customtkinter as ctk

# window
window = ctk.CTk()
window.geometry("500x500")
window.title("customtkinter")

# widgets
label = ctk.CTkLabel(master=window, text="a label", fg_color="red", corner_radius=10)
button = ctk.CTkButton(
    master=window,
    text="a button",
    fg_color=("orange", "yellow"),
    text_color=("blue", "black"),
    hover_color=("pink", "red"),
)

label.pack()
button.pack()
print(ctk.get_appearance_mode())
switch = ctk.CTkSwitch(
    master=window,
    command=lambda: ctk.set_appearance_mode(
        "light" if ctk.get_appearance_mode() == "Dark" else "dark"
    ),
)
switch.pack()
# run
window.mainloop()
