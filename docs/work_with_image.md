[<<](README.md)

# Tkinter with image

## Open
```python
from PIL import Image, ImageTk

image = Image.open("image.png")
ImageTk.PhotoImage(image)
```


## Add text
Need `compound` attribute is setted.
```python
ttk.Label(root, text="Image with text", image=photo, compound="right")
```
