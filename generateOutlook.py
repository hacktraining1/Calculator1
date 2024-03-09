from generateButtons import generateButtons
from generateLabels import generateLabel, setLabelPosition
from generateEntry import generateEntry, setEntryPosition
def generateOutlook(window):
    # TODO DRY CODE - FIX
    # TODO SEE IF ALL CLASSES HAVE A COMMON ANCESTOR
    label1 = generateLabel(window, "Input 1")
    setLabelPosition(label1, 0, 0, 10, 10)
    label2 = generateLabel(window, "Input 2")
    setLabelPosition(label2, 0, 1, 10, 10)
    entry1 = generateEntry(window)
    setEntryPosition(entry1,1,0,10,10)
    entry2 = generateEntry(window)
    setEntryPosition(entry2,1,1,10,10)
    generateButtons(window,entry1,entry2)
