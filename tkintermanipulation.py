import tkinter as tk

def config(label, text, font, size):
    label.config(text=f"{text}", font=(f"{font}", {size}))