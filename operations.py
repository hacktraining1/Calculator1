from getInput import getInput
from updateGUI import updateGUI
def calculate(entry1_widget, entry2_widget, operand):
    operand = operand.strip().lower()
    left = float(getInput(entry1_widget))
    right = float(getInput(entry2_widget))
    operation = {
        'addition': left + right,
        'subtract': left - right,
        'multiplication': left*right,
        'division': left/right,
    }
    #TODO: handle zeroDivisionError
    result = operation[operand]
    updateGUI(entry1_widget, entry2_widget, str(result))