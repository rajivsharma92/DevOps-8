def calculator():
    firstNumber = float(input("Enter the Number 1: "))
    secondNumber = float(input("Enter the Number 2: "))

    selectOperation = str(input("Select +, -, *, / :"))

    if selectOperation == "+":
        result = firstNumber + secondNumber
        print("Sum:", result)
        return result
        br
    elif selectOperation == "-":
        result = firstNumber - secondNumber
        print("Sub:", result)
        return result
    elif selectOperation == "/":
        result = firstNumber / secondNumber
        print("Div:", result)
        return result
    elif selectOperation == "*":
        result = firstNumber * secondNumber
        print("Mul:", result)
        return result
    else:
        print("Select from the operations list")
        return None

# Call the calculator function
calculator()
