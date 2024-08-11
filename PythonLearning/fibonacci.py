print("----- To find the Fibonacci series of a number -----")

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci sequence:")
for i in range(n+1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print(".... end....")
