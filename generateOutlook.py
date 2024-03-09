import tkinter as tk
from additionOperation import addition
def generateOutlook(window):
    label1 = tk.Label(window, text="Input 1:")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(window)
    entry1.grid(row=1, column=0, padx=10, pady=10)

    # Create and place the second input field
    label2 = tk.Label(window, text="Input 2:")
    label2.grid(row=0, column=1, padx=10, pady=10)
    entry2 = tk.Entry(window)
    entry2.grid(row=1, column=1, padx=10, pady=10)

    # Create and place the submit button
    add_button = tk.Button(window, text="Addition", command=lambda: addition(entry1, entry2))
    add_button.grid(row=2, column=1, columnspan=2, pady=10)
