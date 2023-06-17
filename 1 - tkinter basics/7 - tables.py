import tkinter as tk
import ttkbootstrap as ttk
import random

# window
window = tk.Tk()
window.geometry("600x600")

# data
last_names = ["elhousni", "adraoui", "nasssiri", "nassiri", "nassiri"]
first_names = ["oussama", "ayman", "ammar", "ahmed", "mohammed"]

# table
table = ttk.Treeview(master=window, columns=("First", "Last", "Email"), show="headings")
table.heading("First", text="First name")
table.heading("Last", text="Last name")
table.heading("Email", text="Email")

for i in range(15):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first}-{last}@gmail.com"
    data = (first, last, email)
    table.insert(parent="", index=i, values=data)

# add to last of table
table.insert(parent="", index=tk.END, values=("XXXXX", "YYYYY", "ZZZZZZ@gmail.com"))
table.pack(fill="both", expand=True)


# events
def showSelectedItems(_):
    for id in table.selection():
        print(table.item(id)["values"])


def deleteItems(_):
    for id in table.selection():
        table.delete(id)


table.bind("<<TreeviewSelect>>", showSelectedItems)
table.bind("<Delete>", deleteItems)
# run
window.mainloop()
