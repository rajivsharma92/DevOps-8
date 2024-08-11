# Q2. Write a Python program to find the factorial of a number.
print("-----------Factorial Calculator---------------")

num = int(input("Enter the number for factorial: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i

print(f"Factorial of {num} is :", factorial) 