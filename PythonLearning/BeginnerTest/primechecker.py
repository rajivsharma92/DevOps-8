# Q3. Write a Python program to check if a number is prime.

print("----------------Prime Checker-----------------")

number = int(input("Enter the number to check it is prime or not: "))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, sqrt(number) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(number))