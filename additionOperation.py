from getInput import getInput
from updateGUI import updateGUI
def addition(entry1_widget, entry2_widget):

    result = int(getInput(entry1_widget)) + int(getInput(entry2_widget))
    updateGUI(entry1_widget, entry2_widget, str(result))