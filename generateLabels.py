import tkinter as tk
from widgetFactory import generateWidget
def generateLabel(window, name, text):
    label = generateWidget(window, name, text=text)
    return label
def setLabelPosition(label, row, column, x, y):
    label.grid(row=row, column=column, padx=x, pady=y)