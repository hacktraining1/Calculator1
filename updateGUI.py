import tkinter as tk

def updateGUI(entry1_widget, entry2_widget, result):
    entry1_widget.delete(0, tk.END)
    entry2_widget.delete(0, tk.END)
    entry1_widget.insert(0, result)
def clearEntry(widget):
    widget.delete(0, tk.END)
