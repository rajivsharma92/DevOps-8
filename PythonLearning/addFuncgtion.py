def greet():
    print("Hello, welcome!")

def add_and_subtract(num1, num2):
    difference = num1 - num2
    print("The sum is:", num1 + num2)
    return difference

# Define the greet function
greet()
greet()

# Use the add_and_subtract function
result1 = add_and_subtract(10, 50)
result2 = add_and_subtract(20, 3)

print("The difference from first addition is:", result1)
print("The difference from second addition is:", result2)
