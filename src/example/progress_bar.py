import time
from tkinter import *
from tkinter.ttk import *

ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x250")


def step():
    for i in range(5):
        ws.update_idletasks()
        pb1["value"] += 20
        print("value", pb1["value"])

        time.sleep(1)


pb1 = Progressbar(ws, orient=HORIZONTAL, length=100, mode="indeterminate")
pb1.pack(expand=True)

Button(ws, text="Start", command=step).pack()

ws.mainloop()
