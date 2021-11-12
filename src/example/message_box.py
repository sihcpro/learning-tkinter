import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

w = tk.Label(root, text="Message box example", font="50")
w.pack()

messagebox.showinfo("Info", "This is some info!")
messagebox.showwarning("Warning", "This is some warning!")
messagebox.showerror("Error", "Oh no!")
anwser = messagebox.askquestion("Huhh?", "Are you ok?")
messagebox.askyesno("Carefull", "Are you sure want to continue?")
messagebox.askokcancel("END", "This is the end!")

print("anwser", anwser)
