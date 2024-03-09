import tkinter as tk

def getFirst():
    return entry1.get()
def getSecond():
    return entry2.get()
def updateGUI(result):
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.insert(0, result)
def addition():
    result = int(getFirst())
    second = int(getSecond())
    result += second
    updateGUI(str(result))


# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")

# Create and place the first input field
label1 = tk.Label(window, text="Input 1:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(window)
entry1.grid(row=1, column=0, padx=10, pady=10)

# Create and place the second input field
label2 = tk.Label(window, text="Input 2:")
label2.grid(row=0, column=1, padx=10, pady=10)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create and place the submit button
add_button = tk.Button(window, text="Addition", command=addition)
add_button.grid(row=2, column=1, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()