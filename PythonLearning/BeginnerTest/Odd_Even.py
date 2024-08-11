# Write a Python program to check if a number is even or odd.

num = int(input("Enter the integer poitive only: "))
try:
    if num>0 and num%2 == 0:
        print(f"Entered number {num} is even")
    else:
        print(f"Entered Number {num} is odd")

except:
    print(f"Enterd {num} is not valid")
