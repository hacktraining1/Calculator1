import tkinter as tk
from additionOperation import addition
def generateButtons(window, entry1, entry2):
    #TODO MAKE THE DIFFERENT OPERATIONS
    add_button = tk.Button(window, text="Addition ", command=lambda: addition(entry1, entry2))
    add_button.grid(row=500, column=500, columnspan=2, pady=0)
    sub_button = tk.Button(window, text="Subtract ", command=lambda: addition(entry1, entry2))
    sub_button.grid(row=490, column=500, columnspan=2, pady=0)
    mult_button = tk.Button(window, text="Multiply", command=lambda: addition(entry1, entry2))
    mult_button.grid(row=490, column=490, columnspan=2, pady=0)
    div_button = tk.Button(window, text="  Divide  ", command=lambda: addition(entry1, entry2))
    div_button.grid(row=500, column=490, columnspan=2, pady=0)