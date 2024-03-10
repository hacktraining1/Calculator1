import tkinter as tk
from GenerateMainWindow import generateMainWindow
from widgetFactory import generateWidget

def throwError():
    error_window = generateMainWindow("Error!", "600x200")
    label = generateWidget(error_window, "Label", text="Error! Cannot divide by 0!".upper(), font=("Calibri", 36)
                           ,foreground="red")
    label.pack(side="top", anchor="center", pady=20)
    button = generateWidget(error_window, "Button", text = "Close", command=lambda: error_window.destroy())
    button.pack(side="top", anchor="center", pady=20)
    error_window.mainloop()