import tkinter as tk
from operations import calculate
from widgetFactory import generateWidget
def generateButtons(window, entry1, entry2):
    buttons_frame = tk.Frame(window)
    operands = ["addition", "subtract", "multiplication", "division"]
    r = 0
    c = 0
    MAX_ROWS = 2
    for operand in operands:
        button = generateWidget(buttons_frame, "Button", text=operand, command=lambda op=operand: calculate(entry1, entry2, op),
                                width=10, height=2)
        button.grid(row=r, column=c)
        r += 1
        if r == MAX_ROWS:
            r = 0
            c += 1
    buttons_frame.pack()
