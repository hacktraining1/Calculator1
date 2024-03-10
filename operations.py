from getInput import getInput
from updateGUI import updateGUI, clearEntry
from ErrorWindow import throwError

def calculate(entry1_widget, entry2_widget, operand):
    operand = operand.strip().lower()
    left = float(getInput(entry1_widget))
    right = float(getInput(entry2_widget))
    operation = {
        'addition': left + right,
        'subtract': left - right,
        'multiplication': left * right,
        'division': None,
    }

    try:
        if operand == 'division':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            operation['division'] = left / right
        else:
            operation[operand]

        result = operation[operand]
        updateGUI(entry1_widget, entry2_widget, str(result))


    except ZeroDivisionError:
        clearEntry(entry2_widget)
        throwError()