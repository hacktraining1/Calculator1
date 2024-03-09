import tkinter as tk

def generateEntry(window):
    return tk.Entry(window)

def setEntryPosition(entry, row, column, x, y):
    entry.grid(row=row, column=column, padx=x, pady=y)