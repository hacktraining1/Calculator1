import tkinter as tk



def generateMainWindow(title, size):
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    return window