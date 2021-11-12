import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Your phone number:").pack()
phone_number = tk.StringVar(root)
box = ttk.Spinbox(root, from_=111111111, to=999999999, textvariable=phone_number)
box.pack()

tk.Label(root, text="Your age:").pack()
age = tk.StringVar(root, value=25)
box2 = ttk.Spinbox(
    root, from_=0, to=200, textvariable=age, format="%.1f", increment=0.1
)
box2.pack()

root.mainloop()

print("phone_number", phone_number.get())
print("age", age.get())
