from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.ttk import *

# create the root window
root = Tk()
root.title("Tkinter Open File Dialog")
root.resizable(False, False)
root.geometry("300x150")


def select_file():
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilenames(
        title="Open a file", initialdir="/", filetypes=filetypes
    )

    showinfo(title="Selected File", message=filename)


# open button
open_button = Button(root, text="Open a File", command=select_file)

open_button.pack(expand=True)


# run the application
root.mainloop()
