import tkinter as tk

def generateWidget(parent, widget_type, **kwargs):
    widget = getattr(tk, widget_type)(parent, **kwargs)
    return widget