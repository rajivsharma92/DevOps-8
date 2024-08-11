import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        firstNumber = float(entry1.get())
        secondNumber = float(entry2.get())

        if operation == "+":
            result = firstNumber + secondNumber
        elif operation == "-":
            result = firstNumber - secondNumber
        elif operation == "*":
            result = firstNumber * secondNumber
        elif operation == "/":
            result = firstNumber / secondNumber

        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Division by zero", "Cannot divide by zero.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create and place the widgets
tk.Label(window, text="Number 1:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Number 2:").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

tk.Button(window, text="+", command=lambda: calculate("+")).grid(row=2, column=0)
tk.Button(window, text="-", command=lambda: calculate("-")).grid(row=2, column=1)
tk.Button(window, text="*", command=lambda: calculate("*")).grid(row=2, column=2)
tk.Button(window, text="/", command=lambda: calculate("/")).grid(row=2, column=3)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, columnspan=4)

# Run the main loop
window.mainloop()
