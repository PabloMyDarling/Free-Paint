from tkinter import *
from typing import Literal
from tkinter.colorchooser import askcolor

root = Tk()
root.geometry("800x550+70+70")
root.propagate(False)
root.iconbitmap("logo.ico")

canvas = Canvas(root, bg="#fff")
canvas.pack(fill=BOTH, expand=TRUE)

def change_full_color(color: str):
    '''Change the color of the pencil.'''
    fill.set(color)
    outline.set(color)
    root.title(f"Free Paint - Pencil size: {radius.get()}, Colour: {fill.get()}, Pencil shape: {shape.get()}")

def change_size(size: int):
    '''Change the size of the pencil.'''
    radius.set(size)
    root.title(f"Free Paint - Pencil size: {radius.get()}, Colour: {fill.get()}, Pencil shape: {shape.get()}")

def change_shape(shape_: Literal['circle', 'square']):
    '''Change the shape of the pencil.'''
    if shape_ == 'circle': shape.set("circle")
    elif shape_ == 'square': shape.set("square")
    root.title(f"Free Paint - Pencil size: {radius.get()}, Colour: {fill.get()}, Pencil shape: {shape.get()}")

def draw(e):
    if shape.get() == "circle": canvas.create_oval(e.x - radius.get(), e.y - radius.get(), e.x + radius.get(), e.y + 20, fill=fill.get(), outline=outline.get())
    elif shape.get() == "square": canvas.create_rectangle(e.x - radius.get(), e.y - radius.get(), e.x + radius.get(), e.y + 20, fill=fill.get(), outline=outline.get())

def reset(e=None):
    '''Reset the canvas.'''
    canvas.delete(ALL)

fill = StringVar(root, "#000000")
outline = StringVar(root, "#000000")
shape = StringVar(root, "circle")
radius = IntVar(root, 20)

root.title(f"Free Paint - Pencil size: {radius.get()}, Colour: {fill.get()}, Pencil shape: {shape.get()}")

canvas.bind("<Button-1>", draw)
canvas.bind("<B1-Motion>", draw)

root.bind("<Control-=>", lambda e: change_size(radius.get() + 1))
root.bind("<Control-minus>", lambda e: change_size(radius.get() - 1))
root.bind("<Control-r>", reset)
root.bind("<Control-s>", lambda e: change_shape("square"))
root.bind("<Control-c>", lambda e: change_shape("circle"))
root.bind("<Control-C>", lambda e: change_full_color(askcolor(title="Choose a color.")[1]))

mainloop()
