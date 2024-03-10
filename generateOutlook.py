import tkinter as tk

from widgetFactory import generateWidget
from ButtonFactory import generateButtons
def generateOutlook(window):
    entries = generateInput(window)
    generateButtons(window, entries[0], entries[1])
def generateInput(window):
    label_names = ["Input 1:", "Input 2:"]
    entries = []
    input_frame = tk.Frame(window)
    for label_name in label_names:
        label = generateWidget(input_frame, "Label", text=label_name)
        entry = generateWidget(input_frame, "Entry")
        entries.append(entry)
        label.pack()
        entry.pack()
    input_frame.pack()
    return entries