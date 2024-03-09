import tkinter as tk

def generateLabel(window, name):
    label = tk.Label(window, text=name)
    return label
def setLabelPosition(label, row, column, x, y):
    label.grid(row=row, column=column, padx=x, pady=y)