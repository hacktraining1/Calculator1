from generateOutlook import generateOutlook
from GenerateMainWindow import generateMainWindow

WINDOW_NAME = "Calculator"
WINDOW_DIMENSIONS = "600x600"
window = generateMainWindow(WINDOW_NAME,WINDOW_DIMENSIONS)
generateOutlook(window)
window.mainloop()
