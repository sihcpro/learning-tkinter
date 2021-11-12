from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x200")

tab_parent = Notebook(root)

tab1 = Frame(tab_parent)
tab2 = Frame(tab_parent)

Label(tab1, text="Tab1").pack()
Label(tab2, text="Tab2").pack()

tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")

tab_parent.pack(expand=1, fill="both")

root.mainloop()
