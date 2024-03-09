from getInput import getFirst
from updateGUI import updateGUI
def addition(entry1_widget, entry2_widget):

    result = int(getFirst(entry1_widget)) + int(getFirst(entry2_widget))
    updateGUI(entry1_widget, entry2_widget, str(result))