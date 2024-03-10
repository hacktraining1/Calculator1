from widgetFactory import generateWidget
from operations import calculate
def generateOutlook(window):
    # TODO DRY CODE - FIX
    # TODO SEE IF ALL CLASSES HAVE A COMMON ANCESTOR
    label1 = generateWidget(window, "Label", text="Input 1:")
    label1.pack(side="left", padx = (5,10))
    label2 = generateWidget(window, "Label", text="Input 2:")
    label2.pack(side="left", padx = (10,5))
    entry1 = generateWidget(window, "Entry")
    entry1.pack(pady=10)
    entry2 = generateWidget(window, "Entry")
    entry2.pack(pady=10)
    button = generateWidget(window, "Button", text="Click me!", command=lambda: calculate(entry1, entry2, "addition"))
    button.pack(pady=10)
    close_button = generateWidget(window, "Button", text="Close Calculator", command=lambda: window.destroy())
    close_button.pack(side="bottom", anchor="center", pady=20)
