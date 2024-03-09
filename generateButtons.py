import tkinter as tk
from operations import calculate
def generateButtons(window, entry1, entry2):
    add_button = tk.Button(window, text="Addition ", command=lambda: calculate(entry1, entry2, "addition"))
    add_button.grid(row=500, column=500, columnspan=2, pady=0)
    sub_button = tk.Button(window, text="Subtract ", command=lambda: calculate(entry1, entry2, "subtract"))
    sub_button.grid(row=490, column=500, columnspan=2, pady=0)
    mult_button = tk.Button(window, text="Multiply", command=lambda: calculate(entry1, entry2, "multiplication"))
    mult_button.grid(row=490, column=490, columnspan=2, pady=0)
    div_button = tk.Button(window, text="  Divide  ", command=lambda: calculate(entry1, entry2, "division"))
    div_button.grid(row=500, column=490, columnspan=2, pady=0)